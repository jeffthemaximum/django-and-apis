from django.shortcuts import render, redirect
from .forms import TextForm
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
        if word in words:
            pass
        else:
            mispelled_words.append(word)
    mispelled_words.sort(lambda x, y: cmp(len(y), len(x)))
    print mispelled_words

    # return mispelled words
    return mispelled_words


# Create your views here.
def acronym_index(request):
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            text = request.POST['email']
            print text
            # spell check text
            mispelled_words = spell_check(text)
            # check mispelled words in acronym api

            # check mispelled words in abbreviation api

            # return text, acronym suggestions, abbreviation suggestions
            return render(request, 'acronym/acronym_response.html', {'text': text, 'mispelled_words': mispelled_words})
    else:
        form = TextForm()
    return render(request, 'acronym/acronym_index.html', {'form': form})
