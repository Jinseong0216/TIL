import input_data
import drivers
import get_edu_data


def main():
    flag = 1
    while flag:
        # 로그인 정보
        user = input_data.get_user()
        # 드라이버 생성
        driver = drivers.make_driver()
        # 로그인 진행
        drivers.login(driver, user.id, user.pwd)
        # 성공여부 확인
        flag = drivers.is_login_valid(driver)
        if flag:
            print('================== 로그인 실패 -/- ==================')
    # 다운로드 관련 명령 입력
    track, command = input_data.get_command()
    # 트랙 페이지 들어가기
    drivers.enter_data_page(driver, track.track)
    # 코스 정보 받아오기
    course_dic, last_page = drivers.get_course_list(driver)
    # 코스 리스트 출력        
    drivers.print_course_list(course_dic, last_page)  
    driver.quit()

    flag = True
    
    target_pages = []
    command.download_info['is_total_download'] = input('모든 코스 저장여부 Y/N: ').strip().upper()

    if command.download_info['is_total_download'] == 'Y':
        for page in range(1, last_page+1):
            for course_order in range(1, len(course_dic[page])+1):
                target_pages.append([page, course_order])
        flag = False
    else:
        command.download_info['is_specific_download'] = input('특정 페이지의 모든 코스 저장여부 Y/N: ').strip().upper()
    
    if command.download_info['is_specific_download'] == 'Y':
        page = int(input('저장을 원하는 페이지 입력, ex. 1, 3, 4, 5, ..: ').strip())
        for course_order in range(1, len(course_dic[page])+1):
            target_pages.append([page, course_order])
        flag = False

    while flag:
        print('================== 저장할 페이지 및 코스 번호 입력 ================== ')
        page, course_order =  int(input('페이지 입력: ').strip()), int(input('코스 번호 입력: ').strip())
        target_pages.append([page, course_order])
        if input('페이지 및 코스 번호 추가 입력 여부 Y/N: ').strip().upper() == 'Y': flag = True
        else: flag = False

    for page, course_order in target_pages:
        driver = drivers.make_driver()
        # 수업자료 열기
        drivers.open_lecture_pdf(driver, user, course_dic, track, page, course_order)
        # 페이지 정보 및 이미지 URL 가져옴
        total_pages, base_url = get_edu_data.get_page_data(driver)
        # 수업자료 pdf로 저장
        get_edu_data.save_pdfs(driver, total_pages, base_url, track, course_dic, page, course_order)



    # PDF 병합 여부 확인
    if command.is_merge == 'Y':
        print('알아서.. 잘 병합하십쇼..')

    print('pdf 추출 완료^^:)')


if __name__ == '__main__':
    main()