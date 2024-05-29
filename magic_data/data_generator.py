"""
SVM - data generator 

"""
import random
import pandas as pd
from pathlib import Path


class DataGenerator:
    
    def __init__(self, data_configuration):
        
        if type(data_configuration) is dict:
            self.data = self.generate_samples(data_configuration) 

    def generate_samples(self, data_configuration):
        
        samples = {}
        counter = 0
        for class_name in data_configuration:
            for _ in range(data_configuration[class_name].get("number_of_samples", None)):
                sample = []
                for _ in range(data_configuration[class_name].get("number_of_features", None)):
                    sample.append(random.uniform(data_configuration[class_name].get("min_range"), data_configuration[class_name].get("max_range")))
                counter+=1
                sample.append(class_name)
                samples.update({counter: sample})
   
        return samples
    
    def extract_as_csv(self, file_name="Default", file_route=""):
        df_data = pd.DataFrame(data=self.data)
        df_data = df_data.T
        df_data.to_csv(file_route.as_posix()+'/' + f'{file_name}.csv')