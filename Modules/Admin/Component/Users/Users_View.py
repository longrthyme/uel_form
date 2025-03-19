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
        self.window.title("Users")

        self.canvas = Canvas(self.window, bg="#FFFFFF", height=500, width=700, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)


        assets_path = Path(r"C:\DoAn\Image\Admin\Users")

        self.background_img = PhotoImage(file=assets_path / "Background.png")
        self.logout_image = PhotoImage(file=assets_path / "Button_Logout.png")
        self.account_image = PhotoImage(file=assets_path / "Button_Account.png")
        self.delete_image = PhotoImage(file=assets_path / "Button_Delete.png")        
        self.checksales_image = PhotoImage(file=assets_path / "Button_Checksales.png")
        self.inventory_image = PhotoImage(file=assets_path / "Button_Inventory.png")
        self.update_image = PhotoImage(file=assets_path / "Button_Update.png")
        self.user_image = PhotoImage(file=assets_path / "Button_User.png")
        self.hotels_image = PhotoImage(file=assets_path / "Button_Hotels.png")
        self.textbox_image = PhotoImage(file=assets_path / "Textbox.png")
        self.createnew_image = PhotoImage(file=assets_path / "Button_Createnewuser.png")
        self.plaintextbox_image = PhotoImage(file=assets_path / "PlainTextbox.png")
        self.background = self.canvas.create_image(342.0, 246.0, image=self.background_img)

        self.logout_button = Button(image=self.logout_image, borderwidth=0, highlightthickness=0)
                                    # command=lambda: up.User_Landing_process.log_out_button_handle(self))
        self.logout_button.place(x=544, y=26, width=130, height=40)

        self.account_button = Button(image=self.account_image, borderwidth=0, highlightthickness=0)
                                #    command=lambda: up.User_Landing_process.films_button_handle(self))
        self.account_button.place(x=38, y=28, width=39, height=39)

        self.update_button = Button(image=self.update_image, borderwidth=0, highlightthickness=0)
                                        # command=lambda: up.User_Landing_process.buytickets_button_handle(self))
        self.update_button.place(x=67, y=360, width=56, height=24)

        self.delete_button = Button(image=self.delete_image, borderwidth=0, highlightthickness=0)
        self.delete_button.place(x=136, y=360, width=63, height=24)      

        self.createnew_button = Button(image=self.createnew_image, borderwidth=0, highlightthickness=0)
        self.createnew_button.place(x=204, y=360, width=113, height=24)  

        self.checksales_button = Button(image=self.checksales_image, borderwidth=0, highlightthickness=0)
        self.checksales_button.place(x=24, y=90, width=144, height=48)

        self.inventory_button = Button(image=self.inventory_image, borderwidth=0, highlightthickness=0)
        self.inventory_button.place(x=190, y=90, width=144, height=48)

        self.hotels_button = Button(image=self.hotels_image, borderwidth=0, highlightthickness=0)
        self.hotels_button.place(x=358, y=90, width=144, height=48)

        self.users_button = Button(image=self.user_image, borderwidth=0, highlightthickness=0)
        self.users_button.place(x=524, y=90, width=144, height=48)

        self.entry_bg_1 = self.canvas.create_image(235, 223, image=self.textbox_image)
        self.entry_1 = Entry(bd=0, bg="#CADBB7", fg="#000716", highlightthickness=0)
        self.entry_1.place(x=177, y=209, width=116.5, height=28)

        self.entry_bg_2 = self.canvas.create_image(235,263 , image=self.textbox_image)
        self.entry_2 = Entry(bd=0, bg="#CADBB7", fg="#000716", highlightthickness=0)
        self.entry_2.place(x=177, y=249, width=116.5, height=28)

        self.entry_bg_3 = self.canvas.create_image(235, 303, image=self.textbox_image)
        self.entry_3 = Entry(bd=0, bg="#CADBB7", fg="#000716", highlightthickness=0)
        self.entry_3.place(x=177, y=289, width=116.5, height=28)

        self.background_image = Image.open("C:/DoAn/Image/Admin/Users/PlainTextbox.png")  # Thay thế với đường dẫn ảnh của bạn
        self.background_image = self.background_image.resize((20, 244))  # Điều chỉnh kích thước ảnh cho khung
        self.background_photo = ImageTk.PhotoImage(self.background_image)


        
        self.formframe2 = tk.Frame(self.window, bg='pink')
        self.formframe2.place(x=359, y=198, width=300, height=244)


        self.background_label = tk.Label(self.formframe2, image=self.background_photo)

        self.bottom_frame = tk.Frame(self.window, bg="#D9E7C5", height=20)
        self.bottom_frame.pack(fill="x", side="bottom", padx=20, pady=20)
        self.tree = ttk.Treeview(self.formframe2, columns=("STT", "Username", "Password", "Roles"), show="headings")
        self.tree.heading("STT", text="STT")
        self.tree.heading("Username", text="Username")
        self.tree.heading("Password", text="Password")
        self.tree.heading("Roles", text="Roles")

        self.tree.column("STT", width=20)
        self.tree.column("Username", width=100)
        self.tree.column("Password", width=100)
        self.tree.column("Roles", width=80)

        self.tree.pack(fill="both", expand=True)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = Admin_Users()
    app.run()