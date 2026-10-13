# 📊 Min & Max Finder

Небольшой Python-скрипт, который запрашивает у пользователя **5 чисел**, сортирует их и находит **минимум** и **максимум**.

---

## ✨ Возможности

- 🔢 Ввод 5 чисел с клавиатуры
- 🔃 Сортировка списка по возрастанию
- ⬇️ Поиск минимального числа
- ⬆️ Поиск максимального числа
- 🧩 Разбито на три функции: `sorting()`, `min_number()`, `max_number()`

---

## 🚀 Запуск

```bash
python main.py
```

---

## 💻 Пример работы

```
Enter a number for your list: 7
Enter a number for your list: 3
Enter a number for your list: 9
Enter a number for your list: 1
Enter a number for your list: 5

Your list: [1, 3, 5, 7, 9]
The minimum number from your list: 1
The maximum number from your list: 9
```

---

## 🧠 Как это работает

### 1. `sorting(numbers)`
Возвращает **новый** отсортированный список (оригинал не меняется):

```python
def sorting(numbers):
    return sorted(numbers)
```

### 2. `min_number(numbers)`
Берёт первый элемент — это минимум для отсортированного списка:

```python
def min_number(numbers):
    min_num = numbers[0]
    return min_num
```

### 3. `max_number(numbers)`
Берёт последний элемент — это максимум для отсортированного списка:

```python
def max_number(numbers):
    max_num = numbers[-1]
    return max_num
```

### 4. Ввод и вывод

```python
for _ in range(5):
    user_number = int(input("Enter a number for your list: "))
    numbers.append(user_number)

sorted_list = sorting(numbers)

print(f"Your list: {sorting(numbers)}")
print(f"The minimum number from your list: {min_number(sorted_list)}")
print(f"The maximum number from your list: {max_number(sorted_list)}")
```

> ⚠️ `min_number` и `max_number` работают **только с отсортированным списком**. Именно поэтому мы передаём туда `sorted_list`, а не оригинальный `numbers`.

---

## 📁 Структура проекта

```
📦 min-and-max-finder
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
- [ ] Использовать встроенные `min()` и `max()` вместо взятия `[0]` и `[-1]`
- [ ] Добавить проверку на пустой список
- [ ] Написать тесты (`pytest`)

---

## 📄 Лицензия

MIT — используй свободно.
