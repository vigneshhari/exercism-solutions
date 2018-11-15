import collections

def word_count(phrase):
    phrase = " " + phrase.lower() + " "
    phrase = " ".join(phrase.split("_"))
    phrase = " ".join(phrase.split(","))
    new_phrase = ""
    for i in range(0,len(phrase)):
        if(phrase[i] == "'"):
            if(phrase[i-1].isalpha() and phrase[i+1].isalpha() ):
                new_phrase += phrase[i]
        if(phrase[i].isalpha() or phrase[i].isnumeric() ):
            new_phrase += phrase[i]
        if(phrase[i] in [" " , "\t" , "\n"]):
            new_phrase += " "
    phrase = new_phrase
    count = collections.defaultdict(int)
    for i in phrase.split():
        count[i]+=1
    return dict(count)
