"""
SVM - data analyse. Useful for extracting/ploting data

"""
from magic_data.data_handler import DataHandler

class DataAnalyse(DataHandler):
    
    def __init__(self, file_route):
        super().__init__(file_route)
        
