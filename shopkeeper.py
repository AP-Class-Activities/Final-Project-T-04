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
