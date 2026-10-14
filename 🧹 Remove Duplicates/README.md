# 🧹 Remove Duplicates

Небольшой Python-скрипт, который удаляет **дубликаты** из списка и возвращает новый список, содержащий только уникальные элементы.

---

## ✨ Возможности

- 🧹 Удаление повторяющихся чисел из списка
- 📋 Возврат нового списка (оригинал не меняется)
- 🔢 Сохранение исходного порядка элементов
- 🧩 Отдельная функция `remove_duplicates()`

---

## 🚀 Запуск

```bash
python main.py
```

---

## 💻 Пример работы

```
The duplicate was deleted: [1, 2, 3, 4, 5]
```

**Было:** `[1, 2, 2, 3, 4, 4, 4, 5]`  
**Стало:** `[1, 2, 3, 4, 5]`

---

## 🧠 Как это работает

### `remove_duplicates(numbers)`

Проходит по каждому элементу исходного списка и добавляет его в новый список **только если его там ещё нет**:

```python
def remove_duplicates(numbers):
    new_numbers_list = []

    for num in numbers_list:
        if num not in new_numbers_list:
            new_numbers_list.append(num)
    return new_numbers_list
```

**Логика:**
- `if num not in new_numbers_list` → проверяем, есть ли уже такое число
- Если нет → добавляем через `.append()`
- Если есть → пропускаем

Так сохраняется **порядок первого появления** каждого элемента.

---

## 📁 Структура проекта

```
📦 remove-duplicates
 ┣ 📜 main.py
 ┗ 📜 README.md
```

---

## 🛠️ Требования

- Python **3.6+**

Сторонние библиотеки не нужны.

---

## ⚠️ Замечание по коду

Внутри функции используется `numbers_list`, но параметр называется `numbers`.  
Правильнее обращаться к **параметру**, а не к глобальной переменной:

```python
def remove_duplicates(numbers):
    new_numbers_list = []
    for num in numbers:              # 👈 используем параметр
        if num not in new_numbers_list:
            new_numbers_list.append(num)
    return new_numbers_list
```

Иначе функция работает только с одним конкретным списком и не будет универсальной.

---

## 💡 Альтернативные способы

### 1. Через `set` (порядок не сохраняется)
```python
def remove_duplicates(numbers):
    return list(set(numbers))
```

### 2. Через `dict.fromkeys()` (порядок сохраняется)
```python
def remove_duplicates(numbers):
    return list(dict.fromkeys(numbers))
```

### 3. Через list comprehension
```python
def remove_duplicates(numbers):
    result = []
    [result.append(n) for n in numbers if n not in result]
    return result
```

---

## 💡 Идеи для улучшения

- [ ] Спросить у пользователя список чисел через `input()`
- [ ] Добавить обработку ошибок ввода (`try / except`)
- [ ] Сделать функцию универсальной (работать со строками, а не только с числами)
- [ ] Добавить сравнение способов удаления дубликатов
- [ ] Написать тесты (`pytest`)

---

## 📄 Лицензия

MIT — используй свободно.
