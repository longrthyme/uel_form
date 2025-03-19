import Api.Main_Api as main_api
from tkinter import messagebox


class Sale_Api(main_api.Api):

    def __init__(self):
        super().__init__()
        self.connector()

    # user login api
    def add_new_hotel(self, new_hotel):
        pass

        