"""
SVM - data analyse. Useful for extracting/ploting data

"""

class DataG:
    
    def __init__(self, data_configuration):
        
        if type(data_configuration) is dict:
            self.data = self.generate_samples(data_configuration) 
