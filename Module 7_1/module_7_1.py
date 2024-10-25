class Product:

    def __init__(self,name,weight,category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:

    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        f = open(self.__file_name,'r')
        list_products = f.read()
        f.close()
        return list_products

    def add(self,*products):
        for product in products:
            file = open(self.__file_name, 'a')
            list_products = self.get_products()
            if product.__str__() not in list_products:
                file.write(f'{product}\n')
                file.close()
            else:
                print(f'Продукт {product.name} уже есть в магазине')
                file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2) # __str__
s1.add(p1,p2,p2)
s1.add(p3)
print(s1.get_products())