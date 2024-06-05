class MySet:
    def __init__(self,enumarable = []):
        self.dictionary = {}
        for value in enumarable:
            self.dictionary[value] = True

    def has(self, value):
        return value in self.dictionary
    def add(self, value):
        self.dictionary[value] = True
        return self
    def delete(self, value):
        self.dictionary.pop(value)
        return self
    def size(self):
        return len(self.dictionary)
    def clear(self):
        return self.dictionary.clear()
    def __str__(self):
        set_list = []
        for key,value in self.dictionary.items():
            set_list.append(str(key))
        return f'MySet: {{{",".join(set_list)}}}'


    pass
