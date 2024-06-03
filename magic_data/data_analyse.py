"""
SVM - data analyse. Useful for extracting/ploting data

"""
from magic_data.data_handler import DataHandler
import pandas as pd

class DataAnalyse(DataHandler):
    
    def __init__(self, file_name="Default" ,file_route=""):
        super().__init__(file_name=file_name, file_route=file_route)
        

