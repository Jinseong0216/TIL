from input_data import get_data
from drivers import *
from get_edu_data import *
from tqdm import tqdm  # tqdm 임포트 추가


def main():
    # 로그인 정보 및 다운로드할 주차별 정보
    user, week, command = get_data()

    # 드라이버 생성
    driver = make_driver()
    # 로그인 진행
    login(driver, user.id, user.pwd)

    try:
        enter_curriculum_page(driver, week.now)
        # day는 특정 주차의 첫번째 수업을 의미
        day_lst = [command.day_only] if command.day_only else list(range(1, 6))

        # 진행도 표시를 위한 tqdm 설정
        with tqdm(total=len(day_lst), desc='수업 자료 다운로드 진행', unit='수업') as pbar:
            for day in day_lst:  # day_lst에 포함된 요일만 반복
                try:
                    # 수업자료 열기
                    open_lecture_pdf(driver, day)
                    # 페이지 정보 및 이미지 URL 가져옴
                    total_pages, base_url = get_page_data(driver)
                    # 이미지 추출 및 저장
                    save_pdfs(driver, total_pages, base_url, week.now, day)
                    # 진행도 업데이트
                    pbar.update(1)  # 각 수업 자료 다운로드 후 1단계 업데이트
                except Exception as e:
                    print(f"Day {day}에서 오류 발생: {e}")
                    pbar.update(1)  # 오류가 발생해도 진행 상황을 1단계 업데이트
    except Exception as e:
        print(f"전체 과정에서 오류 발생: {e}")
    finally:
        # 드라이버 종료
        driver.quit()

    # PDF 병합 여부 확인
    if command.is_merge == 'Y':
        merge_pdfs(week.now)

    print('pdf 추출 완료^^:)')


if __name__ == '__main__':
    main()