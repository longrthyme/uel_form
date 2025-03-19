import Api.Main_Api as main_api
import re

class Signup_Api(main_api.Api):
    
    def __init__(self):
        super().__init__()
        self.connector()

    # user sign up api
    def check_user_signup(self, username, password, reenterpassword):
        if username == "" or password == "" or reenterpassword == "":
            return -1  # error 1: username or password is empty
        if password != reenterpassword:
            return -2  # error 2: password is not the same
        user = self.users_collection.find_one({'Username': username})
        if user != None:
            return -3  # error 3: username is already exist
        self.users_collection.insert_one(
            {'Username': username, 'Password': password, 'Roles': "User"})
        return 0  # success
    
    def check_password_standard(self, password):
        # Kiểm tra mật khẩu có đủ các yếu tố không (ít nhất 8 ký tự, có chữ hoa, chữ thường, số, ký tự đặc biệt)
        if len(password) < 8:
            return 1

        elif not re.search("[a-z]", password):  # Kiểm tra chữ cái thường
            return 2

        elif not re.search("[A-Z]", password):  # Kiểm tra chữ cái hoa
            return 3

        elif not re.search("[0-9]", password):  # Kiểm tra số
            return 4
        elif not re.search("[!@#$%^&*(),.?\":{}|<>]", password):  # Kiểm tra ký tự đặc biệt
            return 5
        else:
            return 0

