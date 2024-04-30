import User


class UserService:
    def __init__(self):
        self.user = []

    def edit(self, id: int,new_user: User.User):
        self.user[id] = new_user

    def List(self):
        for i, user in enumerate(self.user):
            print(f"User {i}: {user.name}, {user.phone}, {user.email}")
    def Add(self, user: User):
        self.user.append(user)