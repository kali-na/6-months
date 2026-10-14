# 🔍 Find Index

Небольшой Python-скрипт, который ищет **индекс элемента** в списке с помощью функции `enumerate()`.

---

## ✨ Возможности

- 🔍 Поиск индекса заданного числа в списке
- 🔁 Перебор элементов через `enumerate()` (индекс + значение)
- ✅ Возврат индекса, если элемент найден
- ❌ Возврат `None`, если элемент не найден

---

## 🚀 Запуск

```bash
python main.py
```

---

## 💻 Пример работы

**Когда элемент найден:**
```
Индекс: 3
```

**Когда элемент не найден:**
```
Не найдено
```

---

## 🧠 Как это работает

### `find_index(numbers, target)`

Проходит по списку с помощью `enumerate()`, который возвращает **пару (индекс, значение)**:

```python
def find_index(numbers, target):
    for index, num in enumerate(numbers):
        if num == target:
            return index
    return None
```

**Пошагово:**
1. `enumerate(numbers)` → `(0, 1), (1, 2), (2, 3), (3, 4), ...`
2. Если `num == target` → сразу возвращаем `index`
3. Если цикл закончился и ничего не нашли → возвращаем `None`

### Проверка результата

```python
result = find_index(numbers, target)
if result is not None:
    print(f"Индекс: {result}")
else:
    print("Не найдено")
```

> ⚠️ Важно проверять именно `is not None`, а не `if result:`, потому что индекс `0` — валидный результат, но `if 0:` даст `False`.

---

## 📊 Как работает `enumerate()`

```python
numbers = [10, 20, 30]

for index, value in enumerate(numbers):
    print(index, value)
```

**Вывод:**
```
0 10
1 20
2 30
```

По умолчанию индексация начинается с `0`. Можно изменить:

```python
enumerate(numbers, start=1)   # начнёт с 1
```

---

## 📁 Структура проекта

```
📦 find-index
 ┣ 📜 main.py
 ┗ 📜 README.md
```

---

## 🛠️ Требования

- Python **3.6+**

Сторонние библиотеки не нужны.

---

## 💡 Альтернативные способы

### 1. Через `list.index()`
```python
def find_index(numbers, target):
    try:
        return numbers.index(target)
    except ValueError:
        return None
```

### 2. Через генератор
```python
def find_index(numbers, target):
    return next((i for i, n in enumerate(numbers) if n == target), None)
```

### 3. Найти **все** индексы
```python
def find_all_indexes(numbers, target):
    return [i for i, n in enumerate(numbers) if n == target]
```

---

## ⚖️ Сравнение способов

| Способ | Плюсы | Минусы |
|--------|-------|--------|
| `enumerate()` | Универсальный, понятный | Чуть длиннее |
| `.index()` | Короткий | Бросает исключение, если не найдено |
| Генератор + `next()` | В одну строку | Менее читаемо для новичков |

---

## 💡 Идеи для улучшения

- [ ] Спросить список и target у пользователя через `input()`
- [ ] Найти **все** вхождения элемента, а не только первое
- [ ] Добавить обработку ошибок ввода (`try / except`)
- [ ] Сделать поиск регистронезависимым (для строк)
- [ ] Написать тесты (`pytest`)

---

## 📄 Лицензия

MIT — используй свободно.
