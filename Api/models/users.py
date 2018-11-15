user_lists = []


class Users:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def create_users(self):
        user = {
            'user_id': len(user_lists) + 1,
            'username': self.username,
            'password': self.password
        }
        user_lists.append(user)
        return user_lists

    def login_user(self):
        for user in user_lists:
            if user['username'] == self.username and user['password'] == self.password:
                return user['user_id']
