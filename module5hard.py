import time


class User:
    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname    # Имя пользователя
        self.password = self.hash_password(password)    # Пароль пользователя
        self.age = age  # Возраст пользователя

    # Хеширование пароля
    @staticmethod
    def hash_password(password):
        return hash(password)

    def __str__(self):
        return f'Текущий пользователь: {self.nickname}'


class Video:
    def __init__(self, title: str, duration: int, adult_mode=False):
        self.title = title  # Название видео
        self.duration = duration    # Продолжительность видео
        self.time_now = 0   # Время остановки видео (по умолчанию 0)
        self.adult_mode = adult_mode    # Возрастное ограничение


class UrTube:
    def __init__(self):
        self.users = []     # Список зарегистрированных пользователей
        self.videos = []    # Список загруженных видео
        self.current_user = None    # Текущий пользователь (по умолчанию не определен)

    # Метод смены пользователя по имени и паролю
    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == password:
                self.current_user = user
                print(f'Пользователь {nickname} вошел в систему')
                return
        print("Неверные логин или пароль")

    # Метод сброса текущего пользователя
    def log_out(self):
        self.current_user = None
        print("Вы вышли из аккаунта")

    # Метод регистрации нового пользователя (выполнение входа в систему)
    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user

    # Метод загрузки нового видео
    def add(self, *videos):
        for video in videos:
            if video.title not in [v.title for v in self.videos]:
                self.videos.append(video)

    # Метод поиска видео по ключевым словам в списке загруженных видео
    def get_videos(self, search_word):
        search_word = search_word.lower()
        matching_videos = [video.title for video in self.videos if search_word in video.title.lower()]
        return matching_videos

    # Метод просмотра найденного видео и возрастного ограничения
    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return

                for second in range(video.duration):
                    video.time_now = second
                    print(f'{second + 1}')
                    time.sleep(1)  # пауза на 1 секунду

                print("Конец видео")
                return

        """print(f'Видео "{title}" не найдено')"""


if __name__ == "__main__":
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
