from common.libs import (
    yaml,
    pd,
    json
)
class FileUtils:
    """
    Class FileUtils:
    Its a class for managing different files like yaml, csv, json, etc.

    Arguments: 

    Functions:
    1. read_yaml()
    2. read_csv()
    3. read_json()
    
    """
    def __init__(self) -> None:
        pass

    def read_yaml(self,file_path):
        """
        Method read_yaml:
        This is method for reading yaml files

        Arguments: 
            - file_path -> path of the yaml file
        Returns:
            - A dictionary containing yaml file information
        """
        with open(file_path,"r") as file:
            data = yaml.safe_load(file)
        return data
    
    def read_csv(self,file_path):
        """
        """
        data = pd.read_csv(file_path)
        return data
    
    def read_excel(self,file_path):
        data = pd.read_excel(file_path)
        return data
        
    def read_json(self,file_path):
        with open(file_path,'r') as file:
            data = json.load(file)
        return data