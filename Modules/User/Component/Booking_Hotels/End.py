# from tkinter import *
# from pathlib import Path
# import Modules.User.User_Landing_Process as up
import tkinter as tk
from tkinter import Canvas, PhotoImage, Entry, Button
from pathlib import Path
from tkinter import ttk

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
        self.window.title("Bookinghotel")

        self.canvas = Canvas(self.window, bg="#FFFFFF", height=500, width=700, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)


        assets_path = Path(r"C:\DoAn\Image\User\End")

        self.background_img = PhotoImage(file=assets_path / "Background.png")
        self.logout_image = PhotoImage(file=assets_path / "Button_Logout.png")
        self.account_image = PhotoImage(file=assets_path / "Button_Account.png")
        self.quit_image = PhotoImage(file=assets_path / "Button_Quit.png")
        self.printinvoice_image = PhotoImage(file=assets_path / "Button_Printinvoice.png")
        self.background = self.canvas.create_image(342.0, 246.0, image=self.background_img)

        self.logout_button = Button(image=self.logout_image, borderwidth=0, highlightthickness=0)
                                    # command=lambda: up.User_Landing_process.log_out_button_handle(self))
        self.logout_button.place(x=544, y=26, width=130, height=40)

        self.account_button = Button(image=self.account_image, borderwidth=0, highlightthickness=0)
                                #    command=lambda: up.User_Landing_process.films_button_handle(self))
        self.account_button.place(x=38, y=28, width=39, height=39)

        self.addhotel_button = Button(image=self.printinvoice_image, borderwidth=0, highlightthickness=0)
                                        # command=lambda: up.User_Landing_process.buytickets_button_handle(self))
        self.addhotel_button.place(x=96, y=80, width=239, height=48)

        self.checksales_button = Button(image=self.quit_image, borderwidth=0, highlightthickness=0)
        self.checksales_button.place(x=362, y=80, width=239, height=48)


        columns = ("checkin", "checkout", "note", "price")
        # Tạo một Frame chứa bảng, đặt vị trí phù hợp (có thể điều chỉnh toạ độ theo ý bạn)
        table_frame = tk.Frame(self.window)
        table_frame.place(x=12, y=280, width=665, height=100)

        self.table = ttk.Treeview(table_frame, columns=columns, show="headings")
        self.table.heading("checkin", text="Check in")
        self.table.heading("checkout", text="Check out")
        self.table.heading("note", text="Note")
        self.table.heading("price", text="Price")
        # Mỗi cột có độ rộng 165 (165 x 4 = 660)
        self.table.column("checkin", width=165, anchor="center")
        self.table.column("checkout", width=165, anchor="center")
        self.table.column("note", width=165, anchor="center")
        self.table.column("price", width=165, anchor="center")
        self.table.pack(fill="both", expand=True)

        self.invoice_label = tk.Label(self.window, text="Invoice", font=("Inter", 20, "bold"),bg="#FFFFFF", fg="#000000")
        # Đặt Label tại vị trí phù hợp (ví dụ: x=16, y=470)
        self.invoice_label.place(x=12, y=164, width=665,height=66)


        self.entry_1 = Entry(bd=0, bg="#FFFFFF", fg="#000000", highlightthickness=0)
        self.entry_1.place(x=122, y=230, width=222.5, height=50)
        self.customer_label = tk.Label(self.window, text='Customer',font=("Inter", 12, "bold"),bg="#FFFFFF", fg="#000000")
        self.customer_label.place(x=12,y=230,width=110,height=50)

        self.entry_2 = Entry(bd=0, bg="#FFFFFF", fg="#000000", highlightthickness=0)
        self.entry_2.place(x=454.5, y=230, width=222, height=50)
        self.invoiceid_label = tk.Label(self.window, text='Invoice ID',font=("Inter", 12, "bold"),bg="#FFFFFF", fg="#000000")
        self.invoiceid_label.place(x=344.5,y=230,width=110,height=50)

        self.entry_3 = Entry(bd=0, bg="#FFFFFF", fg="#000000", highlightthickness=0)
        self.entry_3.place(x=122, y=380, width=555, height=50)
        self.total_label = tk.Label(self.window, text='Total',font=("Inter", 12, "bold"),bg="#FFFFFF", fg="#000000")
        self.total_label.place(x=12,y=380,width=110,height=50)


        self.window.resizable(0, 0)



    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = Hotel_View()
    app.run()