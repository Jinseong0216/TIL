from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


text = '''
webdrive 숨김 옵션이 적용되지않는 selenium 버그 존재함(2024/10/04 기준)
    options.add_argument("log-level=3")
    options.add_argument("lang=ko_KR")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Whale/3.27.254.15 Safari/537.36")
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36")
    를 추가하면 임시방편으로 해결이 가능하다 함.
'''
# ======================================== DriverOptions 설정 =================================
def make_driver():
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
    driver = webdriver.Chrome(options=options)
    return driver
##############################################################################################
##############################################################################################


# ======================================== 로그인 진행 =================================
def login(driver, id, pwd):
    # 로그인 url
    login_url = 'https://edu.ssafy.com/comm/login/SecurityLoginForm.do'
    # 로그인 url로 들어가기
    driver.get(login_url)

    # id, pwd 입력 및 로그인 버튼 클릭
    driver.find_element(By.XPATH, '//*[@id="userId"]').send_keys(id)
    driver.find_element(By.XPATH, '//*[@id="userPwd"]').send_keys(pwd)
    driver.find_element(By.XPATH, '//*[@id="wrap"]/div/div/div[2]/form/div/div[2]/div[3]/a').click()
##############################################################################################
##############################################################################################


# ======================================== 특정 주차의 커리큘럼 들어가기 ========================================
def enter_curriculum_page(driver, week):
    # 주차별 커리큘럼 버튼 XPATH
    weekly_curriculum_btn_xpath = '//*[@id="wrap"]/div[1]/div[1]/section[2]/div/div[1]/div/a'
    # edussafy main페이지의 주차별 커리큘럼버튼이 로드될 때까지 대기
    weekly_curriculum_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, weekly_curriculum_btn_xpath)))
    # 주차별 커리큘럼 버튼 클릭
    weekly_curriculum_btn.click()
    time.sleep(1)
    # 특정 주차로 들어가는 버튼
    week_btn_xpath = f'//*[@id="_crclmWeekTargetId"]/div/div[2]/div[1]/div[1]/div[{week}]/span[2]'
    # 특정 주차의 커리큘럼 버튼이 생성될 때까지 대기
    week_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, week_btn_xpath)))
    # 특정 주차의 커리큘럼 버튼 클릭
    week_element.click()
    time.sleep(1)
##############################################################################################
##############################################################################################


# ======================================== 수업 교재 화면까지 들어가기 ========================================
def open_lecture_pdf(driver, day):
    # day번째 수업 교재 버튼의 XPATH가 ...button[2]인 경우와 ...button인 경우로 두가지가 존재함
    day_btn_xpath = f'//*[@id="_crclmDayTargetId"]/li[{day}]/dl[1]/dd/div[2]/button[2]'
    try:
        # day번째 수업 교재 버튼이 생성될 때까지 대기
        book_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, day_btn_xpath))
        )
    except:
        # day번째 수업 교재 버튼이 생성될 때까지 대기
        day_btn_xpath = f'//*[@id="_crclmDayTargetId"]/li[{day}]/dl[1]/dd/div[2]/button'
        book_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, day_btn_xpath))
        )

    # day번째 수업 교재 버튼 클릭
    book_btn.click()
    time.sleep(1)
    # 수업교재 자세히보기 버튼 XPATH
    book_detail_btn_xpath = '//*[@id="mainMatlPopup"]/div[2]/form/div[1]/div/div[2]/div[1]/dl/dd/div/a/span'
    # 수업교재 자세히보기 버튼이 생성될 때까지 대기
    book_detail_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, book_detail_btn_xpath)))
    # 수업교재 자세히보기 버튼 클릭
    book_detail_btn.click()
    # 잠시 대기
    time.sleep(1)
    # 수업 교재 화면을 current tap으로
    current_tab = driver.window_handles[1]
    # driver를 수업 교재 화면이 존재하는 탭으로 이동
    driver.switch_to.window(current_tab)
######################################################################################
######################################################################################


if __name__ == '__main__':
    print(text)

