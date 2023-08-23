import pandas as pd
# import ydata_profiler as yp

class PandasProfiler:
    def __init__(self,dataPath):
        self.data_path = dataPath
        self.__read_data()
        self.__get_dataset_name()
        self.__get_features()
        self.__get_number_of_features()
        self.__get_number_of_datapoints()
        self.__get_duplicate_rows()
        self.__get_missing_cells()
        self.__get_missing_features()
        
    def __read_data(self):
        self.data = pd.read_csv(self.data_path)

    def __get_dataset_name(self):
        self.dataset_name = self.data_path.split('/')[-1].split('.')[0]

    def __get_features(self):
        self.features = self.data.columns.to_list()
    
    def __get_number_of_features(self):
        self.number_features = len(self.features)

    def __get_number_of_datapoints(self):
        self.number_datapoints = len(self.data)

    def __get_duplicate_rows(self):
        self.duplicate_datapoints = self.data.duplicated().sum()

    def __get_missing_cells(self):
        self.missing_cells = self.data.isna().sum().sum()

    def __get_missing_features(self):
        self.missing_features = []
        for feature in self.data.columns:
            if self.data[feature].isna().sum() > 0:
                self.missing_features.append(feature)
