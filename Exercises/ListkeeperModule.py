class ListKeeper:
    listDict = dict()
    def __init__(self):
        """initializes the dictionary with a list named example"""
        self.listDict = {"example": [1,2,3,4,5]}

    def show(self):
        """returns all list names"""
        list = []
        for x in self.listDict:
            list.append(x)
        return list

    def add(self,name, list):
        """adds a new list"""
        self.listDict[name] = list

    def delete(self,name):
        """deletes list"""
        self.listDict.pop(name)

    def sort (self, name):
        """returns the sorted list *name*"""
        return self.listDict[name].sort()

    def append (self, name, list):
        """ appends *list* to *name* """
        self.listDict[name].extend(list)