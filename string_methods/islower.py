# ---- islower Method ----
# ex: 'AliReZa'.islower() --> False
# ex: 'alireza'.islower() --> True
# ex: 'ALIREZA'.islower() --> False
# ----

# ---- sequential way ----
# ---- using while ----
string = input('Enter your String: ')
i = 0
ref1 = 'abcdefghijklmnopqrstuvwxyz'
ref2 = '0123456789'
ref3 = '!@#$%^&*()_ -+=][;:.,<>?{}'

result = None
while i < len(string):
    if string[i] in ref1 or string[i] in ref2 or string[i] in ref3:
        result = True
        i = i + 1
    else:
        result = False
        break
print('isupper method using while', result)
# ---- End Using While ----
# ------------------------------------------------------
# ---- Sequential Way ----
# ---- Using for ----
flag = 1
for char in string:
    if char in ref1 or char in ref2 or char in ref3:
        flag = 1
    else:
        flag = 0
        break
print('isupper method using for', bool(flag))


# ----
# ---- End Using for ----
# ------------------------------------------------------
# ---- Functional Way ----
def islower(string: str) -> bool:
    # Type Checking
    if not isinstance(string, str):
        return
    # just with senior commands
    ref1 = 'abcdefghijklmnopqrstuvwxyz'
    ref2 = '0123456789'
    ref3 = '!@#$%^&*()_ -+=][;:.,<>?{}'
    flag = True
    for char in string:
        if char in ref1 or char in ref2 or char in ref3:
            flag = True
        else:
            flag = False
            break
    return flag


a = islower('alireza')
b = islower('alireza python 786')
c = islower('aliReza')

print(a)
print(b)
print(c)
# ---- End Functional Way ----
# ------------------------------------------------------
