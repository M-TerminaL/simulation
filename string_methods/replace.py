import sys

# ---- Replace Method ----
# ex: 'alireza'.replace(old(a), new(i), count=-1) --> 'ilirezi'
# ----

# ----

# ---- Sequential Way ----
# ----
string = input('Enter Your String: ')
old = input('old: ')
new = input('new: ')
count = input('count: (def=-1) ')

# ---- Using While ----
count_ = None
limit_counter = 0
result = ''
old_len = len(old)
i = 0

if count in '           ' or count == '':
    count_ = -1
else:
    try:
        count_ = int(count)
    except ValueError:
        print('value error')
        sys.exit(1)

while i < len(string):
    if string[i:i + old_len] == old and limit_counter < count_:
        result += new
        limit_counter += 1
        i += old_len
    elif string[i:i + old_len] == old and count_ == -1:
        result += new
        i += old_len
    else:
        result += string[i]
        i += 1

print('using while: ', result)


# ---- End Using While ----
# ------------------------------------------------------
# ---- Functional Way ----

def replace(word, old, new, count=-1):
    fp_result = ''
    old_len = len(old)
    limit_counter = 0
    i = 0
    while i < len(word):
        if word[i:i + old_len] == old and limit_counter < count:
            fp_result += new
            limit_counter += 1
            i += old_len
        elif word[i:i + old_len] == old and count == -1:
            fp_result += new
            i += old_len
        else:
            fp_result += word[i]
            i += 1

    return fp_result


a = replace('python programming', 'p', '(***)')
b = replace('python programming', 'p', '(***)', count=1)
c = replace('ali alireza all', 'al', '(***)', count=2)
d = replace('ali alireza all', 'al', '(***)')

print(a)
print(b)
print(c)
print(d)
# ---- End Functional Way ----
# ------------------------------------------------------
