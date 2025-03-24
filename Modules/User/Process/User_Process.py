from tkinter import messagebox

from tkinter import *

import sys
import Api.Hotel_Api as hotel_api
import Api.Invoice_Api as invoice_api
import Modules.User.Component.Booking_Hotels.Booking_Page as bp
import Modules.User.Component.Booking_Hotels.Invoice as invoice
import Modules.User.Component.Booking_Hotels.End as end
import Modules.User.User_Landing_View as usmv

import Modules.Login.Login_View as lv

from datetime import datetime
import unicodedata
import uuid
import re
from Modules.User.global_vars import filter_room_book_data
class User_Process:

    # @staticmethod
    # def clear_all_fields(obj):
    #     obj.entry_1.delete(0, "end")
    #     obj.entry_2.delete(0, "end")
    #     obj.entry_3.delete(0, "end")
    #     obj.entry_4.delete(0, "end")
    #     obj.entry_5.delete(0, "end")
    
    @staticmethod
    def normalize_text(text):
        # Convert to lowercase and strip spaces
        text = text.lower().strip()
        # Remove accents (diacritics)
        text = ''.join(c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn')
        return text


    @staticmethod
    def button_handle(self, view_type):
        
        if view_type == "filter":
            city = self.city_combobox.get()
            day1 = self.combobox1.get()
            month1 = self.combobox2.get()
            year1 = self.combobox3.get()
            day2 = self.combobox4.get()
            month2 = self.combobox5.get()
            year2 = self.combobox6.get()
            
             # Get values from Spinbox widgets
            adults = self.adult_spinbox.get()
            children = self.children_spinbox.get()
            single_room = self.single_spinbox.get()
            couple_room = self.couple_spinbox.get()
            family_room = self.family_spinbox.get()

            # In ra để kiểm tra
            print(f"City: {city}")
            print(f"Check-in Date: {day1}-{month1}-{year1}")
            print(f"Check-out Date: {day2}-{month2}-{year2}")
            print(f"Adults: {adults}")
            print(f"Children: {children}")
            print(f"Single Room: {single_room}")
            print(f"Couple Room: {couple_room}")
            print(f"Family Room: {family_room}")
            

            filter_room_book_data["check_in_day"] = day1
            filter_room_book_data["check_in_month"] = month1
            filter_room_book_data["check_in_year"] = year1
            filter_room_book_data["check_out_day"] = day2
            filter_room_book_data["check_out_month"] = month2
            filter_room_book_data["check_out_year"] = year2

            filter_room_book_data["adults"] = self.adult_spinbox.get() if self.adult_spinbox.get() else "0"
            filter_room_book_data["children"] = self.children_spinbox.get() if self.children_spinbox.get() else "0"
            filter_room_book_data["single_room"] = self.single_spinbox.get() if self.single_spinbox.get() else "0"
            filter_room_book_data["couple_room"] = self.couple_spinbox.get() if self.couple_spinbox.get() else "0"
            filter_room_book_data["family_room"] = self.family_spinbox.get() if self.family_spinbox.get() else "0"

            # cities = ["Hồ Chí Minh", "ho chi minh", "Hồ chí minh", " ho chi minh ", " hồ chí minh "]

            # # Print normalized results
            # for city in cities:
            #     normalized = User_Process.normalize_text(city)
            #     print(f"Original: '{city}' -> Normalized: '{normalized}'")
                
            
            normalized_city = User_Process.normalize_text(city)

                # Create a regex pattern to match variations
# Replace spaces with `\s*` (for flexible matching)
            city_pattern = r"\s*".join(normalized_city.split())  # Correct handling of spaces

            print(f"City Pattern: {city_pattern}")


            collation = { "locale": "vi", "strength": 1 }

            result_cursor = hotel_api.Hotel_Api().hotels_collection.aggregate([
                {
                    "$lookup": {
                        "from": "rooms",
                        "localField": "hotel_id",
                        "foreignField": "hotel_id",
                        "as": "rooms"
                    }
                },
                {
                    "$match": { "address": city }
                }
            ])

            # Convert the cursor to a list
            result = list(result_cursor)
            print(f"Normalized Query Result: {result}")

            # Convert cursor to a list
            # result = list(result_cursor)

            if not result:  # If no hotels match the filter
                messagebox.showinfo("No Results", "No hotels found for the selected location.")
                return  # Stop execution

            print(f"Results: {result}")
            # If results are found, process them
            rooms_data = []
            for hotel in result:
                print(f"Hotel: {hotel['hotel_name']}, Address: {hotel['address']}")
                if "rooms" in hotel and hotel["rooms"]:
                    for room in hotel["rooms"]:
                        room["hotel_name"] = hotel["hotel_name"]
                        print(f"  Room: {room['room_id']}, Price: {room['price']}")
                        rooms_data.append(room)

            # Close current window and open Hotel View with room data
            self.window.destroy()
            print("rooms data 1: ", rooms_data)
            app = bp.Hotel_View(rooms_data)
        elif view_type == "overview":
            self.window.destroy()
            if(self.selected_room):
                print("selected room: ", self.selected_room)
                room_price = self.selected_room

            app = invoice.Invoice_View(room_price)
        elif view_type == "end":
            
            
            api = invoice_api.Invoice_Api()

            print(f"log usser", filter_room_book_data["loged_user"])

            new_invoice = {
                "invoice_id": f"INV-{str(uuid.uuid4())}",
                "room_id": filter_room_book_data.get("room_id", "N/A"),
                "invoice_date": datetime.now().strftime("%Y-%m-%d"),
                "check_in_day": self.entry_2.get(),
                "check_out_day": self.entry_3.get(),
                "note": self.entry_5.get(),
                "price": self.entry_4.get(),
                "total":self.entry_7.get(),
                "hotel_name": filter_room_book_data.get("hotel_name", "Arena"),
                "quantity": 1,
                "customer_name": filter_room_book_data.get("loged_user", "N/A"),
                "adults": filter_room_book_data.get("adults", "0"),
                "children": filter_room_book_data.get("children", "0"),
                "single_room": filter_room_book_data.get("single_room", "0"),
                "couple_room": filter_room_book_data.get("couple_room", "0"),
                "family_room": filter_room_book_data.get("family_room", "0"),

            }

            result =  api.add_invoice(new_invoice)

            print(f"Result invoice", result)

            invoice_detail = api.get_invoice(result.inserted_id)

            print(f"Result invoice detail", invoice_detail)

            self.window.destroy()

            app = end.Hotel_View(invoice_detail)
        elif view_type == "logout":
            self.window.destroy()
            app = lv.Login_View()
        elif view_type == "quit":
            self.window.destroy()
            app = usmv.User_Landing_View()
        app.window.mainloop()