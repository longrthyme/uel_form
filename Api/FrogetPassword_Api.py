import Api.Main_Api as main_api
from werkzeug.security import generate_password_hash
class ForgetPassword_Api(main_api.Api):
    def __init__(self):
        super().__init__()
        self.connector()

        # Kiểm tra thay đổi mật khẩu
    def reset_password(self, username, phone_number, new_password, re_new_password):
        if new_password != re_new_password:
            return {"error": "Passwords do not match"}, 400
        
        # Tìm người dùng trong cơ sở dữ liệu
        user = self.users_collection.find_one({'username': username, 'phone_number': phone_number})
        
        if not user:
            return {"error": "User not found or phone number mismatch"}, 404
        
        # Mã hóa mật khẩu mới và cập nhật vào cơ sở dữ liệu
        hashed_password = generate_password_hash(new_password)
        self.users_collection.update_one(
            {'username': username, 'phone_number': phone_number},
            {'$set': {'password': hashed_password}}
        )
        
        return {"message": "Password successfully updated"}, 200