import json
import shopkeeper_db
import product_db
from login_db import DataBase as db
from shopkeeper_db import DataBase as db2

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
            return "admin not found!!!!"
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
class acceptSH:
    def __ini__(self,name="C:\\DataBase\\accept_shopkeepers.json"):
        self.name = name
    def read_list(self):
        file = open("C:\\DataBase\\accept_shopkeepers.json","r")
        return json.load(file)
    def request(self,new):
        temp = self.read_list()
        temp.append(new)
        file = open("C:\\DataBase\\accept_shopkeepers.json","w")
        json.dump(temp,file)
    def show1(self):
        temp = self.read_list()
        self.A = temp[0]
        return self.A
    def show2(self):
        temp = self.read_list()
        self.A = str(temp[0])
        return self.A
    def accept(self):
        shopkeeper_db.DataBase().add(self.show1())
        temp = self.read_list()
        del temp[0]
        file = open("C:\\DataBase\\accept_shopkeepers.json","w")
        json.dump(temp,file)
    def reject(self):
        temp = self.read_list()
        del temp[0]
        file = open("C:\\DataBase\\accept_shopkeepers.json","w")
        json.dump(temp,file)

class acceptPR:
    def __init__(self,name="C:\\DataBase\\accept_products.json"):
        self.name = name
    def read_list(self):
        file = open("C:\\DataBase\\accept_products.json","r")
        return json.load(file)
    def request(self,dict):
        dict = dict
        temp = acceptPR().read_list()
        temp.append(dict)
        file = open("C:\\DataBase\\accept_products.json","w")
        json.dump(temp,file)
    def show1(self):
        temp = acceptPR().read_list()
        self.A = temp[0]
        return self.A
    def show2(self):
        temp = acceptPR().read_list()
        self.A = str(temp[0])
        return self.A
    def accept(self):
        temp = acceptPR().read_list()
        dic = temp[0]
        name = dic["name"]
        temp1 = db().dict()
        ID = temp1["ID"]
        temp2 = db2().search(ID)
        delt2 = db2().delete(ID)
        temp2["products"].append(name)
        db2().add(temp2)
        product_db.DataBase().add(acceptPR().show1())
        temp = acceptPR().read_list()
        del temp[0]
        file = open("C:\\DataBase\\accept_products.json","w")
        json.dump(temp,file)

    def reject(self):
        temp = acceptPR().read_list()
        del temp[0]
        file = open(self.name,"w")
        json.dump(temp,file)
