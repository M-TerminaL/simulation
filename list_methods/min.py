# ---- min ----
# ex: lst = [1, 2, 3, 4, 5, 6]
# ex: min(lst) --> 1
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
min_ = lst[0]

while i < len(lst):
    if lst[i] < min_:
        min_ = lst[i]
        i = i + 1
    else:
        i = i + 1
print('min using while: ', min_)
# ---- End Using While ----
# ---- Using For -----

min_elem = lst[0]

for elem in lst:
    if elem < min_elem:
        min_elem = elem
print('min using for: ', min_elem)


# ---- End Using For ----
# ------------------------------------------------------
# ---- Functional Way ----

def personal_min(lst):
    min_ = lst[0]
    for element in lst:
        if element < min_:
            min_ = element
    return min_


aa = personal_min([11, 14, 6, 98, 34])
print(aa)


def my_min(*args):
    min_ = args[0]
    for element in args:
        if element < min_:
            min_ = element
    return min_


bb = my_min(11, 14, 7, 99, 33)
print(bb)

# ---- End Functional Way ----
# ------------------------------------------------------
