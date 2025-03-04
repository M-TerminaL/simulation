# ---- Strip Method ----
# ex: '  alireza  '.strip() --> 'alireza'
# ex: '***ali***reza***'.strip('*') --> 'ali***reza'
# ----
string = input('Enter Your String: ')
char = input('Enter Your Char: ')
char_ = None
# ----
end = len(string) - 1
start = 0
# ---- Sequential Way ----
# ---- Using While ----
if char == '' or char in '           ':
    char_ = ' '
else:
    char_ = char

start = 0
while string[start] in char_:
    start += 1

while string[end] in char_:
    end = end - 1
print(string[start:end + 1])
# ---- End Using While ----
# ------------------------------------------------------
# ---- Sequential Way ----
# ---- Using for ----
index_start = 0
index_end = 0
for index in range(len(string)):
    if string[index] in char_:
        continue
    else:
        index_start = index
        break
for index1 in range(len(string) - 1, -1, -1):
    if string[index1] in char_:
        continue
    else:
        index_end = index1
        break
print(string[index_start:index_end + 1])


# ---- End Using for ----
# ------------------------------------------------------
# ---- Functional Way ----
def strip(string, chars=None):
    start = 0
    end = 0

    if chars == None:
        chars = ' '
    for start_idx in range(len(string)):
        if string[start_idx] in chars:
            continue
        else:
            start = start_idx
            break
    for end_idx in range(len(string) - 1, -1, -1):
        if string[end_idx] in chars:
            continue
        else:
            end = end_idx
            break

    return string[start:end + 1]


a = strip('  ali  reza   ')
b = strip('***ali***reza******', chars='*')
print(a)
print(b)

# ---- End Functional Way ----
# ------------------------------------------------------
