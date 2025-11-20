"""Новая реализация `pysaveutils`."""

from __future__ import annotations

from dataclasses import dataclass
import secrets
import string
import uuid
from typing import Optional, Tuple

from .exceptions import HashLengthError, PasswordValidationError

RGBColor = Tuple[int, int, int]
YOUTUBE_ID_LENGTH = 11
DEFAULT_PASSWORD_LENGTH = 8
_HEX_ALPHABET = "0123456789ABCDEF"


@dataclass
class PySaveUtils:
    """Высокоуровневый интерфейс."""

    min_password_length: int = DEFAULT_PASSWORD_LENGTH
    youtube_id_length: int = YOUTUBE_ID_LENGTH

    def __post_init__(self) -> None:
        if self.min_password_length < 1:
            raise ValueError("`min_password_length` должен быть положительным числом.")
        if self.youtube_id_length < 1:
            raise ValueError("`youtube_id_length` должен быть положительным числом.")

    @staticmethod
    def random_color() -> RGBColor:
        """Случайный RGB."""
        return tuple(secrets.randbelow(256) for _ in range(3))  # type: ignore[return-value]

    @staticmethod
    def hex_color() -> str:
        """HEX-цвет."""
        return "#" + "".join(secrets.choice(_HEX_ALPHABET) for _ in range(6))

    @staticmethod
    def uuid() -> str:
        """UUID4."""
        return str(uuid.uuid4())

    def validate_passwords(
        self,
        password: Optional[str],
        confirmation: Optional[str],
        *,
        min_length: Optional[int] = None,
        raise_on_error: bool = False,
    ) -> bool:
        """Проверка паролей."""

        target_length = min_length or self.min_password_length
        try:
            if not isinstance(password, str) or not isinstance(confirmation, str):
                raise PasswordValidationError("Пароль и подтверждение должны быть строками.")

            if len(password) < target_length or len(confirmation) < target_length:
                raise PasswordValidationError(
                    f"Пароль должен содержать минимум {target_length} символов."
                )

            if not secrets.compare_digest(password, confirmation):
                raise PasswordValidationError("Пароли не совпадают.")

        except PasswordValidationError:
            if raise_on_error:
                raise
            return False

        return True

    def youtube_id(self, *, length: Optional[int] = None) -> str:
        """YouTube ID."""
        target_length = length or self.youtube_id_length
        if target_length < 1:
            raise ValueError("Длина идентификатора должна быть положительной.")

        alphabet = string.ascii_letters + string.digits + "-_"
        return "".join(secrets.choice(alphabet) for _ in range(target_length))

    @staticmethod
    def hash(length: int = 16) -> str:
        """Хэш произвольной длины."""
        if length < 1:
            raise HashLengthError("Длина хэша должна быть положительной.")

        return secrets.token_hex((length + 1) // 2)[:length]


_DEFAULT = PySaveUtils()


def random_color() -> RGBColor:
    """Публичный генератор цвета."""
    return _DEFAULT.random_color()


def hex_color() -> str:
    """Публичный HEX-цвет."""
    return _DEFAULT.hex_color()


def validate_passwords(
    password: Optional[str],
    confirmation: Optional[str],
    *,
    min_length: Optional[int] = None,
    raise_on_error: bool = False,
) -> bool:
    """Публичная проверка паролей."""
    return _DEFAULT.validate_passwords(
        password,
        confirmation,
        min_length=min_length,
        raise_on_error=raise_on_error,
    )


def generate_youtube_id(*, length: Optional[int] = None) -> str:
    """Публичный YouTube ID."""
    return _DEFAULT.youtube_id(length=length)


def generate_hash(length: int = 16) -> str:
    """Публичный хэш."""
    return PySaveUtils.hash(length)


def generate_uuid() -> str:
    """Публичный UUID."""
    return _DEFAULT.uuid()

