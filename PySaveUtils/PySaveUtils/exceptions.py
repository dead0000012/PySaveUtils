"""Исключения `pysaveutils`."""


class PySaveUtilsError(Exception):
    """База ошибок."""


class PasswordValidationError(PySaveUtilsError):
    """Пароль невалиден."""


class HashLengthError(PySaveUtilsError):
    """Неверная длина хэша."""

