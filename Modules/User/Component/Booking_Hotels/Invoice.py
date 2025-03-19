# from tkinter import *
# from pathlib import Path
# import Modules.User.User_Landing_Process as up
import tkinter as tk
from tkinter import Canvas, PhotoImage, Entry, Button
from pathlib import Path
from tkinter import ttk


class Invoice_View:
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
        self.window.title("Invoice")

        self.canvas = Canvas(self.window, bg="#FFFFFF", height=500, width=700, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)


        assets_path = Path(r"C:\DoAn\Image\User\Invoice")

        self.background_img = PhotoImage(file=assets_path / "Background.png")
        self.signout_image = PhotoImage(file=assets_path / "Button_Signout.png")
        self.account_image = PhotoImage(file=assets_path / "Button_Account.png")
        self.addtocart_image = PhotoImage(file=assets_path / "Button_Addtocart.png")        
        self.invoice_image = PhotoImage(file=assets_path / "Button_Invoice.png")
        self.process_image = PhotoImage(file=assets_path / "Button_Process.png")
        self.quit_image = PhotoImage(file=assets_path / "Button_Quit.png")
        self.remove_image = PhotoImage(file=assets_path / "Button_Remove.png")
        self.rooms_image = PhotoImage(file=assets_path / "Button_Rooms.png")
        self.textbox1_image = PhotoImage(file=assets_path / "Textbox1.png")
        self.textbox2_image = PhotoImage(file=assets_path / "Textbox2.png")
        self.tabel_image = PhotoImage(file=assets_path / "Table.png")

        self.background = self.canvas.create_image(342.0, 246.0, image=self.background_img)

        self.rooms_button = Button(image=self.rooms_image, borderwidth=0, highlightthickness=0)
                                    # command=lambda: up.User_Landing_process.log_out_button_handle(self))
        self.rooms_button.place(x=59, y=86, width=93, height=34)

        self.account_button = Button(image=self.account_image, borderwidth=0, highlightthickness=0)
                                #    command=lambda: up.User_Landing_process.films_button_handle(self))
        self.account_button.place(x=38, y=28, width=39, height=39)

        self.invoice_button = Button(image=self.invoice_image, borderwidth=0, highlightthickness=0)
                                        # command=lambda: up.User_Landing_process.buytickets_button_handle(self))
        self.invoice_button.place(x=223, y=86, width=93, height=34)

        self.signout_button = Button(image=self.signout_image, borderwidth=0, highlightthickness=0)
        self.signout_button.place(x=387, y=86, width=93, height=34)

        self.quit_button = Button(image=self.quit_image, borderwidth=0, highlightthickness=0)
        self.quit_button.place(x=551, y=86, width=91.22, height=34)

        self.addtocart_button = Button(image=self.addtocart_image, borderwidth=0, highlightthickness=0)
        self.addtocart_button.place(x=435, y=385, width=70.7, height=19.26)

        self.remove_button = Button(image=self.remove_image, borderwidth=0, highlightthickness=0)
        self.remove_button.place(x=520, y=385, width=70.7, height=19.26)

        self.process_button = Button(image=self.process_image, borderwidth=0, highlightthickness=0)
        self.process_button.place(x=350, y=335, width=75.75, height=70.61)      

        self.entry_bg_1 = self.canvas.create_image(520, 185, image=self.textbox1_image)
        self.entry_1 = Entry(bd=0, bg="#E1F2CE", fg="#000716", highlightthickness=0)
        self.entry_1.place(x=450, y=176.5, width=140, height=18.42)

        self.entry_bg_2 = self.canvas.create_image(520, 215, image=self.textbox1_image)
        self.entry_2 = Entry(bd=0, bg="#E1F2CE", fg="#000716", highlightthickness=0)
        self.entry_2.place(x=450, y=206.5, width=140, height=18.42)

        self.entry_bg_3 = self.canvas.create_image(520, 244, image=self.textbox1_image)
        self.entry_3 = Entry(bd=0, bg="#E1F2CE", fg="#000716", highlightthickness=0)
        self.entry_3.place(x=450, y=235.5, width=140, height=18.42)

        self.entry_bg_4 = self.canvas.create_image(520, 272, image=self.textbox1_image)
        self.entry_4 = Entry(bd=0, bg="#E1F2CE", fg="#000716", highlightthickness=0)
        self.entry_4.place(x=450, y=263, width=140, height=18.42)

        self.entry_bg_5 = self.canvas.create_image(560, 342, image=self.textbox2_image)
        self.entry_5 = Entry(bd=0, bg="#E1F2CE", fg="#000716", highlightthickness=0)
        self.entry_5.place(x=522, y=335, width=75, height=16.26)

        self.entry_bg_5 = self.canvas.create_image(560, 369, image=self.textbox2_image)
        self.entry_5 = Entry(bd=0, bg="#E1F2CE", fg="#000716", highlightthickness=0)
        self.entry_5.place(x=522, y=362, width=75, height=16.26)

        self.entry_bg_5 = self.canvas.create_image(520, 423, image=self.textbox1_image)
        self.entry_5 = Entry(bd=0, bg="#E1F2CE", fg="#000716", highlightthickness=0)
        self.entry_5.place(x=450, y=415, width=130, height=16.26)


                # Tạo Frame chứa bảng
        self.table_frame = tk.Frame(self.window, bg="#E1F2CE")
        self.table_frame.place(x=10, y=173)

        # Tạo Treeview (Bảng)
        self.columns = ("name", "checkin", "checkout", "quantity", "price")
        self.tree = ttk.Treeview(self.table_frame, columns=self.columns, show="headings", height=12)
        self.tree.pack()

        # Thiết lập tiêu đề cột
        self.tree.heading("name", text="Name")
        self.tree.heading("checkin", text="Check-in")
        self.tree.heading("checkout", text="Check-out")
        self.tree.heading("quantity", text="Quantity")
        self.tree.heading("price", text="Price")

        # Điều chỉnh độ rộng cột (tổng width = 250)
        self.tree.column("name", width=50)
        self.tree.column("checkin", width=65)
        self.tree.column("checkout", width=65)
        self.tree.column("quantity", width=70)
        self.tree.column("price", width=50)

        self.window.resizable(0, 0)



    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = Invoice_View()
    app.run()