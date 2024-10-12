from models import User, Access, Drug


def validate_username(username: str) -> None:
    assert isinstance(username, str) and len(username) >= 4, "Username must be str type and length >= 4"
    for user in User.store:
        if hasattr(user, "username"):
            assert user.username != username, "Username already exists !"


def validate_password(password: str) -> None:
    assert isinstance(password, str) and len(password) >= 4, "Password must be str type and length >= 4"


def validate_access(access: str) -> None:
    assert isinstance(access, str) and len(access) >= 2, "Access must be str type and length >= 4"
    for acess in Access.store:
        if hasattr(acess, "access"):
            assert acess.access != access, "Access already exists !"


def validate_name_product(name: str) -> None:
    assert isinstance(name, str) and len(name) >= 2, "Access must be str type and length >= 2"
    for drug in Drug.store:
        if hasattr(drug, "name"):
            assert drug.access != name, "Access already exists !"

def valid_input_access(name:str)->None:
    flag=True
    assert isinstance(name, str) and len(name) >= 2, "Access must be str type and length >= 2"
    for access1 in Access.store:
        if name == access1.access:
            flag=False
            break
    if flag:
        assert False ,'access not in data base'.title()