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
            pass
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
    def comment(self,ID,new_comment):
        dictionary = self.search(ID)
        comment = dictionary["comments"].append(new_comment)
        delete = self.delete(ID)
        temp = self.read_list()
        temp.append(dictionary)
        file = open(self.name,"w")
        json.dump(temp,file)
    def counter(self):
        lst = self.read_list()
        count = 125389
        for i in lst:
            count += 6
        st_counter = "PR"+str(count)
        return st_counter