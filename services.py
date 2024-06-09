import pandas as pd

class DataService:
    def __init__(self, data_path=None):
        self.data_path = data_path
        self.data = pd.DataFrame()
        if data_path:
            self.load_data(data_path)

    def load_data(self, data_path):
        self.data_path = data_path
        self.data = pd.read_csv(data_path)

    def get_data(self):
        return self.data

    def update_data(self, updated_data):
        self.data = updated_data

    def save_to_excel(self, output_path):
        self.data.to_excel(output_path, index=False)