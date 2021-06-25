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
        return "CU"+self.__id

    @ID.setter
    def ID(self, customer_counter):
        self.__id = "CU"+customer_counter
        
    @property
    def email(self):
        return self.__email

    @email.setter
    def ID(self, value):
        self.__email = value
        
    def __str__(self):
        return '{"name":"%b","last name":"%b","user":"%b","password":"%b","email":"%b","wallet":%i,"cart":[%b],"favourites":[%b],"bought_items":[%b],"score":%i,"ID":"%b"}'\
        .format(self.name, self.last, self.user, self.password, self.email, self.wallet, self.cart, self.favourite, self.bought_items, self.score, self.ID)
