numbers = []

def summa(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def find_arithmetic_mean(numbers):
    arithmetic_mean = len(numbers)
    answer_arithmetic_mean = summa(numbers) / arithmetic_mean
    return answer_arithmetic_mean

for _ in range(11):
    user_list = int(input('Write down your list (only the number):'))
    numbers.append(user_list)
    
print(f'Your list: {numbers}')
print(f'The amount of your list: {summa(numbers)}')
print(f'The arithmetic mean of your list: {find_arithmetic_mean(numbers)}')



