USERS = [
    {
        "id": 1,
        "name": "kun",
        "phone": "3996",
        "password": "kun"
    },
    {
        "id": 2,
        "name": "rui",
        "phone": "2078",
        "password": "rui"
    }
]


def get_user_by_name(name):
    for user in USERS:
        if user.get('name') == name:
            return user

    return None


def authenticate_user(name, password):
    for user in USERS:
        if user.get('name') == name and user.get('password') == password:
            return user

    return None
