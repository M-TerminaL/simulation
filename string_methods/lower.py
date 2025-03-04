# ---- Lower Method ----
# Return a Copy of The String Converted To
# ex: 'ALIREZA'.lower() --> 'alireza'
# ----
string = input('Enter Your String: ')

lower_ref = 'abcdefghijklmnopqrstuvwxyz'
upper_ref = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# ---- Sequential Way ----
# ---- Using While ----
result = ''
i = 0
while i < len(string):
    if string[i] in upper_ref:
        j = 0
        while j < len(upper_ref):
            if string[i] == upper_ref[j]:
                result = result + lower_ref[j]
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
    if string[index] in upper_ref:
        for upper_index in range(len(upper_ref)):
            if string[index] == upper_ref[upper_index]:
                res = res + lower_ref[upper_index]
    else:
        res = res + string[index]
print('using for: ', res)


# ---- End Using for ----
# ------------------------------------------------------
# ---- Functional Way ----
def personal_lower(str1: str) -> str:
    if not isinstance(str1, str):
        return
    lower_ref = 'abcdefghijklmnopqrstuvwxyz'
    upper_ref = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_result = ''
    for element in str1:
        if element in upper_ref:
            for index in range(len(upper_ref)):
                if element == upper_ref[index]:
                    lower_result += lower_ref[index]
        else:
            lower_result += element
    return lower_result


a = personal_lower('AlIRezA432GFsdvJFB')
print(a)

# ---- End Functional Way ----
# ------------------------------------------------------
