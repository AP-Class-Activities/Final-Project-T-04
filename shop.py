class shop:
    def __init__(self, name, products, location, shop_id, add, delete, destination, comission):
        self.__name = name
        self.__products = products
        self.__location = location
        self.__shop_id = shop_id
        self.__add = add
        self.__delete = delete
        self.__destination = destination
        self.__comission = comission

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def products(self):
        return self.__products

    @products.setter
    def products(self, products_list):
        self.__products = products_list

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location):
        self.__location = location

    @property
    def shop_id(self):
        return self.__shop_id

    @shop_id.setter
    def code(self, shop_id):
        self.__shop_id = shop_id

    @property
    def add(self):
        return self.__add

    @add.setter
    def add(self, add):
        self.__add = add

    @property
    def delete(self):
        return self.__delete

    @delete.setter
    def delete(self, delete):
        self.__delete = delete

    @property
    def destination(self):
        return self.__destination

    @destination.setter
    def destination(self, destination):
        self.__destination = destination

    @property
    def comission(self):
        return self.__comission

    @comission.setter
    def comission(self, comission):
        self.__comission = comission

    def __str__(self):
        return 'name: {}   products: {} location:{} shop_id:{}  add:{}  delete:{}  destination:{}  comission:{}' \
            .format(self.name, self.products, self.location, self.shop_id, self.add, self.delete, self.destination,
                    self.comission)
