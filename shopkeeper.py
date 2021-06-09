class Shopkeeper:
    def __init__(self, user, password, product, location, score, order, wallet, sell, credit, rate, profit, code):
        self.__user = user
        self.__password = password
        self.__product = product
        self.__location = location
        self.__score = score
        self.__order = order
        self.__wallet = wallet
        self.__sell = sell
        self.__credit = credit
        self.__rate = rate
        self.__profit = profit
        self.__code = code
    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, value):
        self.__user = value
    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
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
    def credit(self): 
        return self.__credit

    @credit.setter
    def credit(self,credit_list): 
        self.__credit = credit_list        