def recite(start_verse, end_verse):
    a =  [verse(v) for v in range(start_verse-1, end_verse)]
    ans = []
    if(len(a) == 1):
        return a[0]
    for i in a:
        for x in i:
            ans.append(x)
        ans.append("")
    return ans[:-1]


animals = (
    ("fly", "", ""),
    ("spider", "It wriggled and jiggled and tickled inside her.",
        " that wriggled and jiggled and tickled inside her"),
    ("bird", "How absurd to swallow a bird!", ""),
    ("cat", "Imagine that, to swallow a cat!", ""),
    ("dog", "What a hog, to swallow a dog!", ""),
    ("goat", "Just opened her throat and swallowed a goat!", ""),
    ("cow", "I don't know how she swallowed a cow!", ""),
    ("horse", "She's dead, of course!", ""),)


end = "I don't know why she swallowed the fly. Perhaps she'll die."


def verse(v):

    words = ["I know an old lady who swallowed a {}.".format(animals[v][0])]
    if(animals[v][1] != ""):
        words.append(animals[v][1])

    if v == 7:
        return words

    for i in range(v-1, -1 , -1):
        words.append("She swallowed the {} to catch the {}{}.".format(
            animals[i+1][0], animals[i][0], animals[i][2]))

    return words + [end]
