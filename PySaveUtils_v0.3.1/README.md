# PySaveUtils

Обновлённая структура репозитория содержит исходный пакет `PySaveUtils`
и современную копию `pysaveutils` с проработанным API, типами и
исключениями.

## 🚀 Установка

```bash
pip install PySaveUtils
```

## 📦 Быстрый старт с новым API

```python
from PySaveUtils import (
    PySaveUtils,
    generate_hash,
    generate_uuid,
    generate_youtube_id,
    random_color,
    hex_color,
    validate_passwords,
)

utils = PySaveUtils(min_password_length=10)

rgb = random_color()
hex_value = hex_color()
youtube_id = generate_youtube_id()
hash_value = generate_hash(32)
uid = generate_uuid()
is_valid = validate_passwords("Sup3rPass!", "Sup3rPass!")
```

## 🧩 Доступные функции

- `random_color()` и `hex_color()` — RGB и HEX-цвета.
- `validate_passwords()` — проверка паролей с опцией `raise_on_error`.
- `generate_youtube_id()` — идентификатор YouTube.
- `generate_hash()` — криптографический хэш.
- `generate_uuid()` — UUID v4.

## ✅ Что исправлено в новой копии

- Нормализованное имя пакета: `import PySaveUtils`.
- Явные исключения `PasswordValidationError` и `HashLengthError`.
- Типы, `dataclass` и строгие проверки входных значений.
- Функциональные обёртки и `LegacyPySaveUtils` для обратной совместимости.

## 📄 Лицензия

MIT — см. файл `LICENSE`.
