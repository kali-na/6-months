

first_list = [1, 2, 5, 6, 7]
second_list = [1, 4, 6, 10, 20]

def add_list(one_list, two_list):
    done_list = one_list + two_list
    sorting = sorted(done_list)
    return sorting


print(add_list(first_list, second_list))
print(add_list(first_list, second_list)[:3])
print(add_list(first_list, second_list)[-3:])
