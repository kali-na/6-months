# 🎲 Random Even & Odd Splitter

Небольшой Python-скрипт, который генерирует **случайный список из 6 чисел** (от 1 до 50), разделяет их на **чётные** и **нечётные**, а затем определяет, каких чисел больше.

---

## ✨ Возможности

- 🎲 Генерация случайных 6 чисел от 1 до 50 (без повторов)
- 🟢 Отдельный список для чётных чисел
- 🔴 Отдельный список для нечётных чисел
- ⚖️ Сравнение количества чётных и нечётных
- 🧩 Три функции: `even()`, `odd()`, `more_numbers()`

---

## 🚀 Запуск

```bash
python main.py
```

---

## 💻 Пример работы

```
A random list compiled by a bot: [12, 45, 7, 30, 18, 3]
list of even numbers: [12, 30, 18]
list of odd numbers: [45, 7, 3]
[12, 30, 18]
```

Если чётных и нечётных поровну:
```
draw
```

---

## 🧠 Как это работает

### 1. Генерация случайного списка

```python
import random

random_number = list(range(1, 51))       # числа от 1 до 50
random_list = random.sample(random_number, 6)   # 6 уникальных чисел
```

`random.sample()` выбирает **уникальные** числа — без повторов.

### 2. Функция `even(numbers)` — чётные числа

```python
def even(numbers):
    for nums in random_list:             # ⚠️ см. замечание ниже
        if nums % 2 == 0:
            even_list.append(nums)
    return even_list
```

Число чётное, если `num % 2 == 0`.

### 3. Функция `odd(numbers)` — нечётные числа

```python
def odd(numbers):
    for nums in numbers:
        if nums % 2 != 0:
            odd_list.append(nums)
    return odd_list
```

Число нечётное, если `num % 2 != 0`.

### 4. Функция `more_numbers(even, odd)` — сравнение

```python
def more_numbers(even, odd):
    if len(even) > len(odd):
        return even
    elif len(even) < len(odd):
        return odd
    else:
        return "draw"
```

Возвращает список, в котором больше чисел, или `"draw"` при равенстве.

---

## ⚠️ Замечания по коду

### 1. `even()` использует глобальную переменную вместо параметра

```python
def even(numbers):
    for nums in random_list:      # ❌ использует глобальную random_list
```

Правильнее — обращаться к параметру:

```python
def even(numbers):
    for nums in numbers:          # ✅ использует переданный аргумент
```

### 2. Функции меняют глобальные списки

```python
even_list = []   # глобальный список
```

Если вызвать `even()` дважды, числа **продублируются** в `even_list`. Лучше создавать список внутри функции:

```python
def even(numbers):
    result = []
    for num in numbers:
        if num % 2 == 0:
            result.append(num)
    return result
```

### 3. Опечатка в выводе

```
list of honest numbers: ...
```

Скорее всего имелось в виду **even** (чётные), а не **honest** (честные).

---

## ✅ Исправленный вариант

```python
import random

def even(numbers):
    return [n for n in numbers if n % 2 == 0]

def odd(numbers):
    return [n for n in numbers if n % 2 != 0]

def more_numbers(evens, odds):
    if len(evens) > len(odds):
        return evens
    elif len(evens) < len(odds):
        return odds
    else:
        return "draw"


random_list = random.sample(range(1, 51), 6)
evens = even(random_list)
odds = odd(random_list)

print(f"A random list compiled by a bot: {random_list}")
print(f"List of even numbers: {evens}")
print(f"List of odd numbers: {odds}")
print(more_numbers(evens, odds))
```

---

## 📁 Структура проекта

```
📦 random-even-odd-splitter
 ┣ 📜 main.py
 ┗ 📜 README.md
```

---

## 🛠️ Требования

- Python **3.6+**

Модуль `random` входит в стандартную библиотеку — устанавливать ничего не нужно.

---

## 💡 Идеи для улучшения

- [ ] Спросить у пользователя количество чисел
- [ ] Позволить задать диапазон (например, 1–100)
- [ ] Показать, насколько чётных больше (разницу)
- [ ] Добавить подсчёт суммы чётных и нечётных отдельно
- [ ] Написать тесты (`pytest`)

---

## 📄 Лицензия

MIT — используй свободно.
