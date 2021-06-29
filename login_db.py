import json
class DataBase:
    def __init__(self):
        self.name = "C:\\DataBase\\login.json"
    def read_list(self):
        file = open(self.name,"r")
        return json.load(file)
    def add(self,new:dict):
        temp = self.read_list()
        temp.clear()
        temp.append(new)
        file = open(self.name,"w")
        json.dump(temp,file)
        return True
    def dict(self):
        temp = self.read_list()
        dictionary = temp[0]
        return dictionary