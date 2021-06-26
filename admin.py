class admin:
    def __init__(self, name, last_name, user, password, location, email, ListOfCustomers, ListOfShopkeepers):
        self.__name = name
        self.__last = last_name
        self.__user = user
        self.__password = password
        self.__location = location
        self.__email = email
        self.__customers = ListOfCustomers
        self.__shopkeepers = ListOfShopkeepers

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
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def customers(self):
        return self.__customers

    @customers.setter
    def customers(self, value):
        self.__customers = value

    @property
    def shopkeepers(self):
        return self.__shopkeepers

    @shopkeepers.setter
    def shopkeepers(self, value):
        self.__shopkeepers = value

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self):
        self.__location = "Sarvestan St. , Elahieh , Tehran , Iran"

    def dict(self):
        A = {"name":self.name ,"last name":self.last , "user":self.user , "password":self.password , "email":self.email , "Shop location": self.location}
        return A