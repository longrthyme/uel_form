from tkinter import *
import tkinter as tk
from pathlib import Path

import sys
sys.path.append('c:/DoAn/doancuoiky-nhom1')

import Modules.Signup.Signup_Process as signup_process

class Signup_View:
    def __init__(self):
        self.window = Tk()
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
        self.window.title("Signup")

        self.canvas = Canvas(self.window, bg="#FFFFFF", height=500, width=700, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)

        # assets_path = Path(r"C:\DoAn\doancuoiky-nhom1\Image\Signup")
        assets_path = Path("/home/long/Downloads/doancuoiky-nhom1/Image/Signup")


        self.background_img = PhotoImage(file=assets_path / "Background.png")
        self.login_image = PhotoImage(file=assets_path / "Button_Login.png")
        self.signup_image = PhotoImage(file=assets_path / "Button_Signup.png")
        self.entry_image = PhotoImage(file=assets_path / "Textbox.png")
        self.trendingnow_image = PhotoImage(file=assets_path / "Button_Trendingdestination.png")


        self.background = self.canvas.create_image(342.0, 246.0, image=self.background_img)

        self.login_button = Button(image=self.login_image, borderwidth=0, highlightthickness=0,
                               command=lambda: signup_process.Signup_Process.login_button_handle(self))
        self.login_button.place(x=532, y=25, width=128, height=39)

        self.signup_button = Button(image=self.signup_image, borderwidth=0, highlightthickness=0,
                               command=lambda: signup_process.Signup_Process.signup_button_handle(self))
        self.signup_button.place(x=90, y=360, width=138, height=40)

        self.entry_bg_1 = self.canvas.create_image(160, 181, image=self.entry_image)
        self.entry_1 = Entry(bd=0, bg="#CADBB7", fg="#000716", highlightthickness=0)
        self.entry_1.place(x=60, y=165, width=200, height=33)

        self.entry_bg_2 = self.canvas.create_image(160, 250.5, image=self.entry_image)
        self.entry_2 = Entry(bd=0, bg="#CADBB7", fg="#000716", highlightthickness=0)
        self.entry_2.place(x=60, y=235, width=200, height=33)

        self.entry_bg_3 = self.canvas.create_image(160, 326, image=self.entry_image)
        self.entry_3 = Entry(bd=0, bg="#CADBB7", fg="#000716", highlightthickness=0)
        self.entry_3.place(x=60, y=310, width=200, height=33)

        self.trendingdestination_button = Button(image=self.trendingnow_image, borderwidth=0, highlightthickness=0)
                            #    command=lambda: signup_process.Trendingnow_process.trendingnow(self), relief="flat")
        self.trendingdestination_button.place(x=370.0, y=427.0, width=305, height=44)
        # The 'Trending Now' button displays the movies that are currently trending
       
        # self.signup_button_2 = Button(image=self.signup_image, borderwidth=0, highlightthickness=0)
        #                     #    command=lambda: signup_process.Signup_Process.signup_button_handle(self))
        # self.signup_button_2.place(x=315.0, y=391.0, width=78.0, height=31.0)
        self.window.resizable(0, 0)

class Trendingnow_View:
    def __init__(self):
        self.window = Tk()
        # get screen width and height
        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()

        # set window width and height
        self.window_width = 1080
        self.window_height = 720
        # set window position
        self.window.geometry("%dx%d+%d+%d" % (self.window_width, self.window_height,
                             (self.screen_width - self.window_width) / 2, (self.screen_height - self.window_height) / 2))
        self.window.configure(bg="#FFFFFF")
        self.window.title("TrendingNow")
        self.canvas = Canvas(self.window, bg="#FFFFFF", height=720, width=1080, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)

        assets_path = Path(r"C:\DoAn\Image\TrendingDestination")
        
        self.destination_2 = PhotoImage(file=assets_path / "HaNoi.jpg")
        self.destination_1 = PhotoImage(file=assets_path / "DaLat.jpg")
        self.destination_2 = PhotoImage(file=assets_path / "HaNoi.jpg")
        self.destination_3 = PhotoImage(file=assets_path / "DaNang.jpg")
        self.destination_4 = PhotoImage(file=assets_path / "HoChiMinh.jpg")
        self.destination_5 = PhotoImage(file=assets_path / "VungTau.jpg")


        self.vitri1 = self.canvas.create_image(85.0, 170.0, image=self.destination_1)
        self.vitri2 = self.canvas.create_image(265.0, 170.0, image=self.destination_2)
        self.vitri3 = self.canvas.create_image(445.0, 170.0, image=self.destination_3)
        self.vitri4 = self.canvas.create_image(625.0, 170.0, image=self.destination_4)
        self.vitri5 = self.canvas.create_image(805.0, 170.0, image=self.destination_5)


        self.button1 = Button(image=self.destination_1, borderwidth=0, highlightthickness=0)
                            #    command=lambda: signup_process.Trendingnow_process.phim_button(self))
        self.button1.place(x=0.0, y=0.0, width=170.0, height=340.0)

class Infor_View:
    def __init__(self):
        self.window = Tk()
        # get screen width and height
        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()

        # set window width and height
        self.window_width = 1080
        self.window_height = 720
        # set window position
        self.window.geometry("%dx%d+%d+%d" % (self.window_width, self.window_height,
                             (self.screen_width - self.window_width) / 2, (self.screen_height - self.window_height) / 2))
        self.window.configure(bg="#FFFFFF")
        self.window.title("Information")
        self.canvas = Canvas(self.window, bg="#FFFFFF", height=492, width=685, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)




