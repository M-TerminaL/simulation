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
limit_counter = 1
result = ''
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
    if string[i] == old:
        if limit_counter <= count_:
            result = result + new
            limit_counter += 1
            i += 1
        elif count_ == -1:
            result = result + new
            i += 1
        else:
            result = result + string[i]
            i += 1
    else:
        result = result + string[i]
        i += 1
    
print('using while: ', result)
# ---- End Using While ----
#------------------------------------------------------
# ---- Sequential Way ----
# ---- Using for ----
res = ''
count_ = None
limit_counter = 1

if count in '           ' or count == '':
    count_ = -1
else:
    try:
        count_ = int(count)
    except ValueError:
        print('value error')
        sys.exit(1)


for element in string:
    if element == old:
        if limit_counter <= count_:
            res = res + new
            limit_counter += 1
        elif count_ == -1:
            res = res + new
        else:
            res = res + element
    else:
        res = res + element
print('using for: ', res)
# ---- End Using for ----
#------------------------------------------------------
# ---- Functional Way ----

def replace(word, old, new, count=-1):
    fp_result = ''
    limit_counter = 1
    for char in word:
        if char == old:
            if limit_counter <= count:
                fp_result += new
                limit_counter += 1
            elif count == -1:
                fp_result += new
            else:
                fp_result += char
        else:
            fp_result = fp_result + char
    return fp_result
            
a = replace('python programming', 'p', '(***)')
b = replace('python programming', 'p', '(***)', count=1)
print(a)
print(b)

# ---- End Functional Way ----
#------------------------------------------------------







        
