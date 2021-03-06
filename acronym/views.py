from django.shortcuts import render, redirect
from .forms import TextForm
from requests import get
import re


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
            # check if punctuation in the middle of word, and check that it's not an I contraction
            if any(i in '?:!.,;()\"\'-/' for i in word) and word[0] != "I":
                # check words split by punctuation
                for c in word:
                    if c.isalpha() is not True:
                        # cut of symbol and replace with space
                        word = word.replace(c, " ")
                        # split two words into array of individual words
                        words = word.split(" ")
                        # check if split word is just two letters, if so, join, something like s/b
                        if len(words[0]) == 1 and len(words[1]) == 1:
                            text[i] = words[0] + words[1]
                        #check if one of the split words is just one letter, if so, chuck it, something like they'd
                        # elif len(words[0]) == 1:
                        #     text[i] = words[1]
                        elif len(words[1]) == 1:
                            text[i] = words[0]
                        # else, split words
                        else:
                            # add individual words to text
                            text.append(words[0])
                            # delete original word from lsit
                            text[i] = words[1]
            else:
                text[i] = word
        else:
            text[i] == word
    print "format words: " + str(text)
    return text


def get_acronym_api(acronym):
    url = "http://www.nactem.ac.uk/software/acromine/dictionary.py?sf="
    try:
        r = get(url + acronym).json()
    except:
        r = []
    return r


def parse_acronyms(word):
    acronyms = []
    rs = get_acronym_api(word)
    if rs != []:
        for i in range(len(rs[0]["lfs"])):
            acronym = rs[0]["lfs"][i]["lf"]
            acronyms.append(acronym)
        return acronyms
    else:
        return None


def strip_non_ascii(string):
    ''' Returns the string without non ASCII characters'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)


def spell_check(text):
    # remove non ascii chars
    text = strip_non_ascii(text)
    # load words into dict
    words = {}
    mispelled_words = []
    # acronym_list = []
    with open("acronym/words.txt") as f:
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
        if word in words or any(c.isalpha() for c in word) is not True:
            pass
        else:
            # get possible acronyms
            acronyms = parse_acronyms(word)
            # add word and acronyms to list
            mispelled_words.append([word, acronyms])

    # mispelled_words.sort(lambda x, y: cmp(len(y), len(x)))
    print mispelled_words

    # return mispelled words
    return mispelled_words


# Create your views here.
def acronym_index(request):
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            text = request.POST['input']
            # spell check text
            mispelled_words = spell_check(text)
            # check mispelled words in acronym api

            # check mispelled words in abbreviation api

            # return text, acronym suggestions, abbreviation suggestions
            return render(request, 'acronym/acronym_response.html', {'text': text, 'mispelled_words': mispelled_words})
    else:
        form = TextForm()
    return render(request, 'acronym/acronym_index.html', {'form': form})
