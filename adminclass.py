class admin:
    def __init__(self, user, password, location, email, ListOfCustomers, ListOfShopkeepers):
        self.__user = user
        self.__password = password
        self.__location = location
        self.__email = email
        self.__customers = ListOfCustomers
        self.__shopkeepers = ListOfShopkeepers

    
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
        A = {"user":self.user , "password":self.password , "email":self.email , "Shop location": self.location,"shopkeepers":self.shopkeepers,"customers":self.customers}
        return A
