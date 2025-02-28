import sys
# ---- pop Method ----
# ex: lst = [1, 2, 3, 4, 5, 6]
# ex: lst.pop(index=-1)
# ex: lst.pop() --> [1, 2, 3, 4, 5]
# ex: lst.pop(0) --> [2, 3, 4, 5, 6]
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


index = input('index: (def=-1) ')

if index == '' or index in '      ':
    index = -1
else:
    try:
        index = int(index)
    except ValueError:
        print('Value Error')
        sys.exit(1)

del lst[index]

        
print('pop method of list using while: ', lst)
# ---- End Using While ----
#------------------------------------------------------
# ---- Functional Way ----

def pop(lst, index=-1):
    del lst[index]
    return lst

aa = pop([1,2,3])
bb = pop(['a', 'b', 'c'], 0)

print(aa)
print(bb)

# ---- End Functional Way ----
#------------------------------------------------------







        
