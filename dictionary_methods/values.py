# ---- values Method ----
# ex: data = {'a': 1, 'b': 2, 'c': 3}
# ex: data.values() --> [1 ,2, 3]
# ----
#------------------------------------------------------
# ---- Functional Way ----

def values(dictionary):
    lst = []
    for key in dictionary:
        lst = lst + [dictionary[key]]
    return lst

a = values({'a': 1, 'b': 2, 'c': 3, 'd': 4})
print(a)
    
# ---- End Functional Way ----
#------------------------------------------------------







        
