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
        self.__favourite = fav_lists
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
