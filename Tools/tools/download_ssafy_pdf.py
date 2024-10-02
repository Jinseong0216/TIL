import os
# 파싱관련
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup   
# driver 일시정지
import time
# 입력 보안을 위함
import getpass
# 이미지 저장
from PIL import Image




# 로그인 정보
user_id = input('edussafy_id: ')
user_pwd = getpass.getpass('eddussafy_password: ')

# 다운로드 할 주차별 정보
start_week = int(input('다운로드를 진행할 추차: ex. 12주차면, 12 <------를 입력하시면 됩니다 ^^:)').strip())
end_week = start_week



# 이미지 다운로드 코드
for week in range(start_week, end_week+1):  # 주차
    # ChromeOptions 설정
    options = Options()
    options.add_argument("log-level=3")
    options.add_argument("lang=ko_KR")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Whale/3.27.254.15 Safari/537.36")
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36")
    options.add_argument("--start-maximized")  # 창 최대화
    options.add_argument("--window-size=1920,1080")  # 고해상도 설정
    options.add_argument("headless") # 숨김
    options.add_experimental_option('excludeSwitches', ['enable-logging', 'enable-automation'])
    options.add_experimental_option("useAutomationExtension", False)
    # 웹 드라이버 초기화
    driver = webdriver.Chrome(options=options)
    driver.get('https://edu.ssafy.com/comm/login/SecurityLoginForm.do')

    # 로그인
    driver.find_element(By.XPATH, '//*[@id="userId"]').send_keys(user_id)
    driver.find_element(By.XPATH, '//*[@id="userPwd"]').send_keys(user_pwd)
    driver.find_element(By.XPATH, '//*[@id="wrap"]/div/div/div[2]/form/div/div[2]/div[3]/a').click()
    # ======================================== 로그인 완료 ========================================

    # 특정 요소가 로드될 때까지 대기 후 클릭
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="wrap"]/div[1]/div[1]/section[2]/div/div[1]/div/a'))
    )
    driver.find_element(By.XPATH, '//*[@id="wrap"]/div[1]/div[1]/section[2]/div/div[1]/div/a').click()

    # 주차별 버튼
    xpath_dic = {week: f'//*[@id="_crclmWeekTargetId"]/div/div[2]/div[1]/div[1]/div[{week}]/span[2]' for week in range(1, 22)}
    # ======================================== 로그인 완료 ========================================

    try:        
        week_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath_dic[week])))
        week_element.click()
        # 해당 주차 커리큘럼 목록으로 들어감
        for day in range(1, 6):  # 날짜
            if day == 1:
                print('='*50, '( 0/100)', '='*50)
            else:
                percentage = (day-1)*18
                print('='*50, f'({percentage}/100)', '='*50)
            try:
                book_btn = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, f'//*[@id="_crclmDayTargetId"]/li[{day}]/dl[1]/dd/div[2]/button[2] | //*[@id="_crclmDayTargetId"]/li[{day}]/dl[1]/dd/div[2]/button'))
                )
                book_btn.click()

                driver.implicitly_wait(3)
                driver.find_element(By.XPATH, '//*[@id="mainMatlPopup"]/div[2]/form/div[1]/div/div[2]/div[1]/dl/dd/div/a/span').click()

                time.sleep(3)
                current_tab = driver.window_handles[1]
                driver.switch_to.window(current_tab)


                soup = BeautifulSoup(driver.page_source, 'html.parser')
                label_page = soup.find('span', class_='label-page')

                # 텍스트 추출
                page_text = label_page.text
                # 페이지 수 추출
                total_pages = int(page_text.split(' / ')[-1])

                img_tags = soup.find_all('img', class_='background')

                img_url = [img['src'] for img in img_tags][0]
                base_url = driver.current_url[:-10]

                # 주차와 일자에 해당하는 디렉토리 생성
                dir_name = f'week_{week}_day_{day}'
                os.makedirs(dir_name, exist_ok=True)

                for idx in range(1, 1 + total_pages):
                    img_num = "{0:0=4d}".format(idx)
                    # full_url 구성
                    full_url = base_url + img_url[:-8] + img_num + '.jpg'
                    
                    # 이미지 페이지로 이동
                    driver.get(full_url)

                    # 스크린샷 캡쳐
                    screenshot_path = os.path.join(dir_name, f'screenshot_week_{week}_day_{img_num}.png')
                    driver.save_screenshot(screenshot_path)  # 전체 페이지 캡처


                driver.close()  # 현재 탭 닫기
                driver.switch_to.window(driver.window_handles[0])  # 기본 탭으로 돌아가기
                time.sleep(1)
                driver.find_element(By.XPATH, '//*[@id="mainMatlPopup"]/div[1]/button').click()            

                # JPG를 PDF로 변환하고 JPG 삭제
                jpg_files = [f for f in os.listdir(dir_name) if f.endswith('.png')]
                if jpg_files:
                    pdf_path = os.path.join(dir_name, f'week_{week}_day_{day}.pdf')
                    images = [Image.open(os.path.join(dir_name, f)) for f in jpg_files]
                    images[0].save(pdf_path, save_all=True, append_images=images[1:])

                    # JPG 파일 삭제
                    for f in jpg_files:
                        os.remove(os.path.join(dir_name, f))

            except Exception as e:
                pass
    except Exception as e:
        pass
    # 드라이버 종료
    driver.quit()
    print('='*50, '(90/100)', '='*50)
    # 병합 ==========================================================================================================
    import PyPDF2

    def merge_pdfs(week):
        # 주차 디렉토리
        week_dir = os.getcwd()
        
        # 주차 내의 모든 'day' 디렉토리 탐색
        day_dirs = [d for d in os.listdir(week_dir) if d.startswith(f'week_{week}_day_')]

        # PDF 머지 객체 생성
        merger = PyPDF2.PdfMerger()

        # 각 'day' 디렉토리에서 PDF 파일 추가
        for day_dir in day_dirs:
            day_path = os.path.join(week_dir, day_dir)
            pdf_files = [f for f in os.listdir(day_path) if f.endswith('.pdf')]
            
            for pdf in pdf_files:
                pdf_path = os.path.join(day_path, pdf)
                merger.append(pdf_path)

        # 병합된 PDF를 현재 디렉토리에 저장
        merged_pdf_path = os.path.join(os.getcwd(), f'merged_week_{week}.pdf')
        merger.write(merged_pdf_path)
        merger.close()

    print('='*50, '(95/100)', '='*50)
    # pdf병합
    merge_pdfs(week) 
    print('='*50, '(100/100)', '='*50)
    print('pdf추출 완료^^:)')