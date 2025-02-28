# ---- Remove Method ----
# ex: lst = [1, 2, 3, 1, 2, 1]
# ex: lst.remove(value)
# ex: lst.remove(1) --> [2, 3, 1, 2, 1]
# ex: lst.remove(4) --> Error:  x not in list
# ----
# ---- sequential way ----
# ---- using while ----
ref = '0123456789'
lst = []
# make list with input loop
while True:
    a = input('Enter obj to complete list: ')
    if a == 'quit':
        break
    if a in ref:
        try:
            a = int(a)
        except:
            pass    
    lst = lst + [a]
    
value = input('Enter Value: ')
if value in ref:
    try:
        value = int(value)
    except:
        pass

i = 0
while i < len(lst):
    if lst[i] == value:
        del lst[i]
        break
    else:
        i = i + 1
        
print('remove method of list using while: ', lst)
# ---- End Using While ----
#------------------------------------------------------
# ---- Sequential Way ----
# ---- Using for ----
lst1 = []
# make list with input loop
while True:
    b = input('Enter obj to complete list: ')
    if b == 'quit':
        break
    if b in ref:
        try:
            b = int(b)
        except:
            pass    
    lst1 = lst1 + [b]
    
value1 = input('Enter Value: ')

if value1 in ref:
    try:
        value1 = int(value1)
    except:
        pass

for index in range(len(lst1)):
    if lst1[index] == value1:
        del lst1[index]
        break
print('remove method using for: ', lst1)
# ----
# ---- End Using for ----
#------------------------------------------------------
# ---- Functional Way ----
def remove(lst, value):
    for idx in range(len(lst)):
        if lst[idx] == value:
            del lst[idx]
            break
    return lst

aa = remove([1, 'a', 1, 'b', 1, 'c'], 1)
bb = remove([1, 2, 3, 4, 2, 5, 2], 2)
cc = remove(['a', 'b', 'c', 'b', 'd', 'c'], 'c')

print(aa)
print(bb)
print(cc)

# ---- End Functional Way ----
#------------------------------------------------------







        
