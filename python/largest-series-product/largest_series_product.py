
def multiplier(string):
    ans = 1
    for i in string:ans *= int(i)
    return ans


def largest_product(series, size):
    if( any([ i.isalpha() for i in series ]) ):raise ValueError("Series can Contain Numbers only")
    if(len(series) < size):raise ValueError("Series not possible")
    if(size < 0):raise ValueError("Enter Valid Series Integer")
    if(size == 0):return 1
    max_Value = 0
    for i in range(0 , len(series) - size + 1):
        max_Value = max(max_Value , multiplier( series[i : i+size ] ) )
    return max_Value
