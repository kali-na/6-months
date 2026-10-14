import random

random_number = list(range(1, 51))
random_list = random.sample(random_number, 6)
even_list = []
odd_list = []

def even(numbers):
    for nums in random_list:
        if nums % 2 == 0:
            even_list.append(nums)
    return even_list

def odd(numbers):
    for nums in numbers:
        if nums % 2 != 0:
            odd_list.append(nums)
    return odd_list

def more_numbers(even, odd):
    if len(even) > len(odd):
        return even
    elif len(even) < len(odd):
        return odd
    else:
        return 'draw'

print(f'A random list compiled by a bot: {random_list}')
print(f'list of honest numbers: {even(random_list)}')
print(f'list of odd numbers: {odd(random_list)}')
print(more_numbers(even_list, odd_list))
