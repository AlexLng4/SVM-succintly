from abc import ABC, abstractmethod

class DataHandler(ABC):

    def __init__(self, data_configuration={}, file_name="Default", file_route="") -> None:
        
        if type(data_configuration) is dict:
            self.data_configuration = data_configuration 
        self.file_name = file_name
        self.file_route = file_route