def hey(phrase):
    phrase = phrase.strip()
    if(phrase.strip() == ""):
        return "Fine. Be that way!"
    if(phrase.upper() == phrase and any(c.isalpha() for c in phrase)  ):
        if(phrase[-1] == "?"  ):
            return "Calm down, I know what I'm doing!"
        return "Whoa, chill out!"
    if(phrase[-1] == "?"):
        return "Sure."
    return "Whatever."
