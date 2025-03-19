import Api.Main_Api as main_api
import datetime
from tkinter import messagebox


class User_Api(main_api.Api):
    total_cart = []
    temp = 0

    def __init__(self):
        super().__init__()
        self.connector()

    def create_user(self, user):
        """Create a new user with username, password, and role."""
        if not user.get("Username") or not user.get("Password") or not user.get("Roles"):
            messagebox.showerror("Error", "Username, password, and role are required")
            return False  # Validation failed

        # Check if the username already exists
        existing_user = self.users_collection.find_one({"Username": user["Username"]})
        if existing_user:
            messagebox.showerror("Error", "Username already exists. Choose a different username.")
            return False

        try:
            result = self.users_collection.insert_one(user)
            messagebox.showinfo("Success", f"User created successfully! ID: {result.inserted_id}")
            return True
        except DuplicateKeyError as e:
            messagebox.showerror("Error", f"Duplicate key error: {e}")
            return False
    def update_user(self, username, updated_fields):
        """Update user details based on username."""
        result = self.users_collection.update_one(
            {"Username": username},  # Find user by username
            {"$set": updated_fields}  # Update specific fields
        )

        if result.modified_count > 0:
            messagebox.showinfo("Success", f"User '{username}' updated successfully.")
            return True
        else:
            messagebox.showerror("Info", f"No updates made for user '{username}'.")
            return False

    def delete_user(self, username):
        """Delete a user by username."""
        result = self.users_collection.delete_one({"Username": username})

        if result.deleted_count > 0:
            messagebox.showinfo("Success", f"User '{username}' deleted successfully.")
            return True
        else:
            messagebox.showerror("Error", f"User '{username}' not found.")
            return False

    # get last Invoice_ID from invoice collection
    def get_last_invoice_id(self):
        try:
            self.cursor = self.invoices_collection.find().sort(
                [('Invoice_ID', -1)])
            self.last_invoice_id = self.cursor[0]['Invoice_ID']
            return self.last_invoice_id
        except:
            return "ID000"

    def create_new_invoice_id(self):
        self.last_invoice_id = self.get_last_invoice_id()
        id = self.last_invoice_id
        number = id[2:]
        new_id = int(number) + 1
        self.new_invoice_id = 'ID' + str(100 + int(new_id)).replace("1", "0", 1)

    def add_item_to_cart(self, film, quantity):
        data = self.warehouse_collection.find_one(
            {'Film': film})
        if data == None:
            return -1  # error 1: film is not exist
        else:
            film_id = data['Film_ID']
            film = data['Film']
            price = data['Price']
            stock = data['Stock']
        try:
            quantity = float(quantity)
        except:
            return -3  # error 3: quantity is not a number

        if float(stock) < float(quantity):
            return -2  # error 2: not enough stock
        else:
            stock = float(stock) - float(quantity)
        # check film_id is in User_Api.total_cart
        if len(User_Api.total_cart) != 0:
            for i in range(len(User_Api.total_cart)):
                if User_Api.total_cart[i]['film_ID'] == film_id:
                    x = float(User_Api.total_cart[i]['Quantity']) + float(quantity)
                    if float(stock) < x:
                        return -2  # error 2: not enough stock
                    else:
                        User_Api.total_cart[i]['Quantity'] = x
                        User_Api.total_cart[i]['Price'] = float(User_Api.total_cart[i]['Price']) + float(
                            quantity) * float(price)
                        stock = float(stock) - float(quantity)
                        User_Api.temp = User_Api.total_cart[i]['Price']
                        return -4  # error 4: film already in cart

            self.cart = {}
            self.cart['Film_ID'] = film_id
            self.cart['Film'] = film
            self.cart['Quantity'] = quantity
            self.cart['Price'] = float(price) * float(quantity)
            User_Api.total_cart.append(self.cart)

            return self.cart

        else:
            self.cart = {}
            self.cart['Film_ID'] = film_id
            self.cart['Film'] = film
            self.cart['Quantity'] = quantity
            self.cart['Price'] = float(price) * float(quantity)

            # add cart to cart.json in Data folder
            User_Api.total_cart.append(self.cart)

            return self.cart

    # process
    def process_cart(self):
        self.create_new_invoice_id()
        sum = 0
        if len(User_Api.total_cart) != 0:
            for i in range(len(User_Api.total_cart)):
                sum = sum + User_Api.total_cart[i]['Price']

            dict = {'Invoice_ID': self.new_invoice_id, 'Invoice_Date': datetime.datetime.now(
            ), 'Cart': User_Api.total_cart, 'Total': sum}
            self.invoices_collection.insert_one(dict)
            # update stock in warehouse collection
            for i in range(len(User_Api.total_cart)):
                self.cursor = self.warehouse_collection.find(
                    {'Film': User_Api.total_cart[i]['Film']})
                for data in self.cursor:
                    self.warehouse_collection.update_one({'Film': User_Api.total_cart[i]['Film']}, {
                        '$set': {'Stock': float(data['Stock']) - float(User_Api.total_cart[i]['Quantity'])}})

            User_Api.total_cart = []
            User_Api.temp = 0
            return 0  # success
        else:
            return -1

    # get all product name from warehouse collection
    def get_all_film_name(self):
        cursor = self.warehouse_collection.find()
        film = []
        for data in cursor:
            film.append(data['Film'])
        return film

    def remove_item_from_cart(self, film):
        for i in range(len(User_Api.total_cart)):
            if User_Api.total_cart[i]['Film'] == film:
                User_Api.total_cart.pop(i)
                return 0  # success
        return -1  # error 1: film is not exist

    # get all warehouse data by function get_all_warehouse_data
    # get all invoice data by function get_all_invoice_data
