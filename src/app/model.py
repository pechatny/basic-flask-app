class User(object):

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def show_user(self):
        return "Login: s%, Password: s%" % (self.login, self.password)