class Database:
    def __init__(self):
        self.data = {}
    def add_user(self, username, password):
        self.data[username] = password

class User:
    '''
    Класс пользователя, содержащий атрибуты: логинб пароль
    '''
    def __init__(self, username, password, password_confirm):
        def check_password(password):
            password_is_correct = True
            if len(password) >= 8 and (not password.isalpha()) and (password.lower() != password):
                password_is_correct = True
            else:
                password_is_correct = False
            return password_is_correct

        self.username = username
        while not check_password(password):
            password = input('Password length should be at least 8 symbols,contain ony num and big letter, \nEnter new password: ')
        while password_confirm != password:
            password_confirm = input('Confirmation failed, please try again: ')

        self.password = password



if __name__ == '__main__':
    database = Database()
    while True:
        choice = input('Greetings! Choose action: \n 1 - Entry\n 2 - Register\n')
        if choice == 1:
            login = input('Login: ')
            password = input('Password: ')
            if login in database:
                if password == database.data[login]:
                    print(f'Entry is ok{login}')
                else:
                    print("Invalid password")

            else:
                print('User is not defined')
        if choice == 2:
            user = User(input('Login: '), password := input('Password: '), password2 := input('Confirm password: '))
            if password != password2:
                continue
        database.add_user(user.username, user.password)
        print(database.data)