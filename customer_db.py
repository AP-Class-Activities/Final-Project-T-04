import json

class DataBase:
    def __init__(self):
        self.name = "C:\\DataBase\\customer.json"
    def read_list(self):
        file = open(self.name,"r")
        return json.load(file)