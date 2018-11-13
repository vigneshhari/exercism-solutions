import string
mapper = {}
for i, v in enumerate(string.ascii_lowercase):
    mapper[v] = i
    mapper[i] = v
def encode(plain_text, a, b):
    if a%2==0 or a%13==0:
        raise ValueError("Error: a and m must be coprime.")
    cipher_text = ''
    plain_text = ''.join(plain_text.split())
    for x in plain_text:
        if(x.isnumeric()):cipher_text+=x;continue
        if(x.lower() not in mapper.keys()):continue
        x = mapper[x.lower()]
        E = (a*x +b) % 26
        cipher_text += mapper[E]
    return ' '.join([cipher_text[i:i+5] for i in range(0,len(cipher_text),5)])

def modInverse(a, m) :
    a = a % m;
    for x in range(1, m) :
        if ((a * x) % m == 1) :
            return x
    return 1

def decode(ciphered_text, a, b):
    if a%2==0 or a%13==0:
        raise ValueError("Error: a and m must be coprime.")
    ans = ""
    for i in ciphered_text:
        if(i.isnumeric()):ans+=i;continue
        if(i.lower() not in mapper.keys()):continue
        ans +=  mapper[modInverse(a,26) *  (mapper[i] - b) % 26]
    return ans
