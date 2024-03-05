import tkinter as tk
from start_page import *
from datetime import datetime, timedelta
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

class user_state(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.option_add('*Font', '나눔스퀘어 19 bold')

        # 캔버스 생성
        self.canvas = tk.Canvas(self, width=979, height=680)  # 캔버스 크기 지정
        self.canvas.pack()
        self.canvas.bind("<Button-1>", lambda event: self.canvas_click(event))
        self.show_image("img\이용현황_1.png")

        # 이전 프레임에서 전달된 값 가져오기(시작)
        app = self.winfo_toplevel()
        self.username = app.get_entry_value()
        print("user_id: " + self.username)
        # 이전 프레임에서 전달된 값 가져오기(끝)



        with open("members_time.txt", "r") as file:
            for line in file:
                stored_username,stored_lefttime = line.split(",")
                if self.username == stored_username:
                    formatted_datetime = datetime.strptime(stored_lefttime.strip(), "%Y-%m-%d %H:%M:%S").strftime(
                        "%Y년 %m월 %d일 %H시 %M분")
                    self.label = tk.Label(self, text=f"{formatted_datetime}", bg="#2d2c2e", fg="#FECF95")
                    self.canvas.create_window(608, 328, anchor=tk.CENTER, window=self.label)
                    #self.label.configure(bg=self.cget("bg"))

                    break




    def is_valid_member(self):
        with open("members_time.txt", "r") as file:
            for line in file:
                member_username, _ = line.strip().split(",")
                if member_username == self.username:
                    return True
        return False

    def extend_time(self,hour):
        with open("members_time.txt", 'r') as file:
            lines = file.readlines()

        for i in range(len(lines)):
            username, expiration_date = lines[i].strip().split(',')
            # 현재 로그인한 회원의 정보만 변경
            if username == self.username:
                # 문자열 데이터를 datetime 데이터로 변환
                expiration_datetime = datetime.strptime(expiration_date, '%Y-%m-%d %H:%M:%S')
                # hour만큼 연장
                new_expiration_datetime = expiration_datetime + timedelta(hours=hour)
                # 업데이트된 정보를 문자열로 변경하여 리스트에 저장
                lines[i] = f"{username},{new_expiration_datetime.strftime('%Y-%m-%d %H:%M:%S')}\n"

        # 파일 업데이트
        with open("members_time.txt", 'w') as file:
            file.writelines(lines)

    def canvas_click(self, event):
        print("Canvas clicked at x=", event.x, ", y=", event.y)
        app = self.winfo_toplevel()
        # 뒤로가기
        if 20 <= event.x and event.x <= 101 and 23 <= event.y <= 103:
            from start_page import start_page
            app.start_page = start_page(app)
            app.show_frame("start_page")
        # 시간선택
        if 100 <= event.x and event.x <= 340 and 452 <= event.y <= 537:
            if self.is_valid_member():
                answer = messagebox.askyesno("질문", "1시간을 연장하시겠습니까?")
                if answer:
                    self.extend_time(1)
                    messagebox.showinfo('시간연장', '연장 완료되었습니다.')
                    answer2 = messagebox.askyesno("질문", "자리선택을 하시겠습니까?")
                    if answer2:
                        from seat_select import seat_select
                        app.set_entry_value(self.username)
                        app.seat_select = seat_select(app)
                        app.show_frame("seat_select")
                    else:
                        from start_page import start_page
                        app.start_page = start_page(app)
                        app.show_frame("start_page")
            else:
                messagebox.showerror("연장 실패", "이용권이 없는 회원입니다. 이용권을 등록하세요.")

        if 367 <= event.x and event.x <= 606 and 452 <= event.y <= 537:
            if self.is_valid_member():
                answer = messagebox.askyesno("질문", "3시간을 연장하시겠습니까?")
                if answer:
                    self.extend_time(3)
                    messagebox.showinfo('시간연장', '연장 완료되었습니다.')
                    answer2 = messagebox.askyesno("질문", "자리선택을 하시겠습니까?")
                    if answer2:
                        from seat_select import seat_select
                        app.seat_select = seat_select(app)
                        app.show_frame("seat_select")
                    else:
                        from start_page import start_page
                        app.start_page = start_page(app)
                        app.show_frame("start_page")
            else:
                messagebox.showerror("연장 실패", "이용권이 없는 회원입니다. 이용권을 등록하세요.")


        if 627 <= event.x and event.x <= 867 and 452 <= event.y <= 537:
            if self.is_valid_member():
                answer = messagebox.askyesno("질문", "7시간을 연장하시겠습니까?")
                if answer:
                    self.extend_time(7)
                    messagebox.showinfo('시간연장', '연장 완료되었습니다.')
                    answer2 = messagebox.askyesno("질문", "자리선택을 하시겠습니까?")
                    if answer2:
                        from seat_select import seat_select
                        app.seat_select = seat_select(app)
                        app.show_frame("seat_select")
                    else:
                        from start_page import start_page
                        app.start_page = start_page(app)
                        app.show_frame("start_page")
            else:
                messagebox.showerror("연장 실패", "이용권이 없는 회원입니다. 이용권을 등록하세요.")

    """"""
    def show_image(self, image_path):
        image = Image.open(image_path)
        resized_image = image.resize((979, 680), Image.Resampling.LANCZOS)
        self.img = ImageTk.PhotoImage(resized_image)
        self.canvas.create_image(0, 0, anchor="nw", image=self.img)
        """
        self.text_color = (255, 255, 255)  # 텍스트 색상 (흰색)
        self.font_size = 24  # 폰트 크기
        self.font = ImageFont.truetype('arial.ttf', self.font_size)

        draw = ImageDraw.Draw(image)
        draw.text((300, 300), self.get_due_date(), fill=self.text_color, font=self.font)
        """
    """    
    def get_due_date(self):
        with open("members_time.txt", "r") as file:
            for line in file:
                member_username, due_date = line.strip().split(",")
                if member_username == self.username:
                    return due_date
    """
