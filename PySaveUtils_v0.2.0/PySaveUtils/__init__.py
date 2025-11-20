"""Короткий API `pysaveutils`."""

from __future__ import annotations

from .__about__ import __version__
from .core import (
    PySaveUtils,
    generate_hash,
    generate_youtube_id,
    random_color,
    validate_passwords,
)
from .exceptions import HashLengthError, PasswordValidationError, PySaveUtilsError

__all__ = [
    "__version__",
    "PySaveUtils",
    "random_color",
    "validate_passwords",
    "generate_youtube_id",
    "generate_hash",
    "PySaveUtilsError",
    "PasswordValidationError",
    "HashLengthError",
]
from .utils import PySaveUtils

__all__ = ["PySaveUtils"]
