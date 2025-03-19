import tkinter as tk
from tkinter import ttk
from tkinter import Canvas, PhotoImage, Entry, Button
from pathlib import Path
from PIL import Image, ImageTk

class Admin_Users:
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
        self.window.title("Inventory")

        self.canvas = Canvas(self.window, bg="#FFFFFF", height=500, width=700, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)


        # assets_path = Path(r"C:\DoAn\Image\Admin\Inventory")
        assets_path = Path("/home/long/Downloads/doancuoiky-nhom1/Image/Admin/Inventory")


        self.background_img = PhotoImage(file=assets_path / "Background.png")
        self.logout_image = PhotoImage(file=assets_path / "Button_Logout.png")
        self.account_image = PhotoImage(file=assets_path / "Button_Account.png")      
        self.checksales_image = PhotoImage(file=assets_path / "Button_Checksales.png")
        self.inventory_image = PhotoImage(file=assets_path / "Button_Inventory.png")
        self.user_image = PhotoImage(file=assets_path / "Button_Users.png")
        self.hotels_image = PhotoImage(file=assets_path / "Button_Hotels.png")
        self.textbox_image = PhotoImage(file=assets_path / "Textbox.png")
        self.textbox1_image = PhotoImage(file=assets_path / "Textbox_1.png")
        self.update_image = PhotoImage(file=assets_path / "Button_Update.png")
        self.remove_image = PhotoImage(file=assets_path / "Button_Remove.png")
        self.search_image = PhotoImage(file=assets_path / "Button_Search.png")

        self.background = self.canvas.create_image(342.0, 246.0, image=self.background_img)

        self.logout_button = Button(image=self.logout_image, borderwidth=0, highlightthickness=0)
                                    # command=lambda: up.User_Landing_process.log_out_button_handle(self))
        self.logout_button.place(x=544, y=26, width=130, height=40)

        self.account_button = Button(image=self.account_image, borderwidth=0, highlightthickness=0)
                                #    command=lambda: up.User_Landing_process.films_button_handle(self))
        self.account_button.place(x=38, y=28, width=39, height=39)

        self.search_button = Button(image=self.search_image, borderwidth=0, highlightthickness=0)
                                        # command=lambda: up.User_Landing_process.buytickets_button_handle(self))
        self.search_button.place(x=547, y=173, width=119, height=32)

        self.update_button = Button(image=self.update_image, borderwidth=0, highlightthickness=0)
        self.update_button.place(x=38, y=440, width=130, height=40)      

        self.remove_button = Button(image=self.remove_image, borderwidth=0, highlightthickness=0)
        self.remove_button.place(x=186, y=440, width=130, height=40)  

        self.checksales_button = Button(image=self.checksales_image, borderwidth=0, highlightthickness=0)
        self.checksales_button.place(x=24, y=90, width=144, height=48)

        self.inventory_button = Button(image=self.inventory_image, borderwidth=0, highlightthickness=0)
        self.inventory_button.place(x=190, y=90, width=144, height=48)

        self.hotels_button = Button(image=self.hotels_image, borderwidth=0, highlightthickness=0)
        self.hotels_button.place(x=358, y=90, width=144, height=48)

        self.users_button = Button(image=self.user_image, borderwidth=0, highlightthickness=0)
        self.users_button.place(x=524, y=90, width=144, height=48)



        self.entry_bg_1 = self.canvas.create_image(220, 200, image=self.textbox_image)
        self.entry_1 = Entry(bd=0, bg="#F2F5EF", fg="#000716", highlightthickness=0)
        self.entry_1.place(x=140, y=184, width=160, height=32)

        self.entry_bg_2 = self.canvas.create_image(220,245 , image=self.textbox_image)
        self.entry_2 = Entry(bd=0, bg="#F2F5EF", fg="#000716", highlightthickness=0)
        self.entry_2.place(x=140, y=229, width=160, height=32)

        self.entry_bg_3 = self.canvas.create_image(220, 290, image=self.textbox_image)
        self.entry_3 = Entry(bd=0, bg="#F2F5EF", fg="#000716", highlightthickness=0)
        self.entry_3.place(x=140, y=274, width=160, height=32)

        self.entry_bg_4 = self.canvas.create_image(220, 337, image=self.textbox_image)
        self.entry_4 = Entry(bd=0, bg="#F2F5EF", fg="#000716", highlightthickness=0)
        self.entry_4.place(x=140, y=321, width=160, height=32)

        self.entry_bg_5 = self.canvas.create_image(220, 387, image=self.textbox_image)
        self.entry_5 = Entry(bd=0, bg="#F2F5EF", fg="#000716", highlightthickness=0)
        self.entry_5.place(x=140, y=371, width=160, height=32)

        self.entry_bg_6 = self.canvas.create_image(435, 189, image=self.textbox1_image)
        self.entry_6 = Entry(bd=0, bg="#F2F5EF", fg="#000716", highlightthickness=0)
        self.entry_6.place(x=355, y=173, width=160, height=32)

        # Tạo Frame chứa bảng
        self.table_frame = tk.Frame(self.window, bg="#CADBB7")
        self.table_frame.place(x=354,y=215)

        # Tạo Treeview (Bảng)
        self.columns = ("hotel_name", "description", "type_room", "price")
        self.tree = ttk.Treeview(self.table_frame, columns=self.columns, show="headings", height=9)
        self.tree.pack()

        # Thiết lập tiêu đề cột
        self.tree.heading("hotel_name", text="Hotel Name")
        self.tree.heading("description", text="Description")
        self.tree.heading("type_room", text="Type Room")
        self.tree.heading("price", text="Price")

        # Điều chỉnh độ rộng cột (tổng width = 319)
        self.tree.column("hotel_name", width=80)
        self.tree.column("description", width=100)
        self.tree.column("type_room", width=80)
        self.tree.column("price", width=50)
    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = Admin_Users()
    app.run()