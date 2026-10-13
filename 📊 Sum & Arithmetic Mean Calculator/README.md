# 📊 Sum & Arithmetic Mean Calculator

Небольшой Python-скрипт, который запрашивает у пользователя **11 чисел**, считает их **сумму** и **среднее арифметическое**.

---

## ✨ Возможности

- 🔢 Ввод 11 чисел с клавиатуры
- ➕ Подсчёт суммы всех чисел
- 📈 Подсчёт среднего арифметического
- 🧩 Разбито на две функции: `summa()` и `find_arithmetic_mean()`

---

## 🚀 Запуск

```bash
python main.py
```

---

## 💻 Пример работы

```
Write down your list (only the number): 3
Write down your list (only the number): 7
Write down your list (only the number): 5
Write down your list (only the number): 8
Write down your list (only the number): 2
Write down your list (only the number): 9
Write down your list (only the number): 4
Write down your list (only the number): 6
Write down your list (only the number): 1
Write down your list (only the number): 10
Write down your list (only the number): 5

Your list: [3, 7, 5, 8, 2, 9, 4, 6, 1, 10, 5]
The sum of your list: 60
The arithmetic mean of your list: 5.454545454545454
```

---

## 🧠 Как это работает

### 1. `summa(numbers)`
Проходит по всем числам списка и накапливает их сумму:

```python
def summa(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
```

### 2. `find_arithmetic_mean(numbers)`
Делит сумму чисел на их количество:

```python
def find_arithmetic_mean(numbers):
    count = len(numbers)
    answer = summa(numbers) / count
    return answer
```

### 3. Ввод и вывод

```python
for _ in range(11):
    user_number = int(input("Write down your list (only the number): "))
    numbers.append(user_number)
```

---

## 📁 Структура проекта

```
📦 sum-and-mean
 ┣ 📜 main.py
 ┗ 📜 README.md
```

---

## 🛠️ Требования

- Python **3.6+**

Никакие сторонние библиотеки не нужны.

---

## 💡 Идеи для улучшения

- [ ] Спросить у пользователя количество чисел (вместо фиксированных 11)
- [ ] Добавить обработку ошибок ввода (`try / except`)
- [ ] Использовать встроенные `sum()` и `statistics.mean()`
- [ ] Защита от деления на ноль при пустом списке
- [ ] Добавить тесты (`pytest`)

---

## 📄 Лицензия

MIT — используй свободно.
