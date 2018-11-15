def is_pangram(sentence):
    sentence = sentence.lower()
    final = ""
    for i in sentence :
        if(i.isalpha()):final+=i
    return len(set(final)) == 26
