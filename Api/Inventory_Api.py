import Api.Main_Api as main_api
from tkinter import messagebox


class Inventory_Api(main_api.Api):

    def __init__(self):
        super().__init__()
        self.connector()

    # user login api
    def update_inventory(self, hotel_name, type_room, updated_fields):
        """Update inventory details based on hotel_name and type_room."""
        result = self.inventory_collection.update_one(
            {"hotel_name": hotel_name, "type_room": type_room},  # Find by hotel and room type
            {"$set": updated_fields}  # Update only specified fields
        )

        if result.modified_count > 0:
            messagebox.showinfo("Success", f"Inventory updated for {hotel_name} - {type_room}.")
            return True
        else:
            messagebox.showerror("Error", f"No updates made for {hotel_name} - {type_room}.")
            return False


        