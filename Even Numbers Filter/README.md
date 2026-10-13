# 🔢 Even Numbers Filter

Небольшой Python-скрипт, который запрашивает у пользователя **5 чисел** и возвращает новый список, содержащий **только чётные числа**.

---

## ✨ Возможности

- 🔢 Ввод 5 чисел с клавиатуры
- 🎯 Фильтрация только чётных чисел
- 📋 Возврат нового списка (оригинал не меняется)
- 🧩 Отдельная функция `even_numbers()` для фильтрации

---

## 🚀 Запуск

```bash
python main.py
```

---

## 💻 Пример работы

```
Enter the numbers for the list: 1
Enter the numbers for the list: 2
Enter the numbers for the list: 3
Enter the numbers for the list: 4
Enter the numbers for the list: 5

A new list, only with even numbers: [2, 4]!
```

---

## 🧠 Как это работает

### 1. `even_numbers(user_list)`
Проходит по всем числам списка и добавляет в новый список только чётные:

```python
def even_numbers(user_list):
    result = []
    for num in user_list:
        if num % 2 == 0:
            result.append(num)
    return result
```

**Как определяется чётность:**
- `num % 2 == 0` → число чётное (делится на 2 без остатка)
- `num % 2 != 0` → число нечётное

### 2. Ввод данных

```python
user_list = []

for _ in range(5):
    number_user = int(input("Enter the numbers for the list: "))
    user_list.append(number_user)
```

### 3. Вывод результата

```python
evens = even_numbers(user_list)
print(f"A new list, only with even numbers: {evens}!")
```

---

## 📁 Структура проекта

```
📦 even-numbers-filter
 ┣ 📜 main.py
 ┗ 📜 README.md
```

---

## 🛠️ Требования

- Python **3.6+**

Сторонние библиотеки не нужны.

---

## 💡 Идеи для улучшения

- [ ] Спросить у пользователя количество чисел (вместо фиксированных 5)
- [ ] Добавить обработку ошибок ввода (`try / except`)
- [ ] Сделать фильтр универсальным: чётные, нечётные, положительные, отрицательные
- [ ] Заменить цикл на list comprehension:
  ```python
  return [num for num in user_list if num % 2 == 0]
  ```
- [ ] Написать тесты (`pytest`)

---

## 📄 Лицензия

MIT — используй свободно.
