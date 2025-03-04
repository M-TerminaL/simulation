# ---- max ----
# ex: lst = [1, 2, 3, 4, 5, 6]
# ex: max(lst) --> 6
# ----
# ---- sequential way ----
# ---- using while ----

# make list with input loop
lst = []
while True:
    data = float(input("Enter the elements of the list(press 000 to make list): "))
    if data == 000:
        break
    lst = lst + [data]

i = 0
max_ = lst[0]

while i < len(lst):
    if lst[i] > max_:
        max_ = lst[i]
        i = i + 1
    else:
        i = i + 1
print('max using while: ', max_)
# ---- End Using While ----
# ---- Using For -----

max_elem = lst[0]

for elem in lst:
    if elem > max_elem:
        max_elem = elem
print('max using for: ', max_elem)


# ---- End Using For ----
# ------------------------------------------------------
# ---- Functional Way ----

def personal_max(lst):
    max_ = lst[0]
    for element in lst:
        if element > max_:
            max_ = element
    return max_


aa = personal_max([11, 14, 6, 98, 34])
print(aa)


def my_max(*args):
    max_ = args[0]
    for element in args:
        if element > max_:
            max_ = element
    return max_


bb = my_max(11, 14, 7, 99, 33)
print(bb)

# ---- End Functional Way ----
# ------------------------------------------------------
