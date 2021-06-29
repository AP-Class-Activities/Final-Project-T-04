import sys
import os
sys.path[0]
import json

class DataBase:
    def __init__(self):
        self.name = "C:\\DataBase\\customer.json"
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
                    return dictionaries,1
        else:
            return "User not found!!!!",0
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
    def counter(self):
        lst = self.read_list()
        count = 624311
        for i in lst:
            count += 7
        st_counter = str(count)
        return st_counter