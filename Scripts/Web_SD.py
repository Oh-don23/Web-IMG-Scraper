# 라이브러리 호출
# 웹 스크래핑을 위한 라이브러리
from selenium import webdriver
# 정규표현식(문자열에서 특정 패턴 검색 및 추출 등)을 처리하기 위한 라이브러리
import re
# 컴퓨터 운영체제와의 상호작용을 위한 라이브러리
import os
# HTTP 요청을 간편하게 처리할 수 있는 라이브러리
import requests
# 요청 간 지연시간 추가를 위한 라이브러리
import time

# 클래스, 함수
# 이미지 링크를 얻기 위한 스크래핑 클래스
class Scraper:
    # 변수 url 초기화, 웹드라이버 한 번만 실행
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome()

    # 페이지 열고 html에서 원하는 텍스트 추출 후 전처리
    def find_img_links(self):
        self.driver.get(self.url)
        html = self.driver.page_source
        img_urls = re.findall(r'<img[^>]+src=["\'](https?://[^"\']+)["\']', html)
        return img_urls
    
    # 웹드라이버 종료
    def close(self):
        self.driver.quit()

# 이미지를 다운로드하기 위한 클래스
class Downloader:
    # 변수 초기화 후 만약 폴더가 존재하지 않으면 생성
    def __init__(self, save_folder="images"):
        self.save_folder = save_folder
        if not os.path.exists(self.save_folder):
            os.makedirs(self.save_folder)
    # 추출한 url로 이미지 다운로드
    def download_img(self, img_urls):
        # 파일명에 순서대로 번호 붙이기
        for i, download_link in enumerate(img_urls, start=1):
            try:
                response = requests.get(download_link, timeout=10)  # 10초 타임아웃

                file_name = f"{i}_{os.path.basename(download_link) or f'{i}_image.jpg'}"
                file_path = os.path.join(self.save_folder, file_name)

                with open(file_path, 'wb') as file:
                    file.write(response.content)

                time.sleep(0.5)   # 각 요청 사이에 0.5초 지연(서버 과부하 방지)
                print(f"파일 {i} ({file_name}) 저장 완료")

            # 예외처리
            except requests.exceptions.RequestException as e:
                print(f"파일 {i} 네트워크 문제로 다운로드 오류: {e}")
            except IOError as e:
                print(f"파일 {i} 저장 오류: {e}")
            except Exception as e:
                print (f"파일 {i} 예기치 않은 오류 발생: {e}")
        
        # 파일 다운로드가 다 끝나면 완료 메시지 띄우기
        print("모든 이미지 다운로드 완료!")