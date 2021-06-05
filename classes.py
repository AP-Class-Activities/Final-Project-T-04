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