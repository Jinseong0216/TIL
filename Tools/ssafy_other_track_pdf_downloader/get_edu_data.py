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
import shutil
from tqdm import tqdm


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
def save_pdfs(driver, total_pages, base_url, track, course_dic, page, order):
    # 디렉토리 생성
    dir_name = f'{track.track}_강의자료'
    os.makedirs(dir_name, exist_ok=True)
    with tqdm(total=total_pages, desc='수업 자료 다운로드 진행', unit='페이지') as pbar:
        for idx in range(1, 1 + total_pages):
            img_num = "{0:0=4d}".format(idx)
            # full_url 구성
            full_url = base_url + img_num + '.jpg'
            
            # 이미지 페이지로 이동
            driver.get(full_url)

            # 스크린샷 캡쳐
            screenshot_path = os.path.join(dir_name, f'{track.track}_{course_dic[page][order-1][1]}_{img_num}.png')
            driver.save_screenshot(screenshot_path)  # 전체 페이지 캡처
            # 진행도 업데이트
            pbar.update(1)
    
    driver.close()  # 현재 탭 닫기
    driver.switch_to.window(driver.window_handles[0])  # 기본 탭으로 돌아가기
    


    # JPG를 PDF로 변환
    jpg_files = [f for f in os.listdir(dir_name) if f.endswith('.png')]
    if jpg_files:
        pdf_path = os.path.join(os.getcwd(), f'{course_dic[page][order-1][1]}.pdf')  # 현재 디렉토리에 PDF 저장
        images = [Image.open(os.path.join(dir_name, f)) for f in jpg_files]
        images[0].save(pdf_path, save_all=True, append_images=images[1:])
        print(f"PDF 파일 저장됨: {pdf_path}")

        # JPG 파일 삭제
        for f in jpg_files:
            os.remove(os.path.join(dir_name, f))

    # 디렉토리 삭제
    shutil.rmtree(dir_name)

    driver.quit()
######################################################################################
######################################################################################


if __name__ == '__main__':
    print(text)