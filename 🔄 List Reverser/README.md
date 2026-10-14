# 🔄 List Reverser

Небольшой Python-скрипт, который запрашивает у пользователя **5 чисел** и показывает список в обратном порядке **двумя способами**: через срез (slice) и через метод `reverse()`.

---

## ✨ Возможности

- 🔢 Ввод 5 чисел с клавиатуры
- ✂️ Разворот списка через срез `[::-1]`
- 🔃 Разворот списка через метод `reverse()`
- 🧩 Две отдельные функции: `slice()` и `revers()`

---

## 🚀 Запуск

```bash
python main.py
```

---

## 💻 Пример работы

```
Enter a number 1: 10
Enter a number 2: 20
Enter a number 3: 30
Enter a number 4: 40
Enter a number 5: 50

The list was created using slices: [50, 40, 30, 20, 10]
The list was created using reverse: [50, 40, 30, 20, 10]
```

---

## 🧠 Как это работает

### 1. `slice(user_list)` — разворот через срез

```python
def slice(user_list):
    slice_num = user_list[::-1]
    return slice_num
```

`[::-1]` — это **срез с шагом -1**, который создаёт **новый** список в обратном порядке.  
Оригинальный `user_list` **не меняется**.

### 2. `revers(user_list)` — разворот через `reverse()`

```python
def revers(user_list):
    user_list.reverse()
    return user_list
```

`.reverse()` — метод списка, который меняет список **на месте** (in-place).  
Оригинальный `user_list` **изменяется**.

### 3. Ввод данных

```python
user_list = []

for num in range(1, 5 + 1):
    user_numbers = int(input(f"Enter a number {num}: "))
    user_list.append(user_numbers)
```

### 4. Вывод результата

```python
print(f"The list was created using slices: {slice(user_list)}")
print(f"The list was created using reverse: {revers(user_list)}")
```

---

## ⚖️ Разница между `[::-1]` и `reverse()`

| Способ | Что делает | Меняет оригинал? | Возвращает |
|--------|-----------|------------------|------------|
| `user_list[::-1]` | Создаёт новый список | ❌ Нет | Новый список |
| `user_list.reverse()` | Разворачивает на месте | ✅ Да | `None` |

> 💡 Именно поэтому в `revers()` есть `return user_list` — потому что `reverse()` сам ничего не возвращает.

---

## 📁 Структура проекта

```
📦 list-reverser
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
- [ ] Использовать встроенную функцию `reversed()` для третьего способа
- [ ] Показать, что оригинальный список меняется после `reverse()`
- [ ] Написать тесты (`pytest`)

---

## 📄 Лицензия

MIT — используй свободно.
