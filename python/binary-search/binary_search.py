def binary_search(list_of_numbers, number):
    low = 0
    high = len(list_of_numbers)
    while low != high :
        mid = (low+high)//2
        #print(low,mid,high)
        #if(mid == low or mid == high):break
        if( list_of_numbers[mid] < number):
            low = mid + 1
        elif( list_of_numbers[mid] > number ):
            high = mid
        else :return mid
    raise ValueError("Error Value Not Found")


print(binary_search([1, 3, 4, 6, 8, 9, 11], 1))
