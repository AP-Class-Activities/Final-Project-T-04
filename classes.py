class customer:
    def __init__(self, user, password, wallet, cart, favourite, bought_items, score, id):
        self.__user = user
        self.__password = password
        self.__wallet = wallet
        self.__cart = cart
        self.__favourite = favourite
        self.__bought_items = bought_items
        self.__score = score
        self.__id = id

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