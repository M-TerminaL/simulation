# ---- count Method ----
# ex: data = (1, 2, 3, 1, 4, 1)
# ex: data.count(1) --> 3
# ----
#------------------------------------------------------
# ---- Functional Way ----

def count(set_, value):
    counter = 0
    for elem in set_:
        if elem == value:
            counter += 1
    return counter
        

a = count((1, 2, 3, 4, 1, 2, 11, 1, 6), 1)
b = count((1, 2, 3, 4, 1, 2, 11, 1, 6), 66)

print(a)
print(b)

# ---- End Functional Way ----
#------------------------------------------------------







        
