import sys

# ---- find Method ----
# ex: 'alireza'.find('a', start(1), end(7)) --> 6
# ex: 'alireza'.find('a', 1, 6) --> -1 means not found

# ---- sequential way ----
# ---- using while ----
string = input('Enter Your String: ')
target = input('Enter Your target: ')
start = input('Start (Def=0): ')
end = input('End (Def=len(string)): ')
# ----
target_len = len(target)
# ----
if start == '' or start in '     ':
    start = 0
else:
    try:
        start = int(start)
    except ValueError:
        print('enter integer value in start')
        sys.exit(1)

if end == '' or end in '     ':
    end = len(string)
else:
    try:
        end = int(end)
    except ValueError:
        print('enter integer value in End')
        sys.exit(1)

result = -1
while start < end:
    if string[start:start + target_len] == target:
        result = start
        break
    else:
        start += 1

print('find method using while: ', result)
# ---- End Using While ----
# ------------------------------------------------------
# ---- Sequential Way ----
# ---- Using for ----
string_ = input('Enter Your String: ')
target_ = input('Enter Your target: ')
start_ = input('Start (Def=0): ')
end_ = input('End (Def=len(string)): ')
# ----
tg_len = len(target_)
# ----
if start_ == '' or start_ in '     ':
    start_ = 0
else:
    try:
        start_ = int(start_)
    except ValueError:
        print('enter integer value in start')
        sys.exit(1)

if end_ == '' or end_ in '     ':
    end_ = len(string_)
else:
    try:
        end_ = int(end_)
    except ValueError:
        print('enter integer value in End')
        sys.exit(1)

res = -1

for index in range(start_, end_ - tg_len + 1):
    if string_[index:index + tg_len] == target_:
        res = index
        break

print('find method using for: ', res)


# ---- End Using for ----
# ------------------------------------------------------
# ---- Functional Way ----
def find(string, target, start=0, end=None):
    target_len = len(target)
    if end == None:
        end = len(string)
    find_index = ''

    for index in range(start, end - target_len + 1):
        if string[index:index + target_len] == target:
            find_index = index
            break
    if find_index == '':
        return -1
    else:
        return find_index


a = find('alireza', 'a')
b = find('alireza', 'a', 1, 4)
c = find('alireza', 'a', 1, 7)
d = find('alireza ali all', 'al')
e = find('alireza ali all', 'al', 1, 4)
f = find('alireza ali all', 'al', 1)

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
# ---- End Functional Way ----
# ------------------------------------------------------
