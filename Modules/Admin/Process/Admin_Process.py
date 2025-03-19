from tkinter import messagebox

from tkinter import *

import sys
# sys.path.append('C:/DoAn/doancuoiky-nhom1/Modules')
# # sys.path.append('c:/DoAn/doancuoiky-nhom1')
import Api.Hotel_Api as hotel_api
# import Modules.Admin.Landing_View as av
# import Modules.User.User_Landing_View as uv
# import Modules.Signup.Signup_View as suv
import Modules.Admin.Component.Hotels.Hotels_View as hv


class Admin_Process:

    @staticmethod
    def hotel_button_handle(obj):
        hotel_id = obj.entry_1.get()  # Get Hotel ID
        hotel_name = obj.entry_2.get()  # Get Hotel Name
        address = obj.entry_3.get()  # Get Address
        rating = obj.entry_4.get()  # Get Rating
        description = obj.entry_5.get()  # Get Description

        print(f"Inserting new hotel {hotel_id} with name: {hotel_name}")

        new_hotel = {
        "hotel_id": (hotel_id),  # Convert ID to integer if stored as int
        "hotel_name": hotel_name,
        "address": address,
        "rating": (rating),  # Convert to float if needed
        "description": description
        }


        api = hotel_api.Hotel_Api()
        c = api.add_new_hotel(new_hotel)

        if c == 1:
            # success
            messagebox.showinfo("MB", "Add hotel successful")
        else:
            # fail 
            messagebox.showerror("MB", "Fail add hotel")

    @staticmethod
    def clear_all_fields(obj):
        obj.entry_1.delete(0, "end")
        obj.entry_2.delete(0, "end")
        obj.entry_3.delete(0, "end")
        obj.entry_4.delete(0, "end")
        obj.entry_5.delete(0, "end")
        
    @staticmethod
    def button_handle(self):
        self.window.destroy()
        app = hv.Hotel_View()
        app.window.mainloop()