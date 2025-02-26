# ---- append Method ----
# ex: lst = [1, 2, 3]
# ex: lst.append([4, 5, 6]) --> [1, 2, 3, [4, 5, 6]]
# ex: lst.append(4) --> [1, 2, 3, 4]
# ex: lst.append(object) 
# ----
# ---- sequential way ----
# ---- using while ----
lst = []
lst1 = []
result = []
ref = '0123456789'
while True:
    a = input('Enter Value for list One: ')
    if a in ref:
        a = int(a)
    if a == 'quit':
        break
    lst = lst + [a]

while True:
    b = input('Enter value for list Two: ')
    if b in ref:
        b = int(b)
    if b == 'quit':
        break
    lst1 = lst1 + [b]

if len(lst1) == 1:
    result = lst + lst1
else:
    result = lst + [lst1]

print('append method using while: ', result)
# ---- End Using While ----
#------------------------------------------------------
#------------------------------------------------------
# ---- Functional Way ----
def append(lst, lst1):
    res = []
    res = lst + [lst1]
    return res

aa = append([1, 2, 3], [4, 5, 6])
bb = append(['a', 'b', 'c'], 'alireza')
cc = append([1,2,3], 4)

print(aa)
print(bb)
print(cc)
# ---- End Functional Way ----
#------------------------------------------------------







        
