import random
import os
import sys
from data.word_lists import get_word_list
from data.utils import warn

# test dictionary of
# pos => [(word, topic, plural), ...]
# words = {
#     'adj': [
#         ('funny', 'positive', None),
#         ('yellow', 'neutral', None),
#         ('slow', 'negative', None),
#         ('scary', 'negative', None),
#         ('ugly', 'negative', None)
#     ],
#     'noun': [
#         ('tent', 'camping', False),
#         ('cake', 'food', False),
#         ('uncle', 'family', False),
#         ('car', 'transportation', False),
#         ('poster', 'decorations', False),
#         ('leg', 'body_parts', False),
#         ('head', 'body_parts', False),
#         ('ears', 'body_parts', True),
#         ('Taj-Mahal', 'place', False),
#         ('Chiang Rai', 'place', False),
#         ('Moon', 'place', False),
#         ('Pluto', 'place', False),
#         ('Hawaii', 'place', False),
#         ('Tokyo', 'place', False),
#     ],
#     'verb': [
#         ('run', 'action', None),
#         ('walk', 'action', None),
#         ('jump', 'action', None),
#         ('run', 'action', None),
#         ('must', 'helping', None),
#     ]
# }

def all_words_dict():
    '''
    returns dictionary of word lists as:
    {
      'noun': [(word, topic, plural), ...],
      'verb': [(word, topic, plural), ...],
      'adj': [(word, topic, plural), ...]
    }
    '''
    current = os.path.dirname(os.path.realpath(__file__))
    parent = os.path.dirname(current)
    word_lists_dir = parent + '/words-lists/'
    words = {}
    words['noun'] = get_word_list(f'{word_lists_dir}/nouns.csv', 'tuple')
    words['verb'] = get_word_list(f'{word_lists_dir}/verbs.csv', 'tuple')
    words['adj'] = get_word_list(f'{word_lists_dir}/adjectives.csv', 'tuple')
    return words


words = all_words_dict()

# set of words chosen already
chosen = set()

# list of return values in this recursion stack
recurs = []

def randword(pos, topic=None, plural=None):
    # TODO add category
    '''
    Given a part of speech and a category, return one word of the best random match.

    The match will be guaruteed to match the part of speech only.
    '''

    # this function will recursivly try to find a word not chosen before
    # in the case of this maximum level of recursion, just return the first choice
    if len(recurs) > 5:
        return recurs[0]

    def choose(word):
        '''sets the chosen word so its not chosen again'''
        global chosen
        global recurs
        if word in chosen:  # already chosen, choose another
            recurs.append(word)
            return randword(pos, topic, plural)
        else:
            recurs = []
            chosen.add(word)
            return f'<{word}>'

    # list of words given pos
    pos_words = words[pos]

    # plural == None means we don't care whether plural or not
    if plural != None:
        tpws = [tp for tp in pos_words if topic == tp[1] and bool(plural) == bool(tp[2])]
        # matches POS, topic and plural
        if len(tpws):
            return choose(random.choice(tpws)[0])

    if topic:
        topic_words = [tp for tp in pos_words if topic == tp[1]]
        if len(topic_words) != 0:
            return choose(random.choice(topic_words)[0])
        else:
            warn(f'no word lists for pos and topic: {pos} {topic}')

    # if no topic words, fall back on random word with same POS
    return choose(random.choice(pos_words)[0])
