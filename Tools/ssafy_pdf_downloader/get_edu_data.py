from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from PIL import Image
import PyPDF2


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

# ======================================== 페이지 수, 이미지의 base_url 추출 ========================================
def get_page_data(driver):
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    # 1/105 같은 형식으로 되어있음 현재 페이지/마지막 페이지를 의미함
    total_pages = soup.find('span', class_='label-page').text
    # 페이지 수 추출
    total_pages = int(total_pages.split(' / ')[-1])



    img_tags = soup.find_all('img', class_='background')

    img_url = [img['src'] for img in img_tags][0]
    base_url = driver.current_url[:-10]
    base_url = base_url + img_url[:-8]

    return total_pages, base_url
######################################################################################
######################################################################################


# ======================================== 각 주차 요일별 수업자료 저장 ========================================
def save_pdfs(driver, total_pages, base_url, week, day):
    # 주차와 일자에 해당하는 디렉토리 생성
    dir_name = f'week_{week}_day_{day}'
    os.makedirs(dir_name, exist_ok=True)    
    for idx in range(1, 1 + total_pages):
        img_num = "{0:0=4d}".format(idx)
        # full_url 구성
        full_url = base_url + img_num + '.jpg'
        
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
######################################################################################
######################################################################################


# ======================================== pdf 병합 ========================================
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

if __name__ == '__main__':
    print(text)