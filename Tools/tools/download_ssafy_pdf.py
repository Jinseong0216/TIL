# 사용자 입력 데이터 얻어오기 모듈
from input_data import get_data


import os

# 파싱관련
# webdriver
from selenium import webdriver
# webdriver에 옵션 넣기 위함
from selenium.webdriver.chrome.options import Options
# find_element에 사용
from selenium.webdriver.common.by import By
# 요소 로드까지 대기를 위함
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup   
# driver 일시정지
import time
# 입력 보안을 위함
import getpass
# 이미지 저장
from PIL import Image


'''
시작 및 종료주차 관련
    edussafy login session이 간헐적으로 종료되는 경우가 존재함.
    week.start와 week.end를 같게 처리하여 해결.
    session 유지가 가능하면 end_week = int(input('xxx').strip())로 변경하면 코드 그대로 작동함.

webdrive 숨김 옵션이 적용되지않는 selenium 버그 존재함(2024/10/04 기준)
    options.add_argument("log-level=3")
    options.add_argument("lang=ko_KR")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Whale/3.27.254.15 Safari/537.36")
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36")
    를 추가하면 임시방편으로 해결이 가능하다 함.
'''


# 로그인 정보 및 다운로드할 주차별 정보
user, week = get_data()

for week in range(week.start, week.end+1):  # 주차
    # ======================================== ChromeOptions 설정 =================================
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
    ##############################################################################################
    ##############################################################################################

    options = make_driver_option()
    # ======================================== start webdriver 설정 ===============================
    driver = webdriver.Chrome(options=options.options)
    # edussafy login page에서 시작
    driver.get('https://edu.ssafy.com/comm/login/SecurityLoginForm.do')
    ##############################################################################################
    ##############################################################################################


    # ======================================== 로그인 설정 =========================================
    # user_id에 아이디 입력
    driver.find_element(By.XPATH, '//*[@id="userId"]').send_keys(user.id)
    # user_Pwd에 비밀번호 입력
    driver.find_element(By.XPATH, '//*[@id="userPwd"]').send_keys(user.pwd)
    # 로그인 버튼 클릭
    driver.find_element(By.XPATH, '//*[@id="wrap"]/div/div/div[2]/form/div/div[2]/div[3]/a').click()
    ##############################################################################################
    ##############################################################################################


    # ======================================== 주차별 커리큘럼 들어가기 =============================
    # 주차별 커리큘럼 버튼 XPATH
    weekly_curriculum_btn_xpath = '//*[@id="wrap"]/div[1]/div[1]/section[2]/div/div[1]/div/a'
    # edussafy main페이지의 주차별 커리큘럼버튼이 로드될 때까지 대기
    weekly_curriculum_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, weekly_curriculum_btn_xpath)))
    # 주차별 커리큘럼 버튼 클릭
    weekly_curriculum_btn.click()
    ##############################################################################################
    ##############################################################################################


    # ======================================== 특정 주차로 들어가는 버튼 XPATH 생성 =================
    xpath_dic = {week: f'//*[@id="_crclmWeekTargetId"]/div/div[2]/div[1]/div[1]/div[{week}]/span[2]' for week in range(1, 22)}
    ##############################################################################################
    ##############################################################################################


    try:
        # ======================================== 특정 주차의 커리큘럼 들어가기 ====================
        # 특정 주차의 커리큘럼 버튼이 생성될 때까지 대기
        week_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath_dic[week])))
        # 특정 주차의 커리큘럼 버튼 클릭
        week_element.click()
        ##############################################################################################
        ##############################################################################################


        # day는 특정 주차의 첫번째 수업을 의미
        for day in range(1, 6):  # 날짜
            try:
                # ======================================== 수업 교재 화면까지 들어가기 =================
                # day번째 수업 교재 버튼의 XPATH가 ...button[2]인 경우와 ...button인 경우로 두가지가 존재함
                # 이를 위해 xpath 내부에 | 연산자를 적용함
                day_btn_xpath = f'//*[@id="_crclmDayTargetId"]/li[{day}]/dl[1]/dd/div[2]/button[2] | //*[@id="_crclmDayTargetId"]/li[{day}]/dl[1]/dd/div[2]/button'
                # day번째 수업 교재 버튼이 생성될 때까지 대기
                book_btn = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, day_btn_xpath))
                )
                # day번째 수업 교재 버튼 클릭
                book_btn.click()

                # 수업교재 자세히보기 버튼 XPATH
                book_detail_btn_xpath = '//*[@id="mainMatlPopup"]/div[2]/form/div[1]/div/div[2]/div[1]/dl/dd/div/a/span'
                # 수업교재 자세히보기 버튼이 생성될 때까지 대기
                book_detail_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, book_detail_btn_xpath)))
                # 수업교재 자세히보기 버튼 클릭
                book_detail_btn.click()
                ######################################################################################
                ######################################################################################


                # ======================================== driver 탭 관리 =============================
                # 잠시 대기
                time.sleep(1)
                # 수업 교재 화면을 current tap으로
                current_tab = driver.window_handles[1]
                # driver를 수업 교재 화면이 존재하는 탭으로 이동
                driver.switch_to.window(current_tab)
                ######################################################################################
                ######################################################################################


                # ========================================  수업 교재 화면 데이터 파싱 =================
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                ######################################################################################
                ######################################################################################


                # ======================================== 전체 페이지 수 추출 =========================
                # 1/105 같은 형식으로 되어있음 현재 페이지/마지막 페이지를 의미함
                total_pages = soup.find('span', class_='label-page').text
                # 페이지 수 추출
                total_pages = int(total_pages.split(' / ')[-1]) 
                ######################################################################################
                ######################################################################################


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