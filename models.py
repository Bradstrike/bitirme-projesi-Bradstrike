class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role  # 'admin' veya 'user'

    def check_password(self, password):
        return self.password == password