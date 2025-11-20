"""Короткий API `PySaveUtils`."""

from __future__ import annotations

from .__about__ import __version__
from .core import (
    PySaveUtils as _ModernPySaveUtils,
    generate_hash,
    generate_uuid,
    generate_youtube_id,
    hex_color,
    random_color,
    validate_passwords,
)
from .exceptions import HashLengthError, PasswordValidationError, PySaveUtilsError
from .utils import PySaveUtils as LegacyPySaveUtils

PySaveUtils = _ModernPySaveUtils

__all__ = [
    "__version__",
    "PySaveUtils",
    "LegacyPySaveUtils",
    "random_color",
    "hex_color",
    "validate_passwords",
    "generate_youtube_id",
    "generate_hash",
    "generate_uuid",
    "PySaveUtilsError",
    "PasswordValidationError",
    "HashLengthError",
]
