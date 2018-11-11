def verify(isbn):
    isbn = list("".join(isbn.split("-")))
    if(len(isbn) != 10 ):return False
    for i in isbn[:9]:
        if(i.isalpha()):return False
    if(isbn[-1].isalpha()):
        if(isbn[-1] != "X"):return False
    if(isbn[-1] == "X"):isbn[-1] = 10
    isbn = list(map(int,isbn))
    return sum([ (10 - i) * isbn[i] for i in range(10) ]) % 11 == 0
