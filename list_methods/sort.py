# ---- Sort Method ----
# ex: lst = [22, 11, 76, 34, 99, 10, 4, 68, 86]
# ex: lst.sort(reverse=False) --> [4, 10, 11, 22, 34, 68, 76, 86, 99]
# ----
# ---- sequential way ----
# ---- using while ----

# make list with input loop
lst = []   
while True:
    data = float(input("Enter the elements of the list(press 000 to make list): "))
    if data == 000:
        break
    lst = lst + [data]
# ---- End Using While ----
# ---- Using For -----
for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[j] < lst[i]:
            lst[j], lst[i] = lst[i], lst[j]
print('sort method using for: ', lst)
# ---- End Using For ----
#------------------------------------------------------
# ---- Functional Way ----

def sort(lst, reverse=False):
    if reverse == False:
        for i in range(len(lst)):
            for j in range(i+1, len(lst)):
                if lst[j] < lst[i]:
                    lst[j], lst[i] = lst[i], lst[j]
    elif reverse == True:
        for i in range(len(lst)):
            for j in range(i+1, len(lst)):
                if lst[j] > lst[i]:
                    lst[j], lst[i] = lst[i], lst[j]
    return lst

aa = sort([43, 11, 56, 3, 87, 45, 34, 67, 90, 12])
bb = sort([43, 11, 56, 3, 87, 45, 34, 67, 90, 12], reverse=True)

print(aa)
print(bb)

# ---- End Functional Way ----
#------------------------------------------------------







        
