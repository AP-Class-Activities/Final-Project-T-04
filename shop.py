class shop:
    def __init__(self, user, password, location,profit,sold_items,shopkeepers_list,customers_list):
        self.__user = user
        self.__password = password
        self.__location = location
        self.__profit = profit
        self.__sold_items = sold_items
        self.__shopkeepers_list = shopkeepers_list
        self.__customers_list = customers_list

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, new_user):
        self.__user = new_user

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_pass):
        self.__password = new_pass

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, loc):
        self.__location = loc

    @property
    def profit(self):
        return self.__profit

    @profit.setter
    def profit(self, new_profit):
        self.__profit = new_profit
