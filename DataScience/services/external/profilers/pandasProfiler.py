import pandas as pd
# import ydata_profiler as yp

class PandasProfiler:
    def __init__(self,dataPath):
        self.data_path = dataPath
        self.__read_data()
        self.__get_dataset_name()
        self.__get_columns()

    def __read_data(self):
        self.data = pd.read_csv(self.data_path)

    def __get_dataset_name(self):
        self.dataset_name = self.data_path.split('/')[-1].split('.')[0]

    def __get_columns(self):
        self.columns = self.data.columns.to_list()