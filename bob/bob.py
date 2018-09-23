def hey(phrase):
    phrase = phrase.strip()
    question = bool(phrase.endswith('?'))
    yell = bool(phrase.isupper())
    if not phrase:
        return 'Fine. Be that way!'
    elif question and yell:
        return 'Calm down, I know what I\'m doing!'
    elif question:
        return 'Sure.'
    elif yell:
        return 'Whoa, chill out!'
    else:
        return 'Whatever.'
