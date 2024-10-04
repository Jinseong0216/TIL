from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

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
#     options.add_argument("headless") # 숨김
    options.add_experimental_option('excludeSwitches', ['enable-logging', 'enable-automation'])
    options.add_experimental_option("useAutomationExtension", False)
    driver = webdriver.Chrome(options=options)
##############################################################################################
##############################################################################################


def login(id, pwd):
    # 로그인 url
    login_url = 'https://edu.ssafy.com/comm/login/SecurityLoginForm.do'
    # 로그인 url로 들어가기
    driver.get(login_url)

    # id, pwd 입력 및 로그인 버튼 클릭
    driver.find_element(By.XPATH, '//*[@id="userId"]').send_keys(id)
    driver.find_element(By.XPATH, '//*[@id="userPwd"]').send_keys(pwd)
    driver.find_element(By.XPATH, '//*[@id="wrap"]/div/div/div[2]/form/div/div[2]/div[3]/a').click()



if __name__ == '__main__':
    print(text)