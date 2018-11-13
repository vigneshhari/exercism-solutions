class CustomSet(object):

    elements = []

    def __init__(self, elements=[]):
        self.elements = []
        for i in elements:
                if(i not in self.elements):
                    self.elements.append(i)

    def isempty(self):
        return len(self.elements) == 0

    def __contains__(self, element):
        return element in self.elements

    def issubset(self, other):
        for i in self.elements:
            if(i not in other.elements):return False
        return True

    def isdisjoint(self, other):
        for i in self.elements:
            if(i in other.elements):return False
        return True

    def __eq__(self, other):
        if(len(self.elements) != len(other.elements) ):return False
        for i in self.elements:
            if(i not in other.elements):return False
        return True

    def add(self, element):
        if(element not in self.elements):self.elements.append(element)

    def intersection(self, other):
        newset = CustomSet()
        for i in other.elements:
            if(i in self.elements):
                newset.add(i)
        return newset

    def difference(self, other):
        pass

    def union(self, others):
        pass

    def __add__(self, other):
        ans = CustomSet(self.elements)
        for i in other.elements:
            ans.add(i)
        return ans


    def __sub__(self,other):
        ans = CustomSet()
        for i in self.elements:
            if(i in other.elements):continue
            ans.add(i)
        return ans
