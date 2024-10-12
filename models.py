import datetime

from core.model import Model
from datetime import time


class User(Model):
    store = []

    def __init__(self, username: str, password: str, access: list = ['user']) -> None:
        self.username = username
        self.password = password
        self.access = access

    @property
    def username(self) -> str:
        return self.__username

    @username.setter
    def username(self, new_username: str) -> None:
        self.__username = new_username

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, new_password: str) -> None:
        self.__password = new_password

    @property
    def access(self) -> str:
        return self.__access

    @access.setter
    def access(self, value) -> None:
        self.__access = value

    @classmethod
    def update_access(cls, username: str, access: str) -> None:
        flag = True
        for user in cls.store:
            if user.username == username:
                if not access in user.access:
                    user.__access.append(access)
                    print(200)
                    flag = False
                    break
                else:
                    print('access  user  not in user access'.title())
                    flag = False
        if flag:
            print('username  user  not in database'.title())
        input()

    @classmethod
    def remove_access(cls, username: str, access: str) -> None:
        flag = True
        for user in cls.store:
            if user.username == username:
                assert access != 'super_user', 'no remove super user'
                user.__access.remove(access)
                print(200)
                flag = False
                break

        if flag:
            assert False,'username not iun database'



class Drug(Model):
    store = []

    def __init__(self, name: str, exp_date: str, price: float, cont: int = 0):
        self.name = name
        self.exp_date = exp_date
        self.price = price
        self.cont = cont
        self.access = ['super_user', 'doctor']

    @property
    def exp_date(self) -> str:
        return self.__exp_date

    @exp_date.setter
    def exp_date(self, date: str) -> None:
        self.__exp_date = date

    @property
    def access(self) -> list:
        return self.__access

    @access.setter
    def access(self, access_product: list) -> None:
        self.__access = access_product

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name_product: str) -> None:
        self.__name = name_product

    @property
    def cont(self) -> int:
        return self.__cont

    @cont.setter
    def cont(self, value: int) -> None:
        self.__cont = value

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        self.__price = value

    @classmethod
    def update_cont(cls, name_product: str, cont: int) -> None:
        for name_products in Drug.store:
            if name_products.name == name_product:
                name_products.cont += cont
                return
        assert False,'Drug not in database'

    @classmethod
    def change_price(cls, name_product: str, price: float) -> None:
        for name_products in Drug.store:
            if name_products.name == name_product:
                name_products.price = price
                return
        assert False,'Drug not in database'

    @classmethod
    def change_exp(cls, name_product: str, date: str) -> None:
        for name_products in Drug.store:
            if name_products.name == name_product:
                name_products.exp_date = date
                return
        assert False,'Drug not in database'

    @staticmethod
    def set_access(name_product: str, access: str) -> None:
        for name_products in Drug.store:
            if name_products.name == name_product:
                if not access in name_products.access:
                    name_products.access.append(access)
                    print(200)
                    return
        assert False ,'Drug not in database'

    @staticmethod
    def remove_access(name_product: str, access: str) -> None:
        flag = True
        for name_products in Drug.store:
            if name_products.name == name_product:
                assert access != 'super_user', 'no remove super user'
                name_products.access.remove(access)
                flag = False
                break
        if flag:
            assert False,'Drug not in database'

    @staticmethod
    def remove_product(name_product: str) -> None:
        flag = True
        for name_products in Drug.store:
            if name_products.name == name_product:
                Drug.store.remove(name_products)
                flag = False
                break
        if flag:
            assert False,'Drug not in database'


class Access(Model):
    store = []

    def __init__(self, access: str) -> None:
        self.access = access

    @property
    def access(self) -> str:
        return self.__access

    @access.setter
    def access(self, new_value) -> None:
        self.__access = new_value

    @classmethod
    def remove_access(cls, name_access: str) -> None:
        assert name_access != 'super_user', 'no remove super user'
        for access_value in cls.store:
            if name_access == access_value.access:
                cls.store.remove(access_value)
                print(200)
                break


class Sale_Drug(Model):
    store = []

    def __init__(self, user: str, zanbil: dict):
        self.username = user
        print(zanbil)
        self.box = zanbil
        self.time = datetime.date.today()

    @property
    def time(self) -> float:
        return self.__time

    @time.setter
    def time(self, value) -> None:
        self.__time = value

    @property
    def username(self) -> float:
        return self.__username

    @username.setter
    def username(self, value: float) -> None:
        self.__username = value

''''Menu'''
class Menu_Access(Model):
    store = []

    def __init__(self, name_menu: str):
        self.name = name_menu
        self.access = ['super_user', 'doctor']

    @property
    def access(self) -> list:
        return self.__access

    @access.setter
    def access(self, access_product: list) -> None:
        self.__access = access_product

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        self.__name = value

    @staticmethod
    def update_access(name_menu: str, access: str) -> None:
        for menu in Menu_Access.store:
            if name_menu == menu.name:
                if not access in menu.access:
                    menu.access.append(access)
                    print(200)
                    return
                else:
                    print('access already exists')
                    return
        print('menu not in database')

    @staticmethod
    def remove_access_menu(name_menue: str, access: str) -> None:
        for menu in Menu_Access.store:
            if menu.name == name_menue:
                assert access != 'super_user', 'no remove super user'
                menu.access.remove(access)
                print(200)
                return

        print('menu not in database')
        return
# DataBase.register(Access)
# db = DataBase("db.pickle")
# db.register(User)
# db.register(Access)
# db.load()
#
# for a in User.store:
#     print(a.username)
# d = Drug('h1', '23/12', 10000.0)
# print(d.name, d.price, d.cont, d.access, d.exp_date)
# d.change_price('h1', 300000.0)
# print(d.name, d.price, d.cont, d.access, d.exp_date)
# d.update_cont('h1', 3000)
# print(d.name, d.price, d.cont, d.access, d.exp_date)
# d.set_access('h1', 'user22')
# print(d.name, d.price, d.cont, d.access, d.exp_date)
# d.remove_access('h1', 'cashier')
# print(d.name, d.price, d.cont, d.access, d.exp_date)
# d.change_exp('h1','12/12')
# print(d.name, d.price, d.cont, d.access, d.exp_date)
