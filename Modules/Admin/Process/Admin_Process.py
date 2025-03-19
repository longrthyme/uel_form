from tkinter import messagebox

from tkinter import *

import sys
# sys.path.append('C:/DoAn/doancuoiky-nhom1/Modules')
# # sys.path.append('c:/DoAn/doancuoiky-nhom1')
import Api.Hotel_Api as hotel_api
import Api.User_Api as user_api
import Api.Inventory_Api as inventory_api

# import Modules.Admin.Landing_View as av
# import Modules.User.User_Landing_View as uv
# import Modules.Signup.Signup_View as suv
import Modules.Admin.Component.Hotels.Hotels_View as hv
import Modules.Admin.Component.Users.Users_View as uv
import Modules.Admin.Component.Checksales.Checksales_View as sl
import Modules.Admin.Component.Inventory.Inventory_View as it
import Modules.Login.Login_View as lv

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
    def inventory_clear_fields(obj):
        obj.entry_1.delete(0, "end")
        obj.entry_2.delete(0, "end")
        obj.entry_3.delete(0, "end")
        obj.entry_4.delete(0, "end")
        obj.entry_5.delete(0, "end")
        obj.entry_6.delete(0, "end")

    @staticmethod
    def inventory_action_handle(obj, type):
        hotel_name = obj.entry_1.get()  # Get Hotel Name
        description = obj.entry_2.get()  # Get Description
        type_room = obj.entry_3.get()  # Get Type Room
        price = (obj.entry_4.get())  # Convert price to float
        stock = (obj.entry_5.get())  # Convert stock to integer

        inventory_data = {
            "hotel_name": hotel_name,
            "description": description,
            "type_room": type_room,
            "price": price,
            "stock": stock
        }

        if type == "update":
            # Update only price and stock based on hotel_name and type_room
            updated_fields = {"price": price, "stock": stock,  "description": description,
            "type_room": type_room, "hotel_name": hotel_name}
            api = inventory_api.Inventory_Api()
            api.update_inventory(hotel_name, updated_fields)
            print(f"Inventory updated for {hotel_name} ")

        else:
            messagebox.showerror("Error", "Invalid action type!")
    @staticmethod
    def user_action_handle(obj, type):
        # type: update, delete, create new 
        username = obj.entry_1.get()  # Get Hotel ID
        password = obj.entry_2.get()  # Get Hotel Name
        role = obj.entry_3.get()  # Get Address

        print(f"User action: {type} with username: {username} and password: {password} and role: {role}")

        user = {
            "Username": username,
            "Password": password,
            "Roles": role
        }

        api = user_api.User_Api()

        if type == "create":
            print(f"Create new user: {username}")
            api.create_user(user)

        elif type == "update":
            print(f"Update user: {username} with password: {password} and role: {role}")
            
            updated_fields = {"Password": password, "Roles": role}
            api.update_user(username, updated_fields)

        else: 
            # delete user 
            api.delete_user(username)
            # pass 

    @staticmethod
    def button_handle(self, view_type):
        
        self.window.destroy()
        if view_type == "hotel":
            app = hv.Hotel_View()
        elif view_type == "user":
            app = uv.Admin_Users()
        elif view_type == "sale":
            app = sl.Admin_Users()
        elif view_type == "inventory":
            app = it.Admin_Users()
        elif view_type == "logout":
            app = lv.Login_View()
        else:
            messagebox.showerror("Error", "Invalid view type")
            return  # Exit function if invalid type

        app.window.mainloop()