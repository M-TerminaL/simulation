# --- Class Str ---

class StringModifiers:
    def __init__(self, string):
        self.string = string
        self.lower_ref = 'abcdefghijklmnopqrstuvwxyz'
        self.upper_ref = 'ABCDEFDHIJKLMNOPQRSTUVWXYZ'

    def __repr__(self):
        return self.string

    def lower(self):
        result = ''
        for index1 in range(len(self.string)):
            if self.string[index1] in self.upper_ref:
                for index2 in range(len(self.upper_ref)):
                    if self.string[index1] == self.upper_ref[index2]:
                        result = result + self.lower_ref[index2]
            else:
                result = result + self.string[index1]
        return result

    def upper(self):
        result = ''
        for index1 in range(len(self.string)):
            if self.string[index1] in self.lower_ref:
                for index2 in range(len(self.lower_ref)):
                    if self.string[index1] == self.lower_ref[index2]:
                        result = result + self.upper_ref[index2]
            else:
                result = result + self.string[index1]
        return result

    def islower(self):
        result = False
        for char in self.string:
            if char in self.upper_ref:
                result = False
                break
            else:
                result = True
        return result

    def isupper(self):
        result = False
        for char in self.string:
            if char in self.lower_ref:
                result = False
                break
            else:
                result = True
        return result

    def find(self, target, start=0, stop=None):
        target_len = len(target)
        index = -1
        if stop == None:
            stop = len(self.string)
        for idx in range(start, stop - target_len + 1):
            if self.string[idx:idx + target_len] == target:
                index = idx
                break
        return index

    def count(self, target, start=0, stop=None):
        target_len = len(target)
        counter = 0
        if stop == None:
            stop = len(self.string)
        for index in range(start, stop - target_len + 1):
            if self.string[index:index + target_len] == target:
                counter = counter + 1
        return counter

    def index(self, target, start=0, stop=None):
        target_len = len(target)
        index = None
        if stop == None:
            stop = len(self.string)
        for idx in range(start, stop - target_len + 1):
            if self.string[idx:idx + target_len] == target:
                index = idx
                break
        return index

    def replace(self, old, new, count=-1):
        result = ''
        old_len = len(old)
        limit_counter = 0
        i = 0
        while i < len(self.string):
            if self.string[i:i + old_len] == old and limit_counter < count:
                result = result + new
                i = i + old_len
                limit_counter += 1
            elif self.string[i:i + old_len] == old and count == -1:
                result = result + new
                i = i + old_len
            else:
                result = result + self.string[i]
                i = i + 1
        return result

    def strip(self, chars=None):
        start = 0
        stop = len(self.string)
        if chars is None:
            chars = ' '
        for idx_start in range(0, len(self.string)):
            if self.string[idx_start] == chars:
                continue
            else:
                start = idx_start
                break
        for idx_end in range(len(self.string) - 1, -1, -1):
            if self.string[idx_end] == chars:
                continue
            else:
                stop = idx_end
                break
        return self.string[start:stop + 1]

    def capitalize(self):
        result = ''
        if self.string[0] in self.lower_ref:
            for index1 in range(len(self.lower_ref)):
                if self.string[0] == self.lower_ref[index1]:
                    result = result + self.upper_ref[index1]
                    break
        else:
            result = result + self.string[0]
        i = 1
        while i < len(self.string):
            if self.string[i] in self.upper_ref:
                for index2 in range(len(self.upper_ref)):
                    if self.string[i] == self.upper_ref[index2]:
                        result = result + self.lower_ref[index2]
                        i = i + 1

            else:
                result = result + self.string[i]
                i = i + 1

        return result
