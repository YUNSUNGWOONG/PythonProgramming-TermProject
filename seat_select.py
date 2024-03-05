import tkinter as tk
from PIL import ImageTk, Image
from start_page import *
from tkinter import messagebox

class seat_select(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        # 캔버스 생성
        self.canvas = tk.Canvas(self, width=979, height=680)  # 캔버스 크기 지정
        self.canvas.pack()
        self.canvas.bind("<Button-1>", lambda event: self.canvas_click(event))
        self.show_image("img\좌석선택.png")

        # 이전 프레임에서 전달된 값 가져오기(시작)
        app = self.winfo_toplevel()
        previous_value = app.get_entry_value()
        print("Previous Value: " + previous_value)
        # 이전 프레임에서 전달된 값 가져오기(끝)

        self.username = previous_value

    def canvas_click(self, event):
        app = self.winfo_toplevel()
        # 뒤로가기
        if 20 <= event.x and event.x <= 101 and 23 <= event.y <= 103:
            from start_page import start_page
            app.start_page = start_page(app)
            app.show_frame("start_page")
        # 좌석선택(1-9)
        if 167 <= event.x and event.x <= 264 and 210 <= event.y <= 309:
            self.seat_selected(self.username, '1')
        if 283 <= event.x and event.x <= 379 and 210 <= event.y <= 309:
            self.seat_selected(self.username, '2')
        if 399 <= event.x and event.x <= 496 and 210 <= event.y <= 309:
            self.seat_selected(self.username, '3')
        if 512 <= event.x and event.x <= 609 and 210 <= event.y <= 309:
            self.seat_selected(self.username, '4')
        if 632 <= event.x and event.x <= 729 and 210 <= event.y <= 309:
            self.seat_selected(self.username, '5')
        if 513 <= event.x and event.x <= 610 and 415 <= event.y <= 514:
            self.seat_selected(self.username, '6')
        if 397 <= event.x and event.x <= 493 and 415 <= event.y <= 514:
            self.seat_selected(self.username, '7')
        if 282 <= event.x and event.x <= 380 and 415 <= event.y <= 514:
            self.seat_selected(self.username, '8')
        if 171 <= event.x and event.x <= 268 and 415 <= event.y <= 514:
            self.seat_selected(self.username, '9')

    def seat_selected(self, username, seat):
        selected_seat_info = self.get_selected_seat_info()
        if seat not in selected_seat_info.values():
            if self.is_valid_member:  # 유효한 회원인지 확인
                selected_seat_info[username] = seat
                self.save_selected_seat_info(selected_seat_info)
                messagebox.showinfo("선택 성공", f"{username}님 {seat}번 좌석을 선택하였습니다.")
                # self.update_seat_buttons(selected_seat_info)
            else:
                messagebox.showerror("선택 실패", "좌석을 선택할 수 없습니다. 이용권을 구매해 주세요.")
        else:
            messagebox.showerror("선택 실패", "이미 사용중인 좌석입니다.")

    def is_valid_member(self):
        with open("members_time.txt", "r") as file:
            for line in file:
                member_username, _ = line.strip().split(",")
                if member_username == self.username:
                    return True
        return False

    def get_selected_seat_info(self):
        selected_seat_info = {}
        try:
            with open("selected_seats.txt", "r") as file:
                for line in file:
                    username, seat = line.strip().split(",")
                    selected_seat_info[username] = seat
        except Exception as e:
            messagebox.showerror("Error", str(e))

        return selected_seat_info

    def save_selected_seat_info(self, selected_seat_info):
        try:
            with open("selected_seats.txt", "w") as file:
                for username, seat in selected_seat_info.items():
                    file.write(f"{username},{seat}\n")
        except Exception as e:
            messagebox.showerror("Error", str(e))


    def show_image(self, image_path):
        image = Image.open(image_path)
        resized_image = image.resize((979, 680), Image.Resampling.LANCZOS)
        self.img = ImageTk.PhotoImage(resized_image)
        self.canvas.create_image(0, 0, anchor="nw", image=self.img)

"""
class seat_select(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.label = tk.Label(self, text="seat_select")
        self.label.pack()

        app = self.winfo_toplevel()  # app 변수를 정의
        previous_value = app.get_entry_value()  # 이전 프레임에서 전달된 값 가져오기
        value_label = tk.Label(self, text="Previous Value: " + previous_value)
        value_label.pack()

        previous_button = tk.Button(self, text="Previous", command=self.previous_frame)
        previous_button.pack()

    def previous_frame(self):
        app = self.winfo_toplevel()
        app.show_frame("enter_room")
"""