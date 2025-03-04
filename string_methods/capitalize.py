# ---- capitalize Method ----
# ex: 'pyThon Coding'.capitalize() --> Python coding
# ----
# ---- sequential way ----
# ---- using while ----
string = input('Enter Your String: ')
upper_ref = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_ref = 'abcdefghijklmnopqrstuvwxyz'
result = ''

if string[0] in lower_ref:
    j = 0
    while j < len(lower_ref):
        if string[0] == lower_ref[j]:
            result = result + upper_ref[j]
            break
        else:
            j = j + 1
else:
    result = result + string[0]

i = 1
while i < len(string):
    if string[i] in upper_ref:
        k = 0
        while k < len(upper_ref):
            if string[i] == upper_ref[k]:
                result = result + lower_ref[k]
                i = i + 1
                break
            else:
                k = k + 1
    else:
        result = result + string[i]
        i = i + 1
print('capitalize method using while: ', result)
# ---- End Using While ----
# ------------------------------------------------------
# ---- Sequential Way ----
# ---- Using for ----
res = ''
if string[0] in lower_ref:
    for lower_idx in range(len(lower_ref)):
        if lower_ref[lower_idx] == string[0]:
            res = res + upper_ref[lower_idx]
            break
else:
    res = res + string[0]

for i in range(1, len(string)):
    if string[i] in upper_ref:
        for j in range(len(upper_ref)):
            if string[i] == upper_ref[j]:
                res = res + lower_ref[j]
                break
    else:
        res = res + string[i]
print('capitalize method using for: ', res)


# ----
# ---- End Using for ----
# ------------------------------------------------------
# ---- Functional Way ----
def capitalize(string: str) -> str:
    upper_ref = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_ref = 'abcdefghijklmnopqrstuvwxyz'
    res = ''
    if not isinstance(string, str):
        return
    if string[0] in lower_ref:
        for lower_idx in range(len(lower_ref)):
            if lower_ref[lower_idx] == string[0]:
                res = res + upper_ref[lower_idx]
                break
    else:
        res = res + string[0]

    for i in range(1, len(string)):
        if string[i] in upper_ref:
            for j in range(len(upper_ref)):
                if string[i] == upper_ref[j]:
                    res = res + lower_ref[j]
                    break
        else:
            res = res + string[i]
    return res


a = capitalize('alireZa BabaEi')
print(a)

# ---- End Functional Way ----
# ------------------------------------------------------
