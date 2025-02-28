# ---- count Method ----
# ex: lst = [1, 2, 3, 1, 2, 1]
# ex: lst.count(value)
# ex: lst.count(1) --> 3
# ex: lst.count(4) --> 0
 
# ----
# ---- sequential way ----
# ---- using while ----
ref = '0123456789'
lst = []
counter = 0
i = 0
# make list with input loop
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
    
value = input('Enter Value: ')

while i < len(lst):
    if lst[i] == value:
        counter += 1
        i = i + 1
    else:
        i = i + 1

print('count method of list using while: ', counter)
# ---- End Using While ----
#------------------------------------------------------
# ---- Sequential Way ----
# ---- Using for ----
cnt = 0

for element in lst:
    if element == value:
        cnt = cnt + 1

print('count method of list using for: ', cnt)

# ----
# ---- End Using for ----
#------------------------------------------------------
# ---- Functional Way ----
def my_count(lst: list, value):
    count = 0
    for elem in lst:
        if elem == value:
            count = count + 1
    return count

aa = my_count([1, 2, 3, 'a', 'b', 1, 2, 'a', 1, 'a'], 'a')
bb = my_count([1, 2, 3, 'a', 'b', 1, 2, 'a', 1, 'a'], 1)

print(aa)
print(bb)
        

# ---- End Functional Way ----
#------------------------------------------------------







        
