numbers = []

def sorting(numbers):
    return sorted(numbers)

def min_number(numbers):
    min_num = numbers[0]
    return min_num

def max_number(numbers):
    max_num = numbers[-1]
    return max_num

for _ in range(5):  
    numbers_user_list = int(input('Enter a number for your list:'))
    numbers.append(numbers_user_list)

sorting_list = sorting(numbers)

print(f'Your list: {sorting(numbers)}')
print(f'The minimum number from your list: {min_number(sorting_list)}')
print(f'The maximum number from your list: {max_number(sorting_list)}')
