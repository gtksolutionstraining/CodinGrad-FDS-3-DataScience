from config import DATA_PATH
import pandas as pd

class Profiler:
    def __init__(self):
        self.dataset_name = None
        self.dataset_path = None
        self.dataset_columns = None
        self.read_csv()

    def read_csv(self):
        self.data = pd.read_csv(DATA_PATH)

    def get_dataset_name(self):
        self.dataset_name = DATA_PATH.split('/')[-1].split('.')[0]
        return self.dataset_name
    
    def get_columns(self):
        self.columns = self.data.columns.to_list()
        return self.columns
    