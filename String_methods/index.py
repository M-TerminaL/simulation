import sys
# ---- Index Method ----
# ex: 'alireza'.index('a', start(1), end(7)) --> 6
# ex: 'alireza'.index('a', 1, 6) --> not found
# ex: 'alireza'.index('a') --> 0
# ----

# ---- sequential way ----
# ---- using while ----
string = input('Enter Your String: ')
target = input('Enter Target: ')
start = input('Start: (def=0) ')
end = input('End: (def=len(string)) ')
result = ''


if start == '' or start in '      ':
    start = 0
else:
    try:
        start = int(start)
    except ValueError:
        print('Value Error')
        sys.exit(1)
if end == '' or end in '       ':
    end = len(string)
else:
    try:
        end = int(end)
    except ValueError:
        print('Value Error')
        sys.exit(1)
    
while start < end:
    if string[start] == target:
        result = start
        break
    else:
        start += 1
if result == '':
    result = 'Not Found'
    print('Index method using while: ', result)
else:
    print('Index method using while: ', result)
# ---- End Using While ----
#------------------------------------------------------
# ---- Sequential Way ----
# ---- Using for ----
str1 = input('Enter Your String: ')
value = input('Enter Target: ')
start_ = input('Start: (def=0) ')
end_ = input('End: (def=len(string)) ')
target_index = ''
# ----
if start_ == '' or start_ in '      ':
    start_ = 0
else:
    try:
        start_ = int(start_)
    except ValueError:
        print('Value Error')
        sys.exit(1)
if end_ == '' or end_ in '     ':
    end_ = len(str1)
else:
    try:
        end_ = int(end_)
    except ValueError:
        print('Value Error')
        sys.exit(1)

for index in range(start_, end_):
    if str1[index] == value:
        target_index = index
        break
print('index method using for: ', target_index)
# ---- End Using for ----
#------------------------------------------------------
# ---- Functional Way ----
def index(string, target, start=0, end=None):
    cout = ''
    if end is None:
        end = len(string)
    for idx in range(start, end):
        if string[idx] == target:
            cout = idx
            break
    if cout == '':
        cout = None
    return cout

a = index('alireza', 'a')
b = index('alireza', 'a', 1)
c = index('alireza', 'a', 1, 5)
d = index('alireza', 'i', start=1, end=7)

print(a)
print(b)
print(c)
print(d)
# ---- End Functional Way ----
#------------------------------------------------------







        
