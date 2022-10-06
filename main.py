class Product:
    def __init__(self, name="", price=0):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price > 0:
            self.__price = price

    def print_Info(self):
        print("Kauba nimetus:", self.__name, " hind=", self.__price)


class ProductList:
    def __init__(self, plist=list()):
        self.__pList = plist

    def get_ProductList(self):
        return self.__pList

    def set_ProductList(self, plist):
        self.__pList = plist

    def addProduct(self, product):
        self.__pList.append(product)

    def readFromFile(self, filename):
        print("Andmed failist:", filename)
        with open(filename, "r") as file:
            line = file.readline()
            while (line):
                plist = line.split(",")
                p = Product(plist[0], float(plist[1]))
                self.addProduct(p)
                line = file.readline()

    def printInfo(self):
        for p in self.__pList:
            p.print_Info()

    def findByName(self, name):
        print("Otsing nimetuse järgi:", name)
        for p in self.__pList:
            if p.name == name:
                p.print_Info()

    def findByPrice(self, sprice, fprice):
        print("Otsing hinna järgi:", sprice, " kuni ", fprice)
        for p in self.__pList:
            if p.price >= sprice and p.price <= fprice:
                p.print_Info()



plist = ProductList()  # пустой список
plist.readFromFile("product.txt")  # чтение файла и формирование списка

while (True):
    print("1-kuva üldinfo")
    print("2-otsing nime järgi")
    print("3-otsing hinna järgi")
    print("0-välja")
    menuu = int(input("Sisesta menüü number:"))
    if menuu == 1:
        plist.printInfo()
    elif menuu == 2:
        otsi = input("Sisesta kauba nimetus")
        plist.findByName(otsi)
    elif menuu == 3:
        otsiA = float(input("Sisesta kauba alghind"))
        otsiL = float(input("Sisesta kauba lõpphind"))
        plist.findByPrice(otsiA, otsiL)
    elif menuu == 0:
        break