
def recur_extractor(l):
    ans = []
    if(l == None):return []
    if(type(l) == tuple):return []
    if(type(l) != list):return [l]
    for i in l:
        if(type(l) == list or type(l) == tuple):
            ans = ans + recur_extractor(i)
        elif(l == None):
            continue
        else:
            ans = ans + [i]
    return ans


def flatten(iterable):
    return recur_extractor(iterable)
