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

    @property
    def sold_items(self):
        return self.__sold_items

    @sold_items.setter
    def sold_items(self, new_sold_list):
        self.__sold_items = new_sold_list

    @property
    def shopkeepers_list(self):
        return self.__shopkeepers_list

    @shopkeepers_list.setter
    def shopkeepers_list(self, new_shopkeepers):
        self.__shopkeepers_list = new_shopkeepers

    @property
    def customers_list(self):
        return self.__customers_list

    @customers_list.setter
    def customers_list(self, new_customers):
        self.__customers_list = new_customers

    def __str__(self):
        return 'user: {}  password:{}  location: {}  profit: {}  sold_items: {}  shopkeepers_list: {}  customers_list: {}'.format(
            self.user, self.password, self.location, self.profit, self.sold_items, self.shopkeepers_list,
            self.customers_list)
