import Api.Main_Api as main_api
from tkinter import messagebox


class Invoice_Api(main_api.Api):

    def __init__(self):
        super().__init__()
        self.connector()

    # user login api
    def add_invoice(self, invoice):
        """add invoice"""
        try:
            result = self.invoices_booking.insert_one(invoice)  # Insert document into MongoDB
            print("Invoice inserted with ID:", result.inserted_id)
            messagebox.showinfo("Success", "Invoice added successfully.")
            return result
        except Exception as e:
            print("Error inserting invoice:", e)
            messagebox.showerror("Error", "Failed to add invoice.")
            return {"status": "error", "message": str(e)}

    def get_invoice(self, inserted_id):
        invoice = self.invoices_booking.find_one({"_id": inserted_id})
        return invoice


        