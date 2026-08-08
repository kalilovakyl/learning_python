# First is list
'''
List stores values in order and they can be changed
'''

pet_list = ["dog", "cat", "spider", "jaguar"]
print(pet_list)

def print_all(some_list):
    start = 0
    finish = len(some_list)
    step = 1
    for i in range(start, finish, step):
        print(some_list[i])
pet_list[0] = "not dog"
print_all(pet_list)


# Tuples
'''
Tuples are the same as list but variables cannot be changed
'''

gpu_tuple = ("rx6600", "rtx5090", "rtx3050")
print(gpu_tuple)
print(f"First value in tuple is {gpu_tuple[0]}")

# Sets

'''
    For now seems kinda useless, why not use tuples of lists
    Sets doesn't have index, unordered and unchangeble
    dublicates going to be ignored in set
'''

fruit_set = {"apple", "banana", "mango", 4}
print(fruit_set)

# Dictionaries
'''
    Data collection type which collects keys and values
    really cool data type 
'''

music_dict = { "eartquake": "Tyler the Creator",
               "fein": "Playboi Carti",
               "follow god": "Kanye West" }

print(music_dict["fein"])
