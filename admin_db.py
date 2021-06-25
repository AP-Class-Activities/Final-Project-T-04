import json

class DataBase:
    def __init__(self):
        self.name = "C:\\DataBase\\admin.json"
    def read_list(self):
        file = open(self.name,"r")
        return json.load(file)
    def add(self,new:dict):
        temp = self.read_list()
        ID = self.search_value(new["ID"])
        user = self.search_value(new["user"])
        email = self.search_value(new["email"])
        if ID == 1 or user == 1 or email == 1:
            print("admin already added!")
            return 0
        else:
            temp.append(new)
            file = open(self.name,"w")
            json.dump(temp,file)
            print("admin added!")
            return 1