import tkinter as tk
from tkinter import Canvas, PhotoImage, Entry, Button
from pathlib import Path

# Giả sử bạn có module xử lý login riêng
# Nếu chưa có, bạn có thể comment lại phần import này
# import Modules.Login.Login_Process as lgp

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
        # self.window.title("Forget Password")

        self.canvas = Canvas(self.window, bg="#FFFFFF", height=500, width=700, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)

        assets_path = Path(r"C:\DoAn\Image\ForgetPassword")

        self.background_img = PhotoImage(file=assets_path / "Background.png")
        self.reset_pw_image = PhotoImage(file=assets_path / "Button_Resetpassword.png")
        self.entry_image = PhotoImage(file=assets_path / "Textbox.png")
        self.login_image = PhotoImage(file=assets_path / "Button_Login.png")
        self.signup_image = PhotoImage(file=assets_path / "Button_Signup.png")

        self.background = self.canvas.create_image(342.0, 246.0, image=self.background_img)


        self.entry_bg_1 = self.canvas.create_image(360, 150, image=self.entry_image)
        self.entry_1 = Entry(bd=0, bg="#FBFBFB", fg="#000716", highlightthickness=0)
        self.entry_1.place(x=256, y=131, width=207, height=39)

        self.entry_bg_2 = self.canvas.create_image(360, 218, image=self.entry_image)
        self.entry_2 = Entry(bd=0, bg="#FBFBFB", fg="#000716", highlightthickness=0)
        self.entry_2.place(x=256, y=199, width=207, height=39)

        self.entry_bg_3 = self.canvas.create_image(360, 286, image=self.entry_image)
        self.entry_3 = Entry(bd=0, bg="#FBFBFB", fg="#000716", highlightthickness=0)
        self.entry_3.place(x=256, y=267, width=207, height=39)

        self.entry_bg_4 = self.canvas.create_image(360, 356, image=self.entry_image)
        self.entry_4 = Entry(bd=0, bg="#FBFBFB", fg="#000716", highlightthickness=0)
        self.entry_4.place(x=256, y=337, width=207, height=39)

        self.login_button = Button(image=self.login_image, borderwidth=0, highlightthickness=0)
        self.login_button.place(x=532, y=25, width=129.5, height=39.5)

        self.login_button = Button(image=self.signup_image, borderwidth=0, highlightthickness=0)
        self.login_button.place(x=529.3, y=73, width=133.5, height=47)

        self.reset_ps_button = Button(image=self.reset_pw_image, borderwidth=0, highlightthickness=0)
        self.reset_ps_button.place(x=273, y=400, width=174, height=39)

        self.window.resizable(0, 0)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = Login_View()
    app.run()
