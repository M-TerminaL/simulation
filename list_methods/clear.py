# ---- clear Method ----
# ex: lst = [1, 2, 3, 4, 5, 6]
# ex: lst.clear() --> []
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



del lst[:len(lst)]

        
print('pop method of list using while: ', lst)
# ---- End Using While ----
#------------------------------------------------------
# ---- Functional Way ----

def clear(lst: list):
    del lst[:len(lst)]
    return lst

aa = clear([1,2,3])
bb = clear(['a', 'b', 'c'])

print(aa)
print(bb)

# ---- End Functional Way ----
#------------------------------------------------------







        
