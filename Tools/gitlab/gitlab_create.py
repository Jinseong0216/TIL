from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from getpass import getpass

options = Options()
# userAgent=f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Whale/3.27.254.15 Safari/537.36'
options.add_argument("headless")
options.add_argument("log-level=3")
options.add_argument('--blink-settings=imagesEnabled=false')
options.add_argument("--start-maximized")
options.add_argument("--window-size=1920,1080")
options.add_experimental_option('excludeSwitches', ['enable-logging', 'enable-automation'])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument('--disable-blink-features=AutomationControlled')
# options.add_argument(userAgent)
service = Service(executable_path=ChromeDriverManager().install())
url = 'https://project.ssafy.com'

dr = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(dr, 5)
dr.get(url)
dr.implicitly_wait(4)

id_box = dr.find_element(By.ID,"userId")
password_box = dr.find_element(By.ID,"userPwd")

while True:
    button = dr.find_elements(By.CLASS_NAME,'btn')
    login_button=button[0]
    
    act = ActionChains(dr)
    dr.implicitly_wait(2)
    
    if len(button)>1:
        print("아이디 또는 비밀번호를 잘못 입력하였습니다. 다시 입력해주세요.")
        modal_button=button[1]
        act.click(modal_button).perform()
        id_box.send_keys(Keys.CONTROL + "a")
        id_box.send_keys(Keys.DELETE)
        password_box.send_keys(Keys.CONTROL + "a")
        password_box.send_keys(Keys.DELETE)
    dr.implicitly_wait(2)
    
    id =   input("\nGitlab ID : ")
    password = getpass("Gitlab PASSWORD : ")
    act.send_keys_to_element(id_box, '{}'.format(id)).send_keys_to_element(password_box,'{}'.format(password)).click(login_button).perform()
    time.sleep(5)
    dr.implicitly_wait(5)
    if dr.current_url == 'https://project.ssafy.com/login?returnPath=%2Fhome':continue
    break
act = ActionChains(dr)
print("\n깃랩 로그인 성공!\n")
dr.implicitly_wait(4)
Xpath="//div[contains(@class,'tit_')]//a"
elements=dr.find_elements(By.XPATH, Xpath)
sub=[]
i=0
for e in elements:
    i+=1
    sub.append(e)
    print(f'{i}. {e.text}', end='\t')
print()
x=0
while x<1 or x>3:
    try:x=int(input("\n실습실을 생성할 과목을 선택해주세요 : "))
    except:print("정수만 입력해주세요.")
    else:
        if x<1 or x>3:print("1과 3 사이 숫자만 입력해주세요.")

print("\n목록을 불러오는 중입니다...\n")
select=sub[x-1]
act.click(select).perform()
time.sleep(3)
table=dr.find_element(By.CLASS_NAME, 'con_table')
lst=table.find_elements(By.TAG_NAME, 'a')
N=len(lst)
x=0
while x<1 or x>N:
    try:x=int(input('차수를 입력해주세요. (ex> 2차. Templates ==> 2) : '))
    except:print("정수를 입력해주세요.")
    else:
        if x<1 or x>N:print("없는 차수입니다. 다시 입력해주세요.")
print(f"\n {x}차수 실습실 생성 시도중 입니다...\n")
select=lst[x-1]
act.click(select).perform()
time.sleep(2)
page=dr.current_url
tab=[]
for i in range(9):
    tab.append(dr.current_window_handle)
    dr.execute_script(f'window.open("{page}");')
    dr.switch_to.window(dr.window_handles[-1])
tab.append(dr.current_window_handle)
Xpath="//a[contains(text(),'상세보기')]"
for i in range(10):
    dr.switch_to.window(tab[i])
    #elements=dr.find_elements(By.XPATH, Xpath)
    time.sleep(3)
    try:
        elements=dr.find_elements(By.XPATH, Xpath)
        name = WebDriverWait(dr, 5).until(EC.element_to_be_clickable(elements[i]))
        name.click()
    except:
        try:
            print("재시도중...")
            elements=dr.find_elements(By.XPATH, Xpath)
            name = WebDriverWait(dr, 5).until(EC.element_to_be_clickable(elements[i]))
            name.send_keys(Keys.ENTER)
        except:
            try:
                print("재시도중......")
                elements=dr.find_elements(By.XPATH, Xpath)
                name = WebDriverWait(dr, 5).until(EC.element_to_be_clickable(elements[i]))
                dr.execute_script("arguments[0].click();", name)
            except:
                print(f"{i+1}번째 실습실 생성 문제 생김....")
                break
    time.sleep(3)
    print(f'{i+1}. \"{dr.find_element(By.CLASS_NAME, "title").find_element(By.TAG_NAME, "h3").get_attribute("title")}\" 실습실 생성중....')
    pro=dr.find_element(By.XPATH, "//a[contains(text(),'실습하기')]")
    try:
        pro=dr.find_element(By.XPATH, "//a[contains(text(),'실습하기')]")
        name = WebDriverWait(dr, 5).until(EC.element_to_be_clickable(pro))
        name.click()
    except:
        try:
            pro=dr.find_element(By.XPATH, "//a[contains(text(),'실습하기')]")
            print("재시도중...")
            name = WebDriverWait(dr, 5).until(EC.element_to_be_clickable(pro))
            dr.execute_script("arguments[0].click();", name)
        except:
            try:
                pro=dr.find_element(By.XPATH, "//a[contains(text(),'실습하기')]")
                print("재시도중......")
                name = WebDriverWait(dr, 5).until(EC.element_to_be_clickable(pro))
                name.send_keys(Keys.ENTER)
            except:
                print(f"{i+1}번째 실습실 생성 문제 생김....")
                break
    time.sleep(3)
    dr.switch_to.window(tab[i])
    dr.close()
else:
    for i in range(10):
        dr.switch_to.window(dr.window_handles[-1])
        dr.close()
    print('실습실 생성 성공!')