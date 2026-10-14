numbers_list = [1, 2, 2, 3, 4, 4, 4, 5]

def remove_duplicates(numbers):
    new_numbers_list = []

    for num in numbers_list:
        if num not in new_numbers_list:
            new_numbers_list.append(num)
    return new_numbers_list


print(f'The duplicate was deleted: {remove_duplicates(numbers_list)}')





