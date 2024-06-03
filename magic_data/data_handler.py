from abc import ABC, abstractmethod
import pandas as pd
class DataHandler():

    def __init__(self, data_configuration={}, file_name="Default", file_route="") -> None:
        
        if type(data_configuration) is dict:
            self.data_configuration = data_configuration 
        self.file_name = file_name
        self.file_route = file_route

    def extract_data(self):
        # extract the data csv
        file_name_csv = self.file_name +".csv"
        file_route_csv = self.file_route / file_name_csv
        data_csv = pd.read_csv(file_route_csv)
        return data_csv.to_dict()