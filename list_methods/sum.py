# ---- sum ----
# ex: lst = [1, 2, 3, 4, 5, 6]
# ex: sum(lst) --> 21

# ----
# ---- sequential way ----
# ---- using while ----
ref = '0123456789'
lst = []
# make list with input loop
while True:
    a = input('Enter obj to complete list: ')
    if a == 'quit':
        break
    if a in ref:
        try:
            a = int(a)
        except:
            pass
    lst = lst + [a]

i = 0
sum_ = 0
while i < len(lst):
    sum_ = sum_ + lst[i]
    i = i + 1
print('sum using while: ', sum_)
# ---- End Using While ----
# ---- Using For -----

sum__ = 0
for index in range(len(lst)):
    sum__ += lst[index]
print('sum using for: ', sum__)


# ---- End Using For ----
# ------------------------------------------------------
# ---- Functional Way ----

def personal_sum(lst):
    sum_ = 0
    for idx in range(len(lst)):
        sum_ += lst[idx]
    return sum_


aa = personal_sum([1, 2, 3, 4, 5])
print(aa)

# ---- End Functional Way ----
# ------------------------------------------------------
