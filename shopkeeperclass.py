class Shopkeeper:
    def __init__(self, user, password, product, location, score, order, wallet, sell, email, profit, income ,ID,cart):
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
        self.__income = income
        self.__cart = cart

    @property
    def income(self): 
        return self.__income
    
    @income.setter
    def income(self,value): 
        self.__income = value
    
    @property
    def cart(self): 
        return self.__cart
    
    @cart.setter
    def cart(self,value): 
        self.__cart = value

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
    def email(self,value): 
        self.__email = value

    @property
    def profit(self): 
        return self.__profit

    @profit.setter
    def profit(self,profit_list): 
        self.__profit = profit_list
    

    @property
    def ID(self): 
        return "SL"+self.__ID

    @ID.setter
    def ID(self,code): 
        self.__ID = "SL"+code
    
    @property
    def status(self): 
        return self.__status
    
    @status.setter
    def status(self,value): 
        self.__status = value

    def dict(self):
        A = {"user":self.user , "password":self.password, "email":self.email,"wallet":self.wallet , "products":self.product , "location":self.location , "sold items":self.sell , "score":self.score , "ID":self.ID,"orders":self.order,"profit":self.profit, "cart":self.cart}
        return A