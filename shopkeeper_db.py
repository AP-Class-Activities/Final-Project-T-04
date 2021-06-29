import json

class DataBase:
    def __init__(self):
        self.name = "C:\\DataBase\\shopkeeper.json"
    def read_list(self):
        file = open(self.name,"r")
        return json.load(file)
    def add(self,new:dict):
        temp = self.read_list()
        ID = self.search_value(new["ID"])
        user = self.search_value(new["user"])
        email = self.search_value(new["email"])
        if ID == 1 or user == 1 or email == 1:
            return False
        else:
            temp.append(new)
            file = open(self.name,"w")
            json.dump(temp,file)
            return True
    def search(self,key):
        lst = self.read_list()
        for dictionaries in lst:
            for j,i in dictionaries.items():
                if key == i:
                    return dictionaries
        else:
            return False
    def search_value(self,value):
        lst = self.read_list()
        for dictionaries in lst:
            for j,i in dictionaries.items():
                if value == i:
                    return 1
        else:
            return 0
    def delete(self,value):
        key = self.search(value)
        temp = self.read_list()
        temp.remove(key)
        file = open(self.name,"w")
        json.dump(temp,file)
    def check(self, username, password):
        lst = self.read_list()
        for dictionary in lst:
            user = dictionary["user"]
            passw = dictionary["password"]
            if user == username and passw == password:
                return True
        else:
            return False
    def products(self,ID,new_product):
        dictionary = self.search(ID)
        comment = dictionary["products"].append(new_product)
        delete = self.delete(ID)
        temp = self.read_list()
        temp.append(dictionary)
        file = open(self.name,"w")
        json.dump(temp,file)
    def sold_items(self,ID,value):
        dictionary = self.search(ID)
        comment = dictionary["sold items"].append(value)
        delete = self.delete(ID)
        temp = self.read_list()
        temp.append(dictionary)
        file = open(self.name,"w")
        json.dump(temp,file)
    def orders(self,ID,value):
        dictionary = self.search(ID)
        comment = dictionary["orders"].append(value)
        delete = self.delete(ID)
        temp = self.read_list()
        temp.append(dictionary)
        file = open(self.name,"w")
        json.dump(temp,file)
    def counter(self):
        lst = self.read_list()
        count = 554321
        for i in lst:
            count += 1
        st_counter = str(count)
        return st_counter