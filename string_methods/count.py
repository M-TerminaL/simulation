import sys

# ---- count Method ----
# ex: 'alireza'.count('a', start(1), end(7)) --> 1
# ex: 'alireza'.count('a', 1, 6) --> 0

# ---- sequential way ----
string = input('Enter Your String: ')
target = input('Enter Target: ')
start = input('Start: (Def=0) ')
end = input('End: (Def=len(string)) ')
# ---- using while ----
target_len = len(target)
if start == '' or start in '     ':
    start = 0
else:
    try:
        start = int(start)
    except ValueError:
        print('Value Error')
        sys.exit(1)
if end == '' or end in '      ':
    end = len(string)
else:
    try:
        end = int(end)
    except ValueError:
        print('Value Error')
        sys.exit(1)
counter = 0
while start < end:
    if string[start:start + target_len] == target:
        counter = counter + 1
        start = start + 1
    else:
        start = start + 1

print('count using while', counter)
# ---- End Using While ----
# ------------------------------------------------------
# ---- Sequential Way ----
# ---- Using for ----
string_ = input('Enter Your String: ')
target_ = input('Enter Target: ')
start_ = input('Start: (Def=0) ')
end_ = input('End: (Def=len(string)) ')
# --------

tg_len = len(target_)
c = 0

if start_ == '' or start_ in '     ':
    start_ = 0
else:
    try:
        start_ = int(start_)
    except ValueError:
        print('Value Error')
        sys.exit(1)
if end_ == '' or end_ in '      ':
    end_ = len(string_)
else:
    try:
        end_ = int(end_)
    except ValueError:
        print('Value Error')
        sys.exit(1)

for index in range(start_, end_ - tg_len + 1):
    if string_[index:index + tg_len] == target_:
        c = c + 1

print('count using for', c)


# ----
# ---- End Using for ----
# ------------------------------------------------------
# ---- Functional Way ----
def my_count(str1, target, start=0, end=None):
    if end == None:
        end = len(str1)
    counter = 0
    tg_len = len(target)
    for index in range(start, end - tg_len + 1):
        if str1[index:index + tg_len] == target:
            counter = counter + 1
    return counter


a = my_count('alireza', 'a')
b = my_count('python programming', 'p', start=2)
c = my_count('python programming', 'p', 2, end=5)
d = my_count('alireza allday altinfo', 'al')
e = my_count('alireza allday altinfo', 'al', 2, end=23)

print(a)
print(b)
print(c)
print(d)
print(e)
# ---- End Functional Way ----
# ------------------------------------------------------
