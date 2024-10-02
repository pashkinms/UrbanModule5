from time import sleep

class User:
    nickname = str
    password = int
    age = int

    def __init__(self, nickname: str, password: int, age: int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
    def __str__(self):
        return self.nickname
class Video:
    title = str
    duration = int
    time_now = 0
    adult_mode = False

    def __init__(self, title: str, duration: int, adult_mode= False):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode


class UrTube:
    users = []
    videos = []
    current_user = None
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        user_exists = False
        for i in self.users:
            if i.nickname == nickname and i.password == hash(password):
                self.current_user = i
                user_exists = True
                break
        if not user_exists:
            print("Invalid login or password")

    def register(self, nickname, password, age):
        new_user = True
        for i in self.users:
            if i.nickname == nickname:
                new_user = False
        if new_user:
            self.users.append(User(nickname, hash(password), age))
            self.current_user = self.users[-1]
        else:
            print(f'User {nickname} already exists.')

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for i in args:
            does_exist = False
            for k in self.videos:
                if k.title == i.title:
                    does_exist = True
            if not does_exist:
                self.videos.append(i)

    def get_videos(self, search_word):
        found_list =[]
        for i in self.videos:
            if search_word.casefold() in i.title.casefold():
                found_list.append(i.title)
        return found_list

    def watch_video(self, title):
        if self.current_user == None:
            print("Log in to watch video")
            return
        for i in self.videos:
            if title == i.title:
                if i.adult_mode and self.current_user.age < 18:
                    print("Your age is lower 18 please live this page")
                    return
                else:
                    while i.time_now <= i.duration:
                        print(i.time_now, end=' ')
                        i.time_now += 1
                    print("The end of video")

if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')

    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')