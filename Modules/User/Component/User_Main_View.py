import tkinter as tk
from tkinter import ttk
from pathlib import Path
from tkinter import *
from tkinter import Spinbox
# from PIL import Image, ImageTk
class HotelBookingApp:
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
        self.window.title("BookingHotels")

        self.canvas = Canvas(self.window, bg="#FFFFFF", height=500, width=700, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)

        assets_path = Path(r"C:\DoAn\doancuoiky-nhom1\Image\User\Booking_Hotels")

        self.background_img = PhotoImage(file=assets_path / "Background.png")
        self.account_image = PhotoImage(file=assets_path / "Button_Account.png")
        self.check_image = PhotoImage(file=assets_path / "Button_Check.png")
        self.entry_image_1 = PhotoImage(file=assets_path / "Textbox.png")
        self.entry_image_2 = PhotoImage(file=assets_path / "Textbox_dropdown.png")
        self.homepage_image = PhotoImage(file=assets_path / "Button_HomePage.png")
        self.logout_image = PhotoImage(file=assets_path / "Button_Logout.png")


        self.background = self.canvas.create_image(342.0, 246.0, image=self.background_img)

        self.account_button = Button(image=self.account_image, borderwidth=0, highlightthickness=0)
                            #    command=lambda: signup_process.Signup_Process.login_button_handle(self))
        self.account_button.place(x=76, y=16, width=39, height=39)

        self.check_button = Button(image=self.check_image, borderwidth=0, highlightthickness=0,relief="flat")
        self.check_button.place(x=536, y=437, width=130.4, height=32.8)

        self.homepage_button = Button(image=self.homepage_image,borderwidth=0,highlightthickness=0)
        self.homepage_button.place(x=37.3,y=70.1,width=130.4,height=32.8)

        self.logout_button = Button(image=self.logout_image,borderwidth=0,highlightthickness=0)
        self.logout_button.place(x=563,y=26,width=103.28,height=32.8)

        self.entry_bg_1 = self.canvas.create_image(180, 186, image=self.entry_image_1)
        # self.entry_1 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        # self.entry_1.place(x=97, y=185, width=180, height=47)

        self.entry_bg_2 = self.canvas.create_image(500, 186, image=self.entry_image_2)
        # self.entry_2 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        # self.entry_2.place(x=405, y=163.2, width=180, height=47)
        

        self.entry_bg_3 = self.canvas.create_image(180, 270, image=self.entry_image_2)

        self.entry_bg_4 = self.canvas.create_image(500, 270, image=self.entry_image_2)
        # self.entry_3 = Entry(bd=0, bg="pink", fg="#000716",font=("Inter"), highlightthickness=0)
        # self.entry_3.place(x=77, y=285, width=70, height=47)

        self.city_combobox = ttk.Combobox(self.window,values=["Vũng Tàu", "Đà Nẵng", "Phú Yên", "Hà Nội", "Hồ Chí Minh", "Đà Lạt"],state="readonly",font=("Inter",14))
        self.city_combobox.set("")  # Giá trị mặc định
        self.city_combobox.place(x=97,y=163,width=180,height=47)


        # self.combo_frame = tk.Frame(self.window, bg="#D9E7C5")
        # self.combo_frame.place(x=77, y=255,width=237,height=47)
               # Tạo Combobox 1
        self.combobox1 = ttk.Combobox( values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
, state="readonly",font=("Inter",10))
        self.combobox1.set("Date")  # Giá trị mặc định
        self.combobox1.place(x=77, y=247, width=60,height=47)  # Vị trí của Combobox 1

        # Tạo Combobox 2
        self.combobox2 = ttk.Combobox( values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],font=("Inter",10),state="readonly")
        self.combobox2.set("Month")  # Giá trị mặc định
        self.combobox2.place(x=137, y=247, width=60,height=47)  # Vị trí của Combobox 2

        # Tạo Combobox 3
        self.combobox3 = ttk.Combobox( values=[2025,2026,2027,2028], state="readonly",font=("Inter",10))
        self.combobox3.set("Year")  # Giá trị mặc định
        self.combobox3.place(x=197, y=247, width=80,height=47)  # Vị trí của Combobox 3


               # Tạo Combobox 1
        self.combobox1 = ttk.Combobox( values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
, state="readonly",font=("Inter",10))
        self.combobox1.set("Date")  # Giá trị mặc định
        self.combobox1.place(x=400, y=247, width=60,height=47)  # Vị trí của Combobox 1

        # Tạo Combobox 2
        self.combobox2 = ttk.Combobox( values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],font=("Inter",10),state="readonly")
        self.combobox2.set("Month")  # Giá trị mặc định
        self.combobox2.place(x=460, y=247, width=60,height=47)  # Vị trí của Combobox 2

        # Tạo Combobox 3
        self.combobox3 = ttk.Combobox( values=[2025,2026,2027,2028], state="readonly",font=("Inter",10))
        self.combobox3.set("Year")  # Giá trị mặc định
        self.combobox3.place(x=520, y=247, width=80,height=47)  # Vị trí của Combobox 3

        #Tạo combobox cho "Guest & Rooms"
        # self.adults_var = tk.StringVar(value="Adults")
        self.adult_spinbox = Spinbox(self.window,  values=["Adults", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"], state="readonly", font=("Inter",14), bg="#FFFFFF",command=self.check_spinbox_values)
        # self.guest_room_combobox.set("")  # Giá trị mặc định
        self.adult_spinbox.place(x=400, y=163, width=100, height=47)
        self.adult_spinbox.bind("<ButtonRelease-1>", lambda event: self.check_spinbox_values())


        # self.children_var = tk.StringVar(value="Children")
        self.children_spinbox = Spinbox(self.window,  values=["Children", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"], state="readonly", font=("Inter",14), bg="#FFFFFF",command=self.check_spinbox_values)
        # self.guest_room_combobox.set("")  # Giá trị mặc định
        self.children_spinbox.place(x=500, y=163, width=100, height=47)

        self.children_spinbox.bind("<ButtonRelease-1>", lambda event: self.check_spinbox_values())
        #Khi người dùng chọn "Adults & Rooms" từ Combobox, sẽ hiển thị các Spinbox
        # self.adults_var.trace_add("write", self.show_spinboxes)
        # self.children_var.trace_add("write", self.show_spinboxes)
        # Các Spinbox cho Người lớn, Trẻ em, Phòng
        self.single_label = tk.Label(self.window, text="Single Room", font=("Inter", 14), bg="#CADBB7")
        self.couple_label = tk.Label(self.window, text="Couple Room", font=("Inter", 14), bg="#CADBB7")
        self.family_label = tk.Label(self.window, text="Family Room", font=("Inter", 14), bg="#CADBB7")
        self.single_spinbox = Spinbox(self.window,  values=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], font=("Inter", 14))

        self.couple_spinbox = Spinbox(self.window, from_=0, to=5, width=10, font=("Inter", 14))
        self.family_spinbox = Spinbox(self.window, from_=0, to=4, width=10, font=("Inter", 14))

        # Bắt đầu vòng lặp kiểm tra dữ liệu định kỳ
        self.check_spinbox_values()
    
    def check_spinbox_values(self):
        # Lấy giá trị trực tiếp từ Spinbox
        adult_val = self.adult_spinbox.get()
        children_val = self.children_spinbox.get()
        print("Adults:", adult_val, "Children:", children_val)  # Debug
        
        # Kiểm tra nếu cả hai giá trị là số, tiến hành hiển thị widget phụ theo điều kiện
        if adult_val.isdigit() and children_val.isdigit():
            adult_num = int(adult_val)
            children_num = int(children_val)
            # Giả sử: nếu chỉ có 1 người lớn và 0 trẻ, chỉ hiển thị Single
            if adult_num == 1 and children_num == 0:
                self.single_label.place(x=170, y=305)
                self.single_spinbox.place(x=290, y=305, width=150, height=27)
                self.couple_label.place_forget()
                self.couple_spinbox.place_forget()
                self.family_label.place_forget()
                self.family_spinbox.place_forget()
            # Nếu có từ 2 trở lên người lớn, hiển thị Single và Couple
            elif 3>adult_num >= 2 and  children_num==0 :
                self.single_label.place(x=170, y=305)
                self.single_spinbox.place(x=300, y=305, width=150, height=27)
                self.couple_label.place(x=170, y=345)
                self.couple_spinbox.place(x=300, y=345, width=150, height=27)
                self.family_label.place_forget()
                self.family_spinbox.place_forget()
            # Các trường hợp còn lại, hiển thị cả 3
            elif (adult_num >2 and children_num >=0):
                self.single_label.place(x=170, y=305)
                self.single_spinbox.place(x=300, y=305, width=150, height=27)
                self.couple_label.place(x=170, y=345)
                self.couple_spinbox.place(x=300, y=345, width=150, height=27)
                self.family_label.place(x=170, y=385)
                self.family_spinbox.place(x=300, y=385, width=150, height=27)
        else:
            # Nếu chưa chọn số (vẫn ở giá trị mặc định), ẩn các widget phụ
            self.single_label.place_forget()
            self.single_spinbox.place_forget()
            self.couple_label.place_forget()
            self.couple_spinbox.place_forget()
            self.family_label.place_forget()
            self.family_spinbox.place_forget()
        
        # Gọi lại hàm này sau 200ms để tiếp tục kiểm tra
        self.window.after(200, self.check_spinbox_values)
    def run(self):
        self.window.mainloop()
# Chạy ứng dụng
if __name__ == "__main__":
    # root = tk.Tk()
    app = HotelBookingApp()
    app.run()
