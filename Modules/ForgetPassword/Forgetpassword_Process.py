from tkinter import messagebox
from tkinter import *
import sys
sys.path.append('C:/DoAn/doancuoiky-nhom1/Modules')
import Api.FrogetPassword_Api as ForgetPassword_Api

class Forgetpassword_Process:
    def confirm_button_handle(obj):
        username = obj.entry_1.get()
        password = obj.entry_2.get()
        api = ForgetPassword_Api.ForgetPassword_Api()
        c = api.check_user_login(username, password)