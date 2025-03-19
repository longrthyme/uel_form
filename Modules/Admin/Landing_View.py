import tkinter as tk
from tkinter import Canvas, PhotoImage, Entry, Button
from pathlib import Path
# import Modules.Admin.Component.Hotels.Hotels_View as hv
import Modules.Admin.Process.Admin_Process as adp

# Giả sử bạn có module xử lý login riêng
# Nếu chưa có, bạn có thể comment lại phần import này
# import Modules.Login.Login_Process as lgp

class Admin_View:
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

        # assets_path = Path(r"C:\DoAn\doancuoiky-nhom1\Image\Admin\LandingPage")

        assets_path = Path("/home/long/Downloads/doancuoiky-nhom1/Image/Admin/LandingPage")

        self.background_img = PhotoImage(file=assets_path / "Background.png")
        self.logout_image = PhotoImage(file=assets_path / "Button_Logout.png")
        self.hotel_image = PhotoImage(file=assets_path / "Button_Hotels.png")
        self.inventory_image = PhotoImage(file=assets_path / "Button_Inventory.png")
        self.sales_image = PhotoImage(file=assets_path / "Button_Sales.png")
        self.users_image = PhotoImage(file=assets_path / "Button_Users.png")

        self.background = self.canvas.create_image(342.0, 246.0, image=self.background_img)

        self.logout_button = Button(image=self.logout_image, borderwidth=0, highlightthickness=0)
                            #    command=lambda: ap.Admin_Process.log_out_button_handle(self))
        self.logout_button.place(x=524, y=26, width=130, height=40)

        self.films_button = Button(image=self.hotel_image, borderwidth=0, highlightthickness=0,
                               command=lambda: adp.Admin_Process.button_handle(self, 'hotel'))
        self.films_button.place(x=47, y=283, width=144, height=48)

        #  self.login_button = Button(image=self.login_image_1, borderwidth=0, highlightthickness=0,
        #                        command=lambda: lgp.Login_Process.confirm_button_handle(self))

        self.inventory_button = Button(image=self.inventory_image, borderwidth=0, highlightthickness=0)
                            #    command=lambda: ap.Admin_Process.inventory_button_handle(self))
        self.inventory_button.place(x=230, y=283, width=146, height=48)

        self.sales_button = Button(image=self.sales_image, borderwidth=0, highlightthickness=0)
                            #    command=lambda: ap.Admin_Process.sales_button_handle(self))
        self.sales_button.place(x=229, y=362.3, width=144, height=48)

        self.users_button = Button(image=self.users_image, borderwidth=0, highlightthickness=0,
                            #    command=lambda: ap.Admin_Process.users_button_handle(self))
                            command=lambda: adp.Admin_Process.button_handle(self, 'user'))
        self.users_button.place(x=47, y=362.3, width=144, height=48)
                           
        self.window.resizable(0, 0)

    def run(self):
        self.window.mainloop()
    
    # @staticmethod
    # def signup_button_handle(self):
    #     self.window.destroy()
    #     app = hv.Hotel_View()
    #     app.window.mainloop()


if __name__ == "__main__":
    app = Admin_View()
    app.run()
