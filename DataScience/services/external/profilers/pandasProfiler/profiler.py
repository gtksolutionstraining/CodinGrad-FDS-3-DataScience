import pandas as pd
import ydata_profiling as yp
from services.external.profilers.pandasProfiler.basicDetails import(
    BasicDetails
)
class PandasProfiler:
    def __init__(self,dataPath):
        self.data_path = dataPath
        self.__read_csv()
        self.__profile_data()
        self.__get_description()
        self.basicDetails = BasicDetails(self.reportDict)

    def __read_csv(self):
        self.data = pd.read_csv(self.data_path)

    def __profile_data(self):
        self.report = yp.ProfileReport(self.data)
    
    def __get_description(self):
        self.reportDict = self.report.get_description()
    
    

    