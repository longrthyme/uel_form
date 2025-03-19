# from tkinter import *
# from pathlib import Path
# import Modules.User.User_Landing_Process as up
import tkinter as tk
from tkinter import Canvas, PhotoImage, Entry, Button
from pathlib import Path
import Modules.Admin.Process.Admin_Process as adp


class Hotel_View:
    def __init__(self):
        self.window = tk.Tk()
        # get screen width and height
        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()

        # set window width and height
        self.window_width = 693
        self.window_height = 496
        # set window position
        self.window.geometry("%dx%d+%d+%d" % (self.window_width, self.window_height,
                             (self.screen_width - self.window_width) / 2, (self.screen_height - self.window_height) / 2))
        self.window.configure(bg="#FFFFFF")
        self.window.title("Hotels")

        self.canvas = Canvas(self.window, bg="#FFFFFF", height=500, width=700, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)


        # assets_path = Path(r"C:\DoAn\Image\Admin\Hotels")
        assets_path = Path("/home/long/Downloads/doancuoiky-nhom1/Image/Admin/Hotels")


        self.background_img = PhotoImage(file=assets_path / "Background.png")
        self.logout_image = PhotoImage(file=assets_path / "Button_Logout.png")
        self.account_image = PhotoImage(file=assets_path / "Button_Account.png")
        self.addhotel_image = PhotoImage(file=assets_path / "Button_Addhotel.png")        
        self.checksales_image = PhotoImage(file=assets_path / "Button_Checksales.png")
        self.inventory_image = PhotoImage(file=assets_path / "Button_Inventory.png")
        self.remove_image = PhotoImage(file=assets_path / "Button_Remove.png")
        self.user_image = PhotoImage(file=assets_path / "Button_User.png")
        self.hotels_image = PhotoImage(file=assets_path / "Button_Hotels.png")
        self.textbox_image = PhotoImage(file=assets_path / "TextBox.png")

        self.background = self.canvas.create_image(342.0, 246.0, image=self.background_img)

        self.logout_button = Button(image=self.logout_image, borderwidth=0, highlightthickness=0)
                                    # command=lambda: up.User_Landing_process.log_out_button_handle(self))
        self.logout_button.place(x=544, y=26, width=130, height=40)

        self.account_button = Button(image=self.account_image, borderwidth=0, highlightthickness=0)
                                #    command=lambda: up.User_Landing_process.films_button_handle(self))
        self.account_button.place(x=38, y=28, width=39, height=39)

        self.addhotel_button = Button(image=self.addhotel_image, borderwidth=0, highlightthickness=0,
                                        # command=lambda: up.User_Landing_process.buytickets_button_handle(self))
                                        command=lambda: adp.Admin_Process.hotel_button_handle(self))
        self.addhotel_button.place(x=213, y=417, width=93, height=34)

        self.checksales_button = Button(image=self.checksales_image, borderwidth=0, highlightthickness=0)
        self.checksales_button.place(x=24, y=90, width=144, height=48)

        self.inventory_button = Button(image=self.inventory_image, borderwidth=0, highlightthickness=0)
        self.inventory_button.place(x=190, y=90, width=144, height=48)

        self.hotels_button = Button(image=self.hotels_image, borderwidth=0, highlightthickness=0)
        self.hotels_button.place(x=358, y=90, width=144, height=48)

        self.users_button = Button(image=self.user_image, borderwidth=0, highlightthickness=0)
        self.users_button.place(x=524, y=90, width=144, height=48)

        self.remove_button = Button(image=self.remove_image, borderwidth=0, highlightthickness=0,
                                                                        command=lambda: adp.Admin_Process.clear_all_fields(self))

        self.remove_button.place(x=372, y=417, width=93, height=34)      

        self.entry_bg_1 = self.canvas.create_image(380, 240, image=self.textbox_image)
        self.entry_1 = Entry(bd=0, bg="#CADBB7", fg="#000716", highlightthickness=0)
        self.entry_1.place(x=270, y=226, width=210, height=28)

        self.entry_bg_2 = self.canvas.create_image(380, 276, image=self.textbox_image)
        self.entry_2 = Entry(bd=0, bg="#CADBB7", fg="#000716", highlightthickness=0)
        self.entry_2.place(x=270, y=262, width=210, height=28)

        self.entry_bg_3 = self.canvas.create_image(380, 312, image=self.textbox_image)
        self.entry_3 = Entry(bd=0, bg="#CADBB7", fg="#000716", highlightthickness=0)
        self.entry_3.place(x=270, y=298, width=210, height=28)

        self.entry_bg_4 = self.canvas.create_image(380, 348, image=self.textbox_image)
        self.entry_4 = Entry(bd=0, bg="#CADBB7", fg="#000716", highlightthickness=0)
        self.entry_4.place(x=270, y=334, width=210, height=28)

        self.entry_bg_5 = self.canvas.create_image(380, 384, image=self.textbox_image)
        self.entry_5 = Entry(bd=0, bg="#CADBB7", fg="#000716", highlightthickness=0)
        self.entry_5.place(x=270, y=370, width=210, height=28)


        self.window.resizable(0, 0)



    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = Hotel_View()
    app.run()