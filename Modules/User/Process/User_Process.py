from tkinter import messagebox

from tkinter import *

import sys
import Api.Hotel_Api as hotel_api
import Modules.User.Component.Booking_Hotels.Booking_Page as bp
import Modules.User.Component.Booking_Hotels.Invoice as invoice
import unicodedata
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
            
            # In ra để kiểm tra
            print(f"City: {city}")
            print(f"Check-in Date: {day1}-{month1}-{year1}")
            print(f"Check-out Date: {day2}-{month2}-{year2}")

            filter_room_book_data["check_in_day"] = day1
            filter_room_book_data["check_in_month"] = month1
            filter_room_book_data["check_in_year"] = year1
            filter_room_book_data["check_out_day"] = day2
            filter_room_book_data["check_out_month"] = month2
            filter_room_book_data["check_out_year"] = year2

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
        app.window.mainloop()