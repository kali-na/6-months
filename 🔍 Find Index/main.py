numbers = [1, 2, 3, 4, 5, 6, 7]
target = 4

def find_index(numbers, target):
    for index, num in enumerate(numbers):
        if num == target:
            return index
    return None

result = find_index(numbers, target)
if result is not None:
    print(f"Индекс: {result}")
else:
    print("Не найдено")
