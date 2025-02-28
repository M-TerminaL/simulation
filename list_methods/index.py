import sys
# ---- index Method ----
# ex: lst = [1, 2, 3, 4, 5, 6]
# ex: lst.index(value, start(def=0), stop(def=len(lst)))
# ex: lst.index(2) --> 1
# ex: lst.index(3, 1, 4) --> 2
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

value = input('Value: ')
start = input('Start: (def=0) ')
stop = input('Stop: (def=len(lst)) ')


if value in ref:
    try:
        value = int(value)
    except:
        pass

if start == '' or start in '         ':
    start = 0
else:
    try:
        start = int(start)
    except ValueError:
        print('Value Error')
        sys.exit(1)
if stop == '' or stop in '     ':
    stop = len(lst)
else:
    try:
        stop = int(stop)
    except ValueError:
        print('Value Error')
        sys.exit(1)
#main
result = None
while start < stop:
    if lst[start] == value:
        result = start
        break
    else:
        start = start + 1

if result == None:
    result = 'Not Found'

print('index method using while: ', result)
# ---- End Using While ----
# ---- Using For -----
idx = None
for index in range(start, stop):
    if lst[index] == value:
        idx = index
        break
if idx == None:
    idx = 'Not Found'
    
print('index method using for: ', idx)
# ---- End Using For ----
#------------------------------------------------------
# ---- Functional Way ----
def index(lst, value, start=0, stop=None):
    idx = None
    if stop == None:
        stop = len(lst)
    for index in range(start, stop):
        if lst[index] == value:
            idx = index
            break
    if idx == None:
        idx = 'Not Found'
    return idx
    
aa = index([1, 2, 3, 1, 4, 4], 1, start=2, stop=5)
bb = index([1, 2, 3, 1, 4], 2)

print(aa)
print(bb)
# ---- End Functional Way ----
#------------------------------------------------------







        
