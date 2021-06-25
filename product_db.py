import json

class DataBase:
    def __init__(self):
        self.name = "C:\\DataBase\\product.json"
    def read_list(self):
        file = open(self.name,"r")
        return json.load(file)
    def add(self,new:dict):
        temp = self.read_list()
        ID = self.search_value(new["ID"])
        if ID == 1:
            print("product already added!")
            return 0
        else:
            temp.append(new)
            file = open(self.name,"w")
            json.dump(temp,file)
            print("product added!")
            return 1