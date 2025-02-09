# 라이브러리 호출
# GUI 라이브러리
from tkinter import *
# 절대 경로로 모듈 import 하도록 도와주는 라이브러리
import sys
import os
# 파일의 경로를 절대 경로로 변경
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# 스크래퍼, 다운로더 모듈 호출
from Web_IMG_Scraper.Scripts.Web_SD import Scraper, Downloader

root = Tk()
root.title("Web IMG Scraper")   # 윈도우 창 제목 변경
root.geometry("640x480")    # 가로 * 세로 창 크기 조절
root.resizable(False, False)    # 창 크기 변경 불가

# 이미지 링크 삽입하는 공간
MainLable = Label(root, text="Link")
MainLable.pack()

link = Entry(root, width=50)
link.pack()
link.insert(0, "링크를 입력하세요")

def downloading():
    target_url = link.get()
    Download_btn.config(text="다운로드 중")
    gui_scraper = Scraper(target_url)
    img_links = gui_scraper.find_img_links()
    gui_downloader = Downloader()
    gui_downloader.download_img(img_links)
    gui_scraper.close()
    Download_btn.config(text="다운로드 완료")

Download_btn = Button(root, text="Download", command=downloading)
Download_btn.pack()


root.mainloop()