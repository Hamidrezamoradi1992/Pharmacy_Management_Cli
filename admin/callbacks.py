from time import strptime

from core.validation import *
from models import User, Access, Drug, Sale_Drug, Menu_Access
from getpass import getpass
from core.state import Auth
from core.utils import safe

users = None


@safe
def login(route):
    username = input("Please enter username: ").strip().lower()
    assert username, "Username should not be empty !"

    password = getpass("Please enter password: ")
    assert password, "Password should not be empty !"

    for user in User.store:
        if user.password == password and user.username == username:
            Auth.login_status = True
            Auth.user_register.clear()
            Auth.user_register.extend(user.access)
            Auth.user_aconite = str(user.username)
            print(f"\n\nWelcome '{user.username.title()}' ⭐ ")

            # sleep(4)
            print(user.username, user.access)

            break
    else:
        raise ValueError("Username or password invalid !")


def logout(route):
    print("In Logout Callbacks")
    Auth.login_status = False
    Auth.zanbil = False


'''User '''


@safe
def register(route):
    username = input("Please enter username: ").strip().lower()
    assert username, "Username should not be empty !"

    password = getpass("Please enter password: ")
    assert password, "Password should not be empty !"

    confirm_password = getpass("Please re-enter password: ")
    assert confirm_password, "Confirm Password should not be empty !"
    assert confirm_password == password, "Confirm password and password doesn't match !"
    validate_username(username)
    validate_password(password)
    User(username, password)

    print("Register Successful ✅ ")


@safe
def update_access_user(route):
    for user in User.store:
        print(f' name username: {user.username}')
    username = input("\n\nPlease enter username: ").strip().lower()
    assert username, "Username should not be empty !"
    for acc in Access.store:
        print(f'Access: {acc.access}')
    else:
        pass
    access = input("\n\nPlease enter access: ").strip().lower()
    valid_input_access(access)
    User.update_access(username, access)


@safe
def remove_access_user(route):
    c = None
    for user in User.store:
        print(f' name username: {user.username}')
    username = input("\n\nPlease enter username: ").strip().lower()
    assert username, "Username should not be empty !"
    for user in User.store:
        if username == user.username:
            print(f'user Access: {(c := user.access)}')

    access = input("\n\nPlease enter access: ").strip().lower()
    assert access, "Access should not be empty !"
    if access in c:
        User.remove_access(username, access)
    else:
        assert not access, "Access  not  in access user !"


@safe
def box_access_user(route):
    flag=True
    for user in User.store:
        print(f'name: {user.username}')
    username = input("\n\nPlease enter username: ").strip().lower()
    assert username, "Username should not be empty !"
    for user in User.store:
        if username == user.username:
            for box1 in Sale_Drug.store:
                if username == box1.username:
                    flag=False
                    print(f'''
                           username: {box1.username}
                           date : {box1.time}
                           box : {box1.box}
                     
                           ''')
    if flag:
        print('no payment')

'''Access'''


@safe
def set_access(route):
    for acc in Access.store:
        print(f'Access name:{acc.access}')
    else:
        pass
    access = input('''
    please enter new access 
    ''')
    validate_access(access)
    Access(access)


@safe
def remove_access(route):
    for acc in Access.store:
        print(f'Access name:{acc.access}')
    else:
        pass
    name = input('''
    please enter new access 
    ''')
    valid_input_access(name)
    Access.remove_access(name)


'''Drug'''


@safe
def Add_drug(route):
    name_product = input("Please enter name product: ").strip().lower()
    assert name_product, "Username should not be empty !"
    exp = input("Please enter exp date YYYY/MM: ")
    assert exp, "exp date should not be empty !"
    strptime(exp, '%Y/%m')
    price = float(input("Please enter exp date price flote: "))
    assert price, "price should not be empty !"
    cont = int(input("Please enter cont: "))
    assert cont, "cont should not be empty !"
    validate_name_product(name_product)
    Drug(name_product, exp, price, cont)


@safe
def Remove_drug(route):
    for drug in Drug.store:
        print(f"name drug: {drug.name}")
    name_product = input("\n\nPlease enter name product: ").strip().lower()
    assert name_product, "Username should not be empty !"

    Drug.remove_product(name_product)


@safe
def Update_drug_cont(route):
    for drug in Drug.store:
        print(f'Drug name: {drug.name}')
    name_products = input("\n\nPlease enter name product: ").strip().lower()
    assert name_products, "Username should not be empty !"
    cont = int(input("Please enter cont: "))
    assert cont, "cont should not be empty !"
    Drug.update_cont(name_products, cont)


@safe
def change_drug_price(route):
    for drug in Drug.store:
        print(f'Drug name: {drug.name}')
    name_products = input("\n\nPlease enter name product: ").strip().lower()
    assert name_products, "Username should not be empty !"
    price = float(input("Please enter exp date price flute: "))
    assert price, "price should not be empty !"
    Drug.change_price(name_products, price)


@safe
def change_drug_exp(route):
    for drug in Drug.store:
        print(f'Drug name: {drug.name}')
    name_products = input("\n\nPlease enter name product: ").strip().lower()
    assert name_products, "Username should not be empty !"
    exp = input("Please enter exp date YYYY/MM: ")
    assert exp, "exp date should not be empty !"
    strptime(exp, '%Y/%m')
    Drug.change_exp(name_products, exp)


@safe
def update_access_drug(route):
    for drug in Drug.store:
        print(f'Drug name: {drug.name} ->> Access Drug: {drug.access}')
    name_drug = input("\n\nPlease enter name Drug: ").strip().lower()
    assert name_drug, "Username should not be empty !"
    for acc in Access.store:

        print(f'Access Name: {acc.access}')
    else:
        pass
    access = input("\n\nPlease enter access: ").strip().lower()
    valid_input_access(access)
    Drug.set_access(name_drug, access)


@safe
def remove_access_drug(route):
    flag=True
    for drug in Drug.store:
        print(f'Drug name: {drug.name} ')
    name_drug = input("\n\nPlease enter name drug: ").strip().lower()
    assert name_drug, "name drug should not be empty !"
    for drug in Drug.store:
        if name_drug == drug.name:
            print(f'Drug Access: {drug.access}')
            flag=False
    if flag:
        assert False, 'name drug error'

    access = input("\n\nPlease enter access: ").strip().lower()
    valid_input_access(access)
    Drug.remove_access(name_drug, access)


@safe
def Drug_print(route):
    for drug in Drug.store:
        print(
            f'\n name: {drug.name} -- price: {drug.price}-- cont: {drug.cont} -- exp: {drug.exp_date}-- access: {drug.access}')


'''SHOP'''

zanbile = {}


@safe
def Buy_Shop(rout):
    drugs = {}
    for drug in Drug.store:
        if any([True if x in Auth.user_register else False for x in drug.access]) and drug.cont > 0:
            print(f'\n\n name: {drug.name} -- price: {drug.price}-- cont: {drug.cont} -- exp: {drug.exp_date}')
            drugs[drug.name] = [drug.price, drug.cont]
        elif 'user' in drug.access and drug.cont > 0:
            print(drug.name)
            print(f'\n name: {drug.name} -- price: {drug.price}-- cont: {drug.cont} -- exp: {drug.exp_date}')
            drugs[drug.name] = [drug.price, drug.cont]

    while True:

        name_drug = input("\n\nPlease accept Drug: ").strip().lower()
        cont = int(input("\n\nPlease accept Drug cont: ").strip().lower())
        if name_drug in drugs.keys():
            if cont <= drugs[name_drug][1]:
                zanbile.setdefault(name_drug, [drugs[name_drug][0], cont, (drugs[name_drug][0] * cont)])
                Auth.zanbil = True
            else:
                assert False, ('cont is not valid3')
        else:
            assert False, ('Drug is not valid3')
        print(zanbile)
        y = input('''
        exit
        enter continue 
         \n
         ->''').strip().lower()
        if y[0] == 'e':
            break


@safe
def Payment(route):
    d = 0
    for i in zanbile.keys():
        print(f'{i}:price: {zanbile[i][0]} --- cont: {zanbile[i][1]} --- total: {(c := zanbile[i][2])}')
        d += c
    print(f'''
      -----------------------------
      total:{d}
      ''')
    if (cmd := input("\nyou are payment ? [Y|n] ").strip().lower()) and cmd[0] == "n":
        return
    else:
        for drud in zanbile.keys():
            for drug in Drug.store:
                if drud == drug.name:
                    drug.update_cont(drud, (zanbile[i][1] * -1))
        copy_box = zanbile.copy()
        Sale_Drug(Auth.user_aconite, copy_box)
        zanbile.clear()


'''Menu'''


@safe
def set_access_menu(route):
    access = input('''
    please enter name menu
    ''').strip().lower()
    access1 = access.split()
    access = "_".join(access1)
    Menu_Access(access)

@safe
def add_access_menu(route):
    for menu in Menu_Access.store:
        print(f'Name Menu: {menu.name}')
    name_menu = input("\n\nPlease enter name menu: ").strip().lower()
    assert name_menu, "Username should not be empty !"
    for acc in Access.store:
        print(f'Access Name: {acc.access}', end='  <<-->>  ')
    else:
        pass
    access = input("\n\nPlease enter access: ").strip().lower()
    valid_input_access(access)
    Menu_Access.update_access(name_menu,access)
@safe
def remove_access_menu(route):
    flag=True
    for menu in Menu_Access.store:
        print(f'Name Menu: {menu.name}')
    name_menu = input("\n\nPlease enter name menu: ").strip().lower()
    assert name_menu, "name drug should not be empty !"
    for menu in Menu_Access.store:
        if name_menu == menu.name:
            print(f'Manu Access{menu.access}')
            flag=False
    if flag:
        assert False, 'name drug error'
    name_access = input("\n\nPlease enter name access: ").strip().lower()
    assert name_menu, "name drug should not be empty !"
    Menu_Access.remove_access_menu(name_menu,name_access)