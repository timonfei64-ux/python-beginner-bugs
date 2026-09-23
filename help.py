import os

TEXTS = {
    "ru": {
        "welcome": "=== БАЗА ЗНАНИЙ ДЛЯ НОВИЧКОВ (PYTHON BUGS & FEATURES) ===",
        "intro": "В первые дни работы программистом на Python все мы сталкиваемся с багами, которые после нескольких часов поиска оказываются фичей Python'а. Вот распространенные ошибки:",
        "choose_lang": "Выбери язык / Choose language:\n1 - Русский\n2 - English",
        "menu_title": "\nВыбери номер ошибки для разбора (или 'exit' для выхода):",
        "err0_title": "0 - Путаница с '=' и '=='",
        "err1_title": "1 - Копирование словарей или списков (dict_b = dict_a)",
        "err2_title": "2 - Ключи словарей и Булевы значения (dict_a[True])",
        "err3_title": "3 - Обновление списков и словарей (list_a = list_a.append(6))",
        "err4_title": "4 - Интернированные строки (a is b)",
        "err5_title": "5 - Аргументы по умолчанию вычисляются один раз (lst=[])",
        "err0_desc": "\n[Ошибка]: Использование '=' вместо '==' в условиях.\n[Решение]: Знак '=' присваивает значение, а '==' сравнивает их!\nПример: if score == 10:\n",
        "err1_desc": "\n[Ошибка]: dict_b = dict_a\nИзменение dict_b изменит и dict_a, так как обе переменные указывают на один объект.\n[Решение]: Используй dict_b = dict_a.copy() или deepcopy() для вложенных структур.\n",
        "err2_desc": "\n[Ошибка]: dict_a[1] = 'apple'; dict_a[True] = 'mango'\nКлюч 1 затрется, потому что True в Python наследуется от int и эквивалентен 1 (isinstance(True, int) == True).\n[Решение]: Помни, что True == 1 и False == 0 при использовании их в качестве ключей.\n",
        "err3_desc": "\n[Ошибка]: list_a = list_a.append(6) делает list_a равным None!\nМетоды append(), sort(), update() меняют объект «на месте» (in-place) и возвращают None.\n[Решение]: Пиши просто list_a.append(6) без присваивания обратно в переменную.\n",
        "err4_desc": "\n[Ошибка]: Использование 'is' вместо '==' для сравнения строк.\nPython интернирует (переиспользует) короткие ASCII-строки (a = 'gmail'; b = 'gmail'; a is b -> True), но для '@gmail' 'is' вернет False.\n[Решение]: Используй '==' для проверки равенства значений и 'is' только для проверки указания на один и тот же объект в памяти.\n",
        "err5_desc": "\n[Ошибка]: def func(a, lst=[]): lst.append(a); return lst\nПри повторных вызовах список не очищается, так как аргументы по умолчанию вычисляются всего один раз при объявлении функции.\n[Решение]: Используй None в качестве значения по умолчанию:\ndef func(a, lst=None):\n    if lst is None:\n        lst = []\n    lst.append(a)\n    return lst\n",
        "unknown": "\nНеизвестная команда, попробуй еще раз.\n"
    },
    "en": {
        "welcome": "=== BEGINNER KNOWLEDGE BASE (PYTHON BUGS & FEATURES) ===",
        "intro": "In the early days of Python programming, we all encounter bugs that turn out to be Python features. Here are common mistakes:",
        "choose_lang": "Выбери язык / Choose language:\n1 - Русский\n2 - English",
        "menu_title": "\nSelect an error number to inspect (or type 'exit' to quit):",
        "err0_title": "0 - Confusing '=' and '=='",
        "err1_title": "1 - Copying dictionaries or lists (dict_b = dict_a)",
        "err2_title": "2 - Dictionary keys and Booleans (dict_a[True])",
        "err3_title": "3 - Updating lists or dictionaries (list_a = list_a.append(6))",
        "err4_title": "4 - Interned strings (a is b)",
        "err5_title": "5 - Default arguments evaluated once (lst=[])",
        "err0_desc": "\n[Error]: Using '=' instead of '==' inside if-statements.\n[Solution]: '=' assigns a value, while '==' compares them!\nExample: if score == 10:\n",
        "err1_desc": "\n[Error]: dict_b = dict_a\nModifying dict_b also changes dict_a because both point to the same object.\n[Solution]: Use dict_b = dict_a.copy() or deepcopy() for nested structures.\n",
        "err2_desc": "\n[Error]: dict_a[1] = 'apple'; dict_a[True] = 'mango'\nKey 1 gets overwritten because True inherits from int and equals 1 (isinstance(True, int) == True).\n[Solution]: Keep in mind that True == 1 and False == 0 when using them as dict keys.\n",
        "err3_desc": "\n[Error]: list_a = list_a.append(6) makes list_a equal to None!\nMethods like append(), sort(), and update() operate in-place and return None.\n[Solution]: Simply call list_a.append(6) without re-assigning it.\n",
        "err4_desc": "\n[Error]: Using 'is' instead of '==' for string comparison.\nPython interns short ASCII strings (a = 'gmail'; b = 'gmail'; a is b -> True), but for '@gmail' 'is' returns False.\n[Solution]: Use '==' to check value equality and 'is' only to check if variables point to the exact same memory object.\n",
        "err5_desc": "\n[Error]: def func(a, lst=[]): lst.append(a); return lst\nSubsequent calls reuse the same list because default arguments are evaluated only once during function definition.\n[Solution]: Use None as the default value:\ndef func(a, lst=None):\n    if lst is None:\n        lst = []\n    lst.append(a)\n    return lst\n",
        "unknown": "\nUnknown command, try again.\n"
    }
}

print("1 - Русский\n2 - English")
user_lang = input("Выбор / Choice: ")

if user_lang == "2":
    lang = "en"
else:
    lang = "ru"

t = TEXTS[lang]

os.system("cls" if os.name == "nt" else "clear")

print(t["welcome"])
print(t["intro"])

while True:
    print(t["menu_title"])
    print(t["err0_title"])
    print(t["err1_title"])
    print(t["err2_title"])
    print(t["err3_title"])
    print(t["err4_title"])
    print(t["err5_title"])

    choice = input("\n> ")

    if choice == "0":
        print(t["err0_desc"])
    elif choice == "1":
        print(t["err1_desc"])
    elif choice == "2":
        print(t["err2_desc"])
    elif choice == "3":
        print(t["err3_desc"])
    elif choice == "4":
        print(t["err4_desc"])
    elif choice == "5":
        print(t["err5_desc"])
    elif choice.lower() == "exit":
        break
    else:
        print(t["unknown"])
