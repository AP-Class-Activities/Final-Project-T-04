class Shopkeeper:
    def __init__(self, name, last_name, user, password, product, location, score, order, wallet, sell, email, profit, ID):
        self.__name = name
        self.__last = last_name
        self.__user = user
        self.__password = password
        self.__product = product
        self.__location = location
        self.__score = score
        self.__order = order
        self.__wallet = wallet
        self.__sell = sell
        self.__email = email
        self.__profit = profit
        self.__ID = ID

    @property
    def name(self): 
        return self.__name
    
    @name.setter
    def name(self,value): 
        self.__name = value

    @property
    def last(self): 
        return self.__last
    
    @last.setter
    def last(self,value): 
        self.__last = value

    @property
    def user(self): 
        return self.__user
    
    @user.setter
    def user(self,value): 
        self.__user = value

    @property
    def password(self): 
        return self.__password

    @password.setter
    def password(self,value): 
        self.__password = value

    @property
    def product(self): 
        return self.__product

    @product.setter
    def product(self,product_list): 
        self.__product = product_list

    @property
    def location(self): 
        return self.__location
    
    @location.setter
    def location(self,value): 
        self.__location = value
    @property
    def score(self): 
        return self.__score
    
    @score.setter
    def score(self,value): 
        self.__score = value    

    @property
    def order(self): 
        return self.__order

    @order.setter
    def order(self,order_list): 
        self.__order = order_list

    @property
    def wallet(self): 
        return self.__wallet

    @wallet.setter
    def wallet(self,wallet): 
        self.__wallet = wallet

    @property
    def sell(self): 
        return self.__sell

    @sell.setter
    def sell(self,sell_list): 
        self.__sell = sell_list
 
    @property
    def email(self): 
        return self.__email

    @email.setter
    def wallet(self,value): 
        self.__email = value

    @property
    def profit(self): 
        return self.__profit

    @profit.setter
    def profit(self,profit_list): 
        self.__profit = profit_list
    

    @property
    def ID(self): 
        return "SL"+ self.__ID

    @ID.setter
    def ID(self,code): 
        self.__ID = "SL" + code

    def dict(self):
        A = {"name":self.name ,"last name":self.last , "user":self.user , "password":self.password, "email":self.email,"wallet":self.wallet , "products":self.product , "location":self.location , "sold items":self.sell , "score":self.score , "ID":self.ID,"orders":self.orde,"profit":self.profit}
        return A