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
        self.window.title("Check Sales")

        self.canvas = Canvas(self.window, bg="#FFFFFF", height=500, width=700, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)


        assets_path = Path(r"C:\DoAn\Image\Admin\Check Sales")

        self.background_img = PhotoImage(file=assets_path / "Background.png")
        self.logout_image = PhotoImage(file=assets_path / "Button_Logout.png")
        self.account_image = PhotoImage(file=assets_path / "Button_Account.png")      
        self.checksales_image = PhotoImage(file=assets_path / "Button_Checksales.png")
        self.inventory_image = PhotoImage(file=assets_path / "Button_Inventory.png")
        self.user_image = PhotoImage(file=assets_path / "Button_Users.png")
        self.hotels_image = PhotoImage(file=assets_path / "Button_Hotels.png")
        self.search_image = PhotoImage(file=assets_path / "Button_Search.png")
        self.textbox_image = PhotoImage(file=assets_path / "Textbox.png")


        self.background = self.canvas.create_image(342.0, 246.0, image=self.background_img)

        self.logout_button = Button(image=self.logout_image, borderwidth=0, highlightthickness=0)
                                    # command=lambda: up.User_Landing_process.log_out_button_handle(self))
        self.logout_button.place(x=544, y=26, width=130, height=40)

        self.account_button = Button(image=self.account_image, borderwidth=0, highlightthickness=0)
                                #    command=lambda: up.User_Landing_process.films_button_handle(self))
        self.account_button.place(x=38, y=28, width=39, height=39)

        self.search_button = Button(image=self.search_image, borderwidth=0, highlightthickness=0)
                                #    command=lambda: up.User_Landing_process.films_button_handle(self))
        self.search_button.place(x=46, y=160, width=89.97, height=41.54)



        self.checksales_button = Button(image=self.checksales_image, borderwidth=0, highlightthickness=0)
        self.checksales_button.place(x=24, y=90, width=144, height=48)

        self.inventory_button = Button(image=self.inventory_image, borderwidth=0, highlightthickness=0)
        self.inventory_button.place(x=190, y=90, width=144, height=48)

        self.hotels_button = Button(image=self.hotels_image, borderwidth=0, highlightthickness=0)
        self.hotels_button.place(x=358, y=90, width=144, height=48)

        self.users_button = Button(image=self.user_image, borderwidth=0, highlightthickness=0)
        self.users_button.place(x=524, y=90, width=144, height=48)

        self.entry_bg_1 = self.canvas.create_image(209, 181, image=self.textbox_image)
        self.entry_1 = Entry(bd=0, bg="#F2F5EF", fg="#000716", highlightthickness=0)
        self.entry_1.place(x=137.5, y=160, width=250, height=41.54)
    

            # Tạo Frame chứa bảng
        self.table_frame = tk.Frame(self.window, bg="#CADBB7")
        self.table_frame.place(x=45, y=232)

        # Tạo Treeview (Bảng)
        self.columns = ("invoice_id", "invoice_date", "hotel", "type_room", "quantity", "price", "total")
        self.tree = ttk.Treeview(self.table_frame, columns=self.columns, show="headings", height=10)
        self.tree.pack()

        # Thiết lập tiêu đề cột
        self.tree.heading("invoice_id", text="Invoice ID")
        self.tree.heading("invoice_date", text="Invoice Date")
        self.tree.heading("hotel", text="Hotel")
        self.tree.heading("type_room", text="Type Room")
        self.tree.heading("quantity", text="Quantity")
        self.tree.heading("price", text="Price")
        self.tree.heading("total", text="Total")

        # Điều chỉnh độ rộng cột (tổng width = 602)
        self.tree.column("invoice_id", width=80)
        self.tree.column("invoice_date", width=100)
        self.tree.column("hotel", width=120)
        self.tree.column("type_room", width=100)
        self.tree.column("quantity", width=60)
        self.tree.column("price", width=60)
        self.tree.column("total", width=80)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = Admin_Users()
    app.run()