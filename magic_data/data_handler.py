"""
SVM - data generator 

"""
import random
import pandas as pd
from pathlib import Path
import json

class DataHandler:
    
    def __init__(self, data_configuration="", file_name="Default", file_route=""):
        
        if type(data_configuration) is dict:
            self.data_configuration = data_configuration 
        self.file_name = file_name
        self.file_route = file_route

    def generate_samples(self):
        
        samples = {}
        counter = 0
        for class_name in self.data_configuration:
            for _ in range(self.data_configuration[class_name].get("number_of_samples", None)):
                sample = []
                for _ in range(self.data_configuration[class_name].get("number_of_features", None)):
                    sample.append(random.uniform(self.data_configuration[class_name].get("min_range"), self.data_configuration[class_name].get("max_range")))
                counter+=1
                sample.append(class_name)
                samples.update({counter: sample})
   
        self.store_as_csv(data=samples)
        self.save_configuration_json()
    
    def store_as_csv(self, data={}):
        
        df_data = pd.DataFrame(data=data)
        df_data = df_data.T
        df_data.to_csv(self.file_route.as_posix()+'/' + f'{self.file_name}.csv')

    def save_configuration_json(self):

        file_name = self.file_name +'.json'
        file_path = self.file_route.as_posix()+'/'+ file_name
        with open(file_path, "w") as json_file:
            json.dump(self.data_configuration, json_file)

    def extract_data_csv():
        return