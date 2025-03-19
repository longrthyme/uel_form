import tkinter as tk
from tkinter import Canvas, PhotoImage, Entry, Button
from pathlib import Path
import sys
sys.path.append('c:/DoAn/doancuoiky-nhom1')

import Modules.Login.Login_Process as lgp
import Modules.ForgetPassword.Forgetpassword_Process as fgpw
# Giả sử bạn có module xử lý login riêng
# Nếu chưa có, bạn có thể comment lại phần import này


class Login_View:
    def __init__(self):
        self.window = tk.Tk()

        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()

        self.window_width = 693
        self.window_height = 496

        self.window.geometry("%dx%d+%d+%d" % (self.window_width, self.window_height,
                             (self.screen_width - self.window_width) / 2, (self.screen_height - self.window_height) / 2))
        
        self.window.configure(bg="#FFFFFF")
        self.window.title("Login")

        self.canvas = Canvas(self.window, bg="#FFFFFF", height=500, width=700, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)

        # assets_path = Path(r"\Image\Login")
        assets_path = Path("/home/long/Downloads/doancuoiky-nhom1/Image/Login")

        self.background_img = PhotoImage(file=assets_path / "Background.png")
        self.login_image_1 = PhotoImage(file=assets_path / "Button_Login.png")
        self.signup_image = PhotoImage(file=assets_path / "Button_Signup.png")
        self.entry_image_1 = PhotoImage(file=assets_path / "Textbox1.png")
        self.entry_image_2 = PhotoImage(file=assets_path / "Textbox2.png")
        self.forgetpw_image = PhotoImage(file=assets_path / "Button_Forget_pw.png")

        self.background = self.canvas.create_image(342.0, 246.0, image=self.background_img)

        self.login_button = Button(image=self.login_image_1, borderwidth=0, highlightthickness=0,
                               command=lambda: lgp.Login_Process.confirm_button_handle(self))
        self.login_button.place(x=96, y=310, width=141, height=39)

        self.signup_button = Button(image=self.signup_image, borderwidth=0, highlightthickness=0,
                               command=lambda: lgp.Login_Process.signup_button_handle(self))
        self.signup_button.place(x=532, y=25, width=134, height=46.53)

        self.entry_bg_1 = self.canvas.create_image(160, 205, image=self.entry_image_1)
        self.entry_1 = Entry(bd=0, bg="#CADBB7", fg="#000716", highlightthickness=0)
        self.entry_1.place(x=60, y=189, width=200, height=33)

        self.entry_bg_2 = self.canvas.create_image(160, 279, image=self.entry_image_2)
        self.entry_2 = Entry(bd=0, bg="#CADBB7", fg="#000716", highlightthickness=0)
        self.entry_2.place(x=60, y=262, width=200, height=33)

        self.forgetps_button = Button(image=self.forgetpw_image, borderwidth=0, highlightthickness=0)
                                    #   command=lambda: fgpw.Forgetpassword_Process.signup_button_handle(self))
        self.forgetps_button.place(x=80, y=360, width=168, height=25)
                           
        self.window.resizable(0, 0)


