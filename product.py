class product:
    def __init__(self,name,count,code,sellers_list,score,comments,discription):
        self.__name = name
        self.__count = count
        self.__ID = ID    
        self.__sellers = sellers_list
        self.__score = score
        self.__comments = comments
        self.__discription = discription

        
    @property
    def name(self): 
        return self.__name

    @name.setter
    def name(self,value): 
        self.__name = value
    @property
    def count(self): 
        return self.__count
    
    @count.setter
    def count(self,count_list): 
        self.__count = count_list

    @property
    def ID(self): 
        return 'PR'+self.__ID
    
    @ID.setter
    def ID(self,code_counter): 
        self.__ID = "PR"+ code_counter
    
    @property
    def sellers(self): 
        return self.__sellers
    
    @sellers.setter
    def sellers(self,sellers_list): 
        self.__sellers = sellers_list

    @property
    def score(self): 
        return self.__score
    
    @score.setter
    def score(self,value): 
        self.__score = value

    @property
    def comments(self): 
        return self.__comments
    
    @comments.setter
    def comments(self,value): 
        self.__comments = value

    @property
    def discription(self): 
        return self.__discription
    
    @discription.setter
    def discription(self,value): 
        self.__discription = value
    
    def dict(self):
        A = {"name":self.name , "count":self.count , "ID":self.ID , "sellers":self.sellers , "score":self.score , "comments":self.comments , "discription":self.discription}
        return A

