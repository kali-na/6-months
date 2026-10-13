user_list = []

def even_numbers(user_list):
    result = []
    for num in user_list: 
        if num % 2 == 0:
            result.append(num)
    return result

for _ in range(5):
    number_user = int(input('Enter the numbers for the list: '))
    user_list.append(number_user)

evens = even_numbers(user_list)
print(f'A new list, only with even numbers: {evens}!')
