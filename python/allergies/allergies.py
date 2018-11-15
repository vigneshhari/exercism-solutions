


class Allergies(object):

    allergies = {"eggs" : 1 ,"peanuts" : 2 , "shellfish" : 4  ,"strawberries" : 8 ,"tomatoes" : 16, "chocolate" : 32 ,"pollen" : 64 , "cats" : 128}
    allergies_reverse = {64: 'pollen', 1: 'eggs', 2: 'peanuts', 4: 'shellfish', 16: 'tomatoes', 32: 'chocolate', 8: 'strawberries', 128: 'cats'}

    score = 0

    def __init__(self, score):
        self.score = score

    def is_allergic_to(self, item):
        return item in self.lst

    @property
    def lst(self):
        temp = self.score
        ans = []
        for i in sorted(self.allergies_reverse.keys() , reverse=True):
            if(temp < i):continue
            else:
                ans += [self.allergies_reverse[i]]
                temp -= (temp // i) * i
        return ans

a = Allergies(509)
print(a.lst)
