import uzwords
from difflib import get_close_matches
from transliterate import to_latin, to_cyrillic

def to_l(matches):
    answers = []
    for match in matches:
        answers.append(to_latin(match))
    return answers

def checkWord(word, words=uzwords.words):
    word_l = False
    if word.isascii():
        word_l = True
        word = to_cyrillic(word)

    matches = set(get_close_matches(word, words))
    available = False

    if word in matches:
        available = True
        matches = word
        if word_l:
            matches = to_latin(matches)
        return {'available': available, 'matches': matches}

    elif 'ҳ' in word:
        word = word.replace('ҳ', 'х')
        matches.update(get_close_matches(word, words))
        if word_l:
            matches = to_l(matches)
        return {'available': available, 'matches': matches}

    else:
        if word_l:
            matches = to_l(matches)
        return {'available': available, 'matches': matches}


