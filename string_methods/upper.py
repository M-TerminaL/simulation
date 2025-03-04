# ---- Upper Method ----
# Return a Copy of The String Converted To
# ex: 'alireza'.upper() --> 'ALIREZA'
# ----
string = input('Enter Your String: ')

lower_ref = 'abcdefghijklmnopqrstuvwxyz'
upper_ref = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# ---- Sequential Way ----
# ---- Using While ----
result = ''
i = 0
while i < len(string):
    if string[i] in lower_ref:
        j = 0
        while j < len(lower_ref):
            if string[i] == lower_ref[j]:
                result = result + upper_ref[j]
                i = i + 1
                break
            else:
                j = j + 1
    else:
        result += string[i]
        i += 1
print('using while: ', result)
# ---- End Using While ----
# ------------------------------------------------------
# ---- Sequential Way ----
# ---- Using for ----
res = ''
for index in range(len(string)):
    if string[index] in lower_ref:
        for lower_index in range(len(lower_ref)):
            if string[index] == lower_ref[lower_index]:
                res = res + upper_ref[lower_index]
    else:
        res = res + string[index]
print('using for: ', res)


# ---- End Using for ----
# ------------------------------------------------------
# ---- Functional Way ----
def personal_upper(str1: str) -> str:
    if not isinstance(str1, str):
        return
    lower_ref = 'abcdefghijklmnopqrstuvwxyz'
    upper_ref = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    upper_result = ''
    for element in str1:
        if element in lower_ref:
            for index in range(len(lower_ref)):
                if element == lower_ref[index]:
                    upper_result += upper_ref[index]
        else:
            upper_result += element
    return upper_result


a = personal_upper('aLiReZa13!?')
print(a)

# ---- End Functional Way ----
# ------------------------------------------------------
