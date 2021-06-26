class customer:
    def __init__(self, name, last_name, user, password, email, wallet, cart, favourite, bought_items, score, Id):
        self.__name = name
        self.__last = last_name
        self.__user = user
        self.__password = password
        self.__email = email
        self.__wallet = wallet
        self.__cart = cart
        self.__favourite = favourite
        self.__bought_items = bought_items
        self.__score = score
        self.__Id = Id
        
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value
        
    @property
    def last(self):
        return self.__last

    @last.setter
    def last(self, value):
        self.__last = value
    
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
    def wallet(self):
        return self.__wallet

    @wallet.setter
    def wallet(self, value):
        self.__wallet = value

    @property
    def cart(self):
        return self.__cart

    @cart.setter
    def cart(self, cart_list):
        self.__cart = cart_list

    @property
    def favourite(self):
        return self.__favourite

    @favourite.setter
    def favourite(self, fav_list):
        self.__favourite = fav_list

    @property
    def bought_items(self):
        return self.__bought_items

    @bought_items.setter
    def bought_items(self, bought_list):
        self.__bought_items = bought_list

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, new_score):
        self.__score = new_score

    @property
    def ID(self):
        return "CU"+self.__Id

    @ID.setter
    def ID(self, customer_counter):
        self.__Id = "CU"+customer_counter
        
    @property
    def email(self):
        return self.__email

    @email.setter
    def ID(self, value):
        self.__email = value
        
    def dict(self):
        A = {"name":self.name ,"last name":self.last , "user":self.user , "password":self.password , "email":self.email , "wallet":self.wallet , "cart":self.cart , "favourite":self.favourite , "bought items":self.bought_items , "score":self.score , "ID":self.ID}
        return A
#A = customer("Hamed","Teymouri","XviL","ha113","htm133@gmail.com",10000,["xbox one" , "ps4"],["ps5"],["watch"],60,"213245")
#B = A.dict()
