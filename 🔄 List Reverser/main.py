user_list = []

def slice(user_list):
    slice_num = user_list[::-1]
    return slice_num

def revers(user_list):
    user_list.reverse()
    return user_list

for num in range(1, 5 + 1):
    user_numbers = int(input(f'Enter a number {num}: '))
    user_list.append(user_numbers)

print(f'The list was created using slices: {slice(user_list)}')
print(f'The list was created using reverse: {revers(user_list)}')
