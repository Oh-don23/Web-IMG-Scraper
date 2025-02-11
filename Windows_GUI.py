# 라이브러리 호출
# GUI 라이브러리
from tkinter import *
from tkinter import messagebox
# 웹페이지 여는 라이브러리
import webbrowser
# 절대 경로로 모듈 import 하도록 도와주는 라이브러리
import sys
import os
# 파일의 경로를 절대 경로로 변경
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# 스크래퍼, 다운로더 모듈 호출
from Web_IMG_Scraper.Scripts.Web_SD import Scraper, Downloader

root = Tk()
root.title("Web IMG Scraper")   # 윈도우 창 제목 변경
root.geometry("400x200")    # 가로 * 세로 창 크기 조절
root.resizable(False, False)    # 창 크기 변경 불가

# 간단한 프로그램 설명
MainLable = Label(root, text="웹사이트 이미지 일괄 다운로드 프로그램입니다.\n웹사이트 링크를 아래에 입력 후 저장 버튼을 눌러주세요.")
MainLable.pack()

# 메인 프레임
main_frame = Frame(root, relief="solid", bd=1)
main_frame.pack(fill=X, padx=5)

# 입력창 클릭 시 문구 없애는 함수
def focus_in(event):
    if link.get() == "여기에 링크를 입력하세요":
        link.delete(0, END)
        link.config(fg="black")
# 입력창에서 벗어나면 다시 문구 생성하는 함수
def focus_out(event):
    if link.get() == "":
        link.insert(0, "여기에 링크를 입력하세요")
        link.config(fg="gray")

# 웹사이트 url 입력하는 공간
link = Entry(main_frame, width=48, fg="gray")
link.grid(row=0, column=0, padx=4, pady=18)
link.insert(0, "여기에 링크를 입력하세요")

link.bind("<FocusIn>", focus_in)    # 입력창 클릭 시 실행
link.bind("<FocusOut>", focus_out)  # 입력창에서 벗어나면 실행

# 이미지 저장 버튼 관련 함수
def downloading():
    # url을 제대로 입력하지 않았을 경우 경고 문구 출력
    if link.get() in ["여기에 링크를 입력하세요", ""]:
        messagebox.showerror("오류!", "올바른 url을 입력해주세요.")
    else:
        target_url = link.get()
        Download_btn.config(text="다운로드 중")
        gui_scraper = Scraper(target_url)
        img_links = gui_scraper.find_img_links()
        gui_downloader = Downloader()
        gui_downloader.download_img(img_links)
        gui_scraper.close()
        Download_btn.config(text="다운로드 완료")
# 링크 초기화 관련 함수
def input_reset():
    link.delete(0, END)
    link.config(fg="black")

# 이미지 저장 버튼
Download_btn = Button(main_frame, text="다운로드", width=20, height=2, command=downloading)
Download_btn.grid(row=1, column=0, pady=(0, 10))
# 링크 초기화 버튼
Reset_btn = Button(main_frame, text="reset", command=input_reset)
Reset_btn.grid(row=0, column=1)

# 하단 프레임
bottom_frame = Frame(root, relief="solid", bd=1)
bottom_frame.pack(fill=X, padx=5, pady=(5, 0))

# 하단 프레임 버튼 함수
# 블로그 웹페이지 연결 함수
def open_blog():
    webbrowser.open("https://blog.naver.com/PostList.naver?blogId=oh_don23&from=postList&categoryNo=24")
# 업데이트 웹페이지 연결 함수
def open_github():
    webbrowser.open("https://github.com/Oh-don23/Web_IMG_Scraper")
# 저장된 이미지 폴더 열기
def open_IMG_folder():
    folder_path = os.path.join(os.getcwd(), "images")

    if not os.path.exists(folder_path):
        messagebox.showerror("오류!", "이미지 저장 폴더가 생성되지 않았습니다.")
    else: os.startfile(folder_path)
# 종료 버튼 함수
def close_program():
    root.quit()

btn1 = Button(bottom_frame, width=11, text="제작자 블로그", command=open_blog)
btn1.grid(row=0, column=0, padx=(4, 5))
btn2 = Button(bottom_frame, width=11, text="업데이트 확인", command=open_github)
btn2.grid(row=0, column=1, padx=5)
btn3 = Button(bottom_frame, width=11, text="저장폴더 열기", command=open_IMG_folder)
btn3.grid(row=0, column=2, padx=5)
btn4 = Button(bottom_frame, width=11, text="종료", command=close_program)
btn4.grid(row=0, column=3, padx=5)

bottom_label = Label(root, text="https://github.com/Oh-don23/Web_IMG_Scraper", fg="gray")
bottom_label.pack()

root.mainloop()