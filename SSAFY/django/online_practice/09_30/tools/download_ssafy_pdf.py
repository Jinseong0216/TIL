from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import os
from fpdf import FPDF

def images_to_pdf(image_files, output_pdf):
    pdf = FPDF()
    for image_file in image_files:
        pdf.add_page()
        try:
            pdf.image(image_file, x=0, y=0, w=210, h=297)
        except Exception as e:
            print(f"이미지 추가 실패: {e} - 파일: {image_file}")
    pdf.output(output_pdf)

def download_image(url, folder):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            image_name = os.path.join(folder, url.split('/')[-1])
            with open(image_name, 'wb') as f:
                f.write(response.content)
            return image_name
    except Exception as e:
        print(f"이미지 다운로드 실패: {e}")
    return None

# 이미지 저장 폴더 생성
if not os.path.exists('./images'):
    os.makedirs('./images')

driver = webdriver.Chrome()
driver.get('https://edu.ssafy.com/comm/login/SecurityLoginForm.do')

start_week = int(input('다운로드 시작 주: ex. 3 '))
end_week = int(input('다운로드 종료 주: ex. 5 '))
user_id = 'pnum2378@naver.com'
user_pwd = 'yoosd216!'

# 로그인
driver.find_element(By.XPATH, '//*[@id="userId"]').send_keys(user_id)
driver.find_element(By.XPATH, '//*[@id="userPwd"]').send_keys(user_pwd)
driver.find_element(By.XPATH, '//*[@id="wrap"]/div/div/div[2]/form/div/div[2]/div[3]/a').click()

# 로그인 후 특정 요소가 로드될 때까지 대기 후 클릭
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="wrap"]/div[1]/div[1]/section[2]/div/div[1]/div/a'))
)
driver.find_element(By.XPATH, '//*[@id="wrap"]/div[1]/div[1]/section[2]/div/div[1]/div/a').click()

# 각 주차별 버튼 xpath
xpath_dic = {week: f'//*[@id="_crclmWeekTargetId"]/div/div[2]/div[1]/div[1]/div[{week}]/span[2]' for week in range(1, 22)}

images = []  # 모든 이미지를 담을 리스트

for week in range(start_week, end_week + 1):
    print(f'주: {week}')
    
    try:
        for day in range(1, 2):  # 여기에 날짜를 조정할 수 있습니다
            try:
                book_btn = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, f'//*[@id="_crclmDayTargetId"]/li[{day}]/dl[1]/dd/div[2]/button[2]'))
                )
                book_btn.click()

                driver.implicitly_wait(3)
                driver.find_element(By.XPATH, '//*[@id="mainMatlPopup"]/div[2]/form/div[1]/div/div[2]/div[1]/dl/dd/div/a/span').click()
                driver.switch_to.window(driver.window_handles[1])
                
                # 대기 후 모든 img 태그 찾기
                WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.TAG_NAME, 'img'))
                )
                img_elements = driver.find_elements(By.TAG_NAME, 'img')
                
                # 이미지 다운로드
                for img in img_elements:
                    img_src = img.get_attribute('src')
                    if img_src:  # 이미지 URL이 존재하는지 확인
                        print(f"다운로드 중: {img_src}")  # URL 확인
                        image_file = download_image(img_src, './images')  # 이미지를 'images' 폴더에 다운로드
                        if image_file:
                            images.append(image_file)

                driver.close()
                driver.switch_to.window(driver.window_handles[0])
                driver.find_element(By.XPATH, '//*[@id="mainMatlPopup"]/div[1]/button').click()
            except Exception as e:
                print(f"주 {week}, 일 {day}에서 오류 발생: {e}")
    except Exception as e:
        print(f"주 {week}에서 오류 발생: {e}")

# PDF 생성
if images:
    images_to_pdf(images, 'output.pdf')

driver.quit()
