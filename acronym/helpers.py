import re
import pudb

text = "Hi all - some of you may have experienced a few headaches over the past two weeks as we began to implement our new Google Admin software (GoGuardian). I apologize for the rocky start, which ended-up w/us rolling back most restrictions. After learning more about the product, we're now planning to reconfigure the filter & implement the program. (if you'd like know more about CIPA compliance, please see attached) What I could really use fm/staff is a list of sites that you use in the classroom, so I can be sure to white-list those right fm/the start. At the MS, please direct that to Jeff, so he can consolidate the list. HS folks, you can let me know directly. Students' user accounts will obviously be more rigorously controlled, so again, if there's something you want your kids to be able to use in class, please let us know that too. By the way, besides the filtering (access control) component, GoGuardian also has a great Teacher Dashboard app, which if you're using the CBooks in your classroom, you'll absolutely love. Please see either Jeff or myself to learn more."


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
    print mispelled_words

    # return mispelled words
    return mispelled_words

print spell_check(text)