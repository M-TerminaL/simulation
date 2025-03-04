# ---- insert Method ----
# ex: lst = [1, 2, 3]
# ex: lst.insert(index, object)
# ex: lst.insert(1, 'python') --> [1, 'python', 2, 3]

# ----
# ---- sequential way ----
# ---- using while ----
ref = '0123456789'
lst = []
while True:
    a = input('Enter value to complete list: ')
    if a == 'quit':
        break
    if a in ref:
        try:
            a = int(a)
        except:
            pass

    lst = lst + [a]
index = int(input('Enter index: '))
object1 = input('Enter Object: ')

lst[index:index] = [object1]
print(lst)


# ---- End Using While ----
# ------------------------------------------------------
# ---- Functional Way ----

def insert(lst: list, index: int, obj):
    lst[index:index] = [obj]
    return lst


aa = insert([1, 2, 3], 1, 'hello')
print(aa)
# ---- End Functional Way ----
# ------------------------------------------------------
