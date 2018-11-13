def is_armstrong(number):
    power = len(str(number))
    ans = 0
    saved_num = number
    while number > 0:
        ans = ans + ((number % 10) ** power)
        number = number // 10
    return ans == saved_num
