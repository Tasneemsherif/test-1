# 1. order
# 2. mutable
# 3. duplicates


# set unique data
# use case : IDs
# 1. unordered
# 2. mutable
# 3. no duplicates
ages_set = {10, 20, 38, 20, 'ali', 20, True}
test = {}
print(ages_set)

# print(ages_set[0])

ages_set.add(100)
print(ages_set)

print(len(ages_set))

for x in ages_set:
    print(x)

# ----------------------------------------

# dictionary

# 1. ordered
# 2. mutable
# 3. no duplicates

ages_dict = { 'ali': 20, 'ahmed': 30, 'sara': 25, 'john': 20 }

print(ages_dict)

ages_dict['ali'] = 50
print(ages_dict)

for key in ages_dict:
    print(ages_dict[key])

print(len(ages_dict))