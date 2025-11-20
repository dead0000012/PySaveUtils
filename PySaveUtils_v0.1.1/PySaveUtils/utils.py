import secrets

class PySaveUtils:
    def __init__(self, input_1=None, input_2=None, hash_long=8):
        self.input_1 = input_1
        self.input_2 = input_2
        self.hash_long = hash_long

    ## Генератор случайного цвета ##
    @staticmethod
    def random_color_gen():
        """Генерирует случайный RGB-цвет в виде списка [R, G, B]."""
        return [secrets.randbits(8) for _ in range(3)]

    ## Проверка пользовательского ввода ##
    @staticmethod
    def input_checker(input_1, input_2):
        """Проверяет, совпадают ли пароли и длина не меньше 8 символов."""
        try:
            if len(input_1) >= 8 and len(input_2) >= 8 and secrets.compare_digest(input_1, input_2):
                return True
            return False
        except TypeError:
            print("Ошибка: параметры должны быть строками")
            return False

    ## Генератор YouTube URL ##
    @staticmethod
    def youtube_url_gen():
        """Создаёт случайный YouTube-идентификатор (11 символов)."""
        return secrets.token_urlsafe(8)[:11]

    ## Генератор хэша ##
    @staticmethod
    def hash_gen(hash_long):
        """Создаёт случайный хэш заданной длины."""
        try:
            return secrets.token_hex((hash_long + 1) // 2)[:hash_long]
        except ValueError:
            print("Ошибка: длина хэша должна быть положительным числом")
            return None