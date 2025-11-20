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
from pysaveutils import (
    PySaveUtils,
    generate_hash,
    generate_youtube_id,
    random_color,
    validate_passwords,
)

utils = PySaveUtils(min_password_length=10)

color = random_color()
youtube_id = generate_youtube_id()
hash_value = generate_hash(32)
is_valid = validate_passwords("Sup3rPass!", "Sup3rPass!")
```

## 🧩 Доступные функции

- `random_color()` — безопасная генерация RGB-цвета.
- `validate_passwords()` — расширенная проверка паролей с опцией `raise_on_error`.
- `generate_youtube_id()` — создание идентификатора с алфавитом YouTube.
- `generate_hash()` — криптографически стойкий хэш произвольной длины.

## ✅ Что исправлено в новой копии

- Нормализованное имя пакета: `import pysaveutils`.
- Явные исключения `PasswordValidationError` и `HashLengthError`.
- Типы, `dataclass` и строгие проверки входных значений.
- Функциональные обёртки для быстрого использования.

## 📄 Лицензия

MIT — см. файл `LICENSE`.
