# ---- index Method ----
# ex: data = (1, 2, 3, 1, 4, 1)
# ex: data.index(1, start=1, stop=len(data)) --> 3
# ----
#------------------------------------------------------
# ---- Functional Way ----

def index(tuple_, value, start=0, stop=None):
    idx = None
    if stop == None:
        stop = len(tuple_)
    for index in range(start, stop):
        if tuple_[index] == value:
            idx = index
            break
    return idx

a = index(('a', 'b', 'c', 'b', 'd'), 'b', start=2, stop=5)
b = index(('a', 'b', 'c', 'b', 'd'), 'z')
c = index(('a', 'b', 'c', 'b', 'd'), 'b')

print(a)
print(b)
print(c)

# ---- End Functional Way ----
#------------------------------------------------------







        
