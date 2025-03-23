import tkinter as tk
from tkinter import Canvas, PhotoImage, Button
from pathlib import Path
from tkinter import ttk
import Modules.User.Process.User_Process as up
from Modules.User.global_vars import filter_room_book_data

class Hotel_View:
    def __init__(self, rooms_data):
        self.window = tk.Tk()
        self.rooms_data = rooms_data

        print("rooms data: ", self.rooms_data)
        
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

        # assets_path = Path(r"C:\DoAn\Image\User\Room2")

        assets_path = Path(r"/home/long/Downloads/doancuoiky-nhom1/Image/User/Room2")

        self.background_img = PhotoImage(file=assets_path / "Background.png")
        self.account_image = PhotoImage(file=assets_path / "Button_Account.png")
        self.homepage_image = PhotoImage(file=assets_path / "Button_Homepage.png")
        self.logout_image = PhotoImage(file=assets_path / "Button_Logout.png")
        self.update_image = PhotoImage(file=assets_path / "Button_Update.png")


        self.background = self.canvas.create_image(342.0, 246.0, image=self.background_img)

        self.account_button = Button(image=self.account_image, borderwidth=0, highlightthickness=0)
                            #    command=lambda: signup_process.Signup_Process.login_button_handle(self))
        self.account_button.place(x=76, y=16, width=39, height=39)

        self.update_button = Button(image=self.update_image, borderwidth=0, highlightthickness=0,relief="flat",
                                    command=lambda: up.User_Process.button_handle(self, 'overview'))
        self.update_button.place(x=570, y=457, width=97.8, height=24.6)

        self.homepage_button = Button(image=self.homepage_image,borderwidth=0,highlightthickness=0)
        self.homepage_button.place(x=37.3,y=70.1,width=130.4,height=32.8)

        self.logout_button = Button(image=self.logout_image,borderwidth=0,highlightthickness=0)
        self.logout_button.place(x=563,y=26,width=103.28,height=32.8)




        self.title_label = tk.Label(self.window, text="Price List", font=("Inter", 16, "bold"), bg="#FFFFFF")
        self.title_label.place(x=25,y=150,width=642,height=60)

        # Tạo frame chứa bảng
        self.table_frame = tk.Frame(self.window, bg="#D9E7C5", width=642, height=230)
        self.table_frame.place(x=25, y=210)

        # Tạo Treeview cho bảng
        self.tree = ttk.Treeview(self.table_frame, columns=("Room Number", "Price", "Description"), show="headings")

        # Đặt tiêu đề các cột
        self.tree.heading("Room Number", text="Room Number")
        self.tree.heading("Price", text="Price")
        self.tree.heading("Description", text="Description")

        # Đặt chiều rộng cho các cột
        self.tree.column("Room Number", width=100, anchor="center")
        self.tree.column("Price", width=100, anchor="center")
        self.tree.column("Description", width=442, anchor="w")

        # Đặt kích thước bảng
        self.tree.place(x=0, y=0, width=642, height=230)
        self.populate_rooms()

        self.tree.bind("<ButtonRelease-1>", self.handle_selected_row)
    
    def handle_selected_row(self, event):
        """Retrieve and handle the data from the selected row."""
        # Get the selected item id
        selected_item = self.tree.focus()
        if not selected_item:
            return
        
        # Retrieve the row's values
        row_values = self.tree.item(selected_item, 'values')
        print("Selected row values:", row_values)
        
        # Save the selected room data into a self variable for later use
        self.selected_room = {
            "room_id": row_values[0],
            "price": row_values[1],
            "description": row_values[2]
        }

        filter_room_book_data["room_id"] = row_values[0]

    def populate_rooms(self):
        for room in self.rooms_data:
            self.tree.insert("", "end", values=(room.get("room_id", "N/A"), room.get("price", "N/A"), room.get("description", "No Description")))

    def run(self):
        self.window.mainloop()
# Chạy ứng dụng
if __name__ == "__main__":
    # root = tk.Tk()
    app = Hotel_View()
    app.run()