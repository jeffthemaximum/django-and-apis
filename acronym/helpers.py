import re
import pudb
from requests import get


class ApiGet(object):
    def __init__(self, url, request):
        self.url = url
        self.request = request

    def get_string_response(self):
        r = get(self.url).text
        return r

    def get_json_response(self):
        r = get(self.url).json()
        return r

text = "sb ba"


def get_acronym_api(acronym):
    # pu.db
    url = "http://www.nactem.ac.uk/software/acromine/dictionary.py?sf="
    r = get(url + acronym).json()
    return r


def words_as_list(text):
    return text.split(" ")


def format_words(text):
    for i, word in enumerate(text):
        if re.search('[a-zA-Z]', word):
            # strip whitespace
            word = word.strip()
            # remove trailing punctuation
            word = word.rstrip("?:!.,;()\"\'")
            word = word.lstrip("?:!.,;()\"\'")
            if any(i in '?:!.,;()\"\'-/' for i in word):
                # check words split by punctuation
                for c in word:
                    if c.isalpha() is not True:
                        # cut of symbol and replace with space
                        word = word.replace(c, " ")
                        # split two words into array of individual words
                        words = word.split(" ")
                        # add individual words to text
                        text.append(words[0])
                        # delete original word from lsit
                        text[i] = words[1]
            else:
                text[i] = word
        else:
            text.remove(word)
    print "format words: " + str(text)
    return text


def spell_check(text):
    # load words into dict
    words = {}
    mispelled_words = []
    with open("/Users/curtisfinnigan/Dropbox/projects/apis/acronym/words.txt") as f:
        for line in f:
            word = line
            words[word.rstrip()] = True
    # iterate over text
    individual_words = words_as_list(text)
    words_without_punctuation = format_words(individual_words)
    for word in words_without_punctuation:
        # make word lowercase to check against all words
        word = word.lower()
        # if word not in dict, add to mispelled words list
        if word in words:
            pass
        else:
            mispelled_words.append(word)
            rs = get_acronym_api(word)
            for i in range(len(rs[0]["lfs"])):
                print "possible acronym: " + rs[0]["lfs"][i]["lf"]
    print mispelled_words

    # return mispelled words
    return mispelled_words

print spell_check(text)
