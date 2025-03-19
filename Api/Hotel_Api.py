import Api.Main_Api as main_api
from tkinter import messagebox


class Hotel_Api(main_api.Api):

    def __init__(self):
        super().__init__()
        self.connector()

    # user login api
    def add_new_hotel(self, new_hotel):
        # Validate required fields
        required_fields = ["hotel_id", "hotel_name", "address", "rating", "description"]
        
        for field in required_fields:
            if field not in new_hotel or new_hotel[field] == "":
                messagebox.showerror("Error", f"{field} is required")  
                return -1  # Error: Missing field
        
        try:
            # Insert into MongoDB
            result = self.hotels_collection.insert_one(new_hotel)
            print("Hotel created successfully! ID:", result.inserted_id)
            return 1  # Success
        except Exception as e:
            print("Error inserting hotel:", str(e))
            return -2  # Error: Database insertion failed

        