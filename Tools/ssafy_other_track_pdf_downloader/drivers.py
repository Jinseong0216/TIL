from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from pprint import pprint


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
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36")
    options.add_argument("--start-maximized")  # 창 최대화
    options.add_argument("--window-size=1920,1080")  # 고해상도 설정
    options.add_argument("--headless=old") # 숨김
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


# ======================================== 로그인 성공여부 확인 =================================
def is_login_valid(driver):
    try:
        driver.find_element(By.XPATH, '//*[@id="wrap"]/div[1]/div[1]/section[3]/div/div[1]/a')
        return 0
    except:
        driver.quit()
        return 1
##############################################################################################
##############################################################################################


# ======================================== 학습자료 들어가기 ========================================
def enter_data_page(driver, track):
    # 학습자료 버튼 XPATH
    edu_data_btn_xpath = '//*[@id="wrap"]/div[1]/div[1]/section[3]/div/div[1]/a'
    # edussafy main페이지의 주차별 커리큘럼버튼이 로드될 때까지 대기
    edu_data_btn = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, edu_data_btn_xpath)))
    edu_data_btn.click()
    time.sleep(1)

    # 입력 input
    keyword_input_xpath = '//*[@id="searchContNm"]'
    keyword_input= WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, keyword_input_xpath)))
    keyword_input.send_keys(track)
    time.sleep(1)    

    # 전송    
    send_btn_xpath = '//*[@id="wrap"]/div/div[2]/div[2]/div[1]/div/button'
    send_btn = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, send_btn_xpath)))
    send_btn.click()
    time.sleep(1)
##############################################################################################
##############################################################################################


def get_course_list(driver):
    # 코스정보 저장
    course_dic, course_list, page, num = {}, [], 1, 1
    while True:
        next_btn = driver.find_element(By.CLASS_NAME,'next')
        try:
            course_xpath = f'//*[@id="wrap"]/div/div[2]/div[2]/div[2]/ul/li[{num}]/div/div[1]/a'
            course_element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, course_xpath)))
            course_list.append([num, course_element.text, course_xpath])
            num += 1
        except:
            course_dic[page] = course_list
            course_list = []
            # 다음 페이지로
            next_btn = driver.find_element(By.CLASS_NAME,'next')
            if 'disabled' in next_btn.get_attribute('class'): 
                break
            else: 
                next_btn.click()
                num = 1
                page += 1

    
    return course_dic, page
##############################################################################################
##############################################################################################


# ======================================== 코스 리스트 출력 ========================================
def print_course_list(course_dic, last_page):
    for page in range(1, last_page+1):
        print(f'==================== {page}페이지의 코스 정보 ====================')
        for idx, course, xpath in course_dic[page]:
            print(f'{idx}. {course}')
        print()
##############################################################################################
##############################################################################################


# ======================================== 수업 교재 화면까지 들어가기 ========================================
def open_lecture_pdf(driver, user, course_dic, track, page, order):
    login(driver, user.id, user.pwd)
    enter_data_page(driver, track.track)
    # 입력한 페이지로 이동
    for _ in range(page-1): 
        time.sleep(1)
        driver.find_element(By.CLASS_NAME,'next').click()
    course_xpath = course_dic[page][order-1][2]
    WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, course_xpath))).click()
    eBook_btn_xpath = '//*[@id="wrap"]/div/div[2]/div/div/dl/dd/div/a/span'
    WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, eBook_btn_xpath))).click()
    # 교재 화면까지 들가기기 완료
    # 드라이버 탭 전환
    time.sleep(1)
    # 수업 교재 화면을 current tap으로
    current_tab = driver.window_handles[1]
    # driver를 수업 교재 화면이 존재하는 탭으로 이동
    driver.switch_to.window(current_tab)
##############################################################################################
##############################################################################################



if __name__ == '__main__':
    print(text)

