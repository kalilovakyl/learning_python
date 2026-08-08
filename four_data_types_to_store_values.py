# First is list
pet_list = ["dog", "cat", "spider", "jaguar"]
print(pet_list)

def print_all(some_list):
    start = 0
    finish = len(some_list)
    step = 1
    for i in range(start, finish, step):
        print(some_list[i])

print_all(pet_list)

print(type(pet_list[0]))
