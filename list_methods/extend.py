# ---- extend Method ----
# ex: lst = [1, 2, 3]
# ex: lst.extend([4, 5, 6]) --> [1, 2, 3, 4, 5, 6]
# ex: lst.extend([4]) --> [1, 2, 3, 4]
# ex: lst.extend('hell') --> [1, 2, 3, 'h', 'e', 'l', 'l']
# ex: lst.extend(iterable) 
# ----
# ---- sequential way ----
# ---- using while ----
lst = []
lst1 = []
result = []
ref = '0123456789'
while True:
    a = input('Enter Value for list One: ')
    if a == 'quit':
        break
    if a in ref:
        try:
            a = int(a)
        except:
            pass
    lst = lst + [a]

while True:
    b = input('Enter value for list Two: ')
    if b == 'quit':
        break
    if b in ref:
        try:
            b = int(b)
        except:
            pass
    lst1 = lst1 + [b]

result = lst + lst1
print('extend method using while: ', result)


# ---- End Using While ----
# ------------------------------------------------------
# ---- Functional Way ----
def extend(lst, lst1):
    res = []
    res = lst + list(lst1)
    return res


aa = extend([1, 2, 3], [4, 5, 6])
bb = extend(['a', 'b', 'c'], 'alireza')

print(aa)
print(bb)

# ---- End Functional Way ----
# ------------------------------------------------------
