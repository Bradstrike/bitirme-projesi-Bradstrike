from models import User
from services import DataService

class UserController:
    def __init__(self, user, data_service):
        self.user = user
        self.data_service = data_service

    def view_data(self):
        return self.data_service.get_data()

class AdminController(UserController):
    def __init__(self, user, data_service):
        super().__init__(user, data_service)

    def update_data(self, updated_data):
        self.data_service.update_data(updated_data)

    def save_data(self, output_path):
        self.data_service.save_to_excel(output_path)