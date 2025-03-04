# --- Class List ---

class ListModifier:
    def __init__(self, lst):
        self.lst = lst

    def __repr__(self):
        return str(self.lst)

    def append(self, obj):
        self.lst = self.lst + [obj]

    def extend(self, iterable):
        if isinstance(iterable, list):
            self.lst = self.lst + iterable
        elif isinstance(iterable, str) or isinstance(iterable, tuple):
            self.lst = self.lst + list(iterable)

    def insert(self, index, obj):
        self.lst[index:index] = [obj]

    def pop(self, index=-1):
        value = self.lst[index]
        del self.lst[index]
        return value

    def remove(self, element):
        for index in range(len(self.lst)):
            if self.lst[index] == element:
                del self.lst[index]
                break
            
    def count(self, value):
        counter = 0
        for char in self.lst:
            if char == value:
                counter += 1
        return counter

    def index(self, value, start=0, stop=None):
        idx = 'Not Found'
        if stop == None:
            stop = len(self.lst)
        for index in range(start, stop):
            if self.lst[index] == value:
                idx = index
                break
        return idx

    def clear(self):
        del self.lst[:len(self.lst)]

    def sort(self, reverse=False):
        if reverse is False:
            for i in range(len(self.lst)):
                for j in range(i+1, len(self.lst)):
                    if self.lst[j] < self.lst[i]:
                        self.lst[j], self.lst[i] = self.lst[i], self.lst[j]
        if reverse is True:
            for i in range(len(self.lst)):
                for j in range(i+1, len(self.lst)):
                    if self.lst[j] > self.lst[i]:
                        self.lst[j], self.lst[i] = self.lst[i], self.lst[j]
                         
                        

    
                

    

    
            
                
        
        

        
        
