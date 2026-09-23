[README.md](https://github.com/user-attachments/files/32550417/README.md)
# 🐍 Beginner Python Knowledge Base (Python Bugs & Features)

Исполняемая база знаний и шпаргалка по самым распространенным ошибкам и особенностям языка Python, с которыми сталкиваются начинающие разработчики.

An interactive knowledge base and cheatsheet covering common Python traps, bugs, and non-obvious features for beginners.

---

## 📌 Особенности / Features

- 🌐 **Двуязычный интерфейс / Dual-language support:** Русский / English.
- 🔄 **Интерактивный цикл / Interactive CLI:** Выбирайте любые пункты подряд без необходимости перезапускать программу.
- ⚡ **Нулевые зависимости / Zero dependencies:** Использует только встроенные модули Python (`os`), не требует установки сторонних библиотек.
- 🖥️ **Кроссплатформенность / Cross-platform:** Работает на Linux, Windows и macOS.

---

## 🛠️ Как запустить / How to Run

### Linux / macOS
```bash
python3 help.py
```

### Windows
```cmd
python help.py
```

---

## 📚 Какие ошибки разобраны / Errors Covered

0. **Путаница с `=` и `==`** / Confusing assignment (`=`) with equality comparison (`==`).
1. **Копирование словарей и списков** / Object reference issues when copying dicts/lists (`dict_b = dict_a`).
2. **Ключи словарей и Булевы значения** / Boolean keys collapsing into integer keys (`dict_a[True]`).
3. **Обновление списков и словарей** / Misunderstanding in-place methods that return `None` (`list_a = list_a.append(6)`).
4. **Интернированные строки** / Difference between value equality (`==`) and object identity (`is`).
5. **Аргументы по умолчанию** / Mutable default arguments being evaluated only once during function definition (`lst=[]`).

---

## 🤝 Вклад в проект / Contributing

Проект открыт для любых изменений! Вы можете:
1. Добавить новые распространенные ошибки или фичи Python.
2. Перевести интерфейс на другие языки (например, украинский, испанский).
3. Создать Pull Request или открыть Issue на GitHub.
