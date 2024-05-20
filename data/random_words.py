import random

# test dictionary of
# pos => [(word, topic, plural), ...]
# TODO: this data will be queried from a database
words = {
    'adj': [
        ('funny', '', False),
        ('yellow', 'colors', False),
        ('slow', '', False),
        ('scary', '', False),
        ('ugly', '', False)
    ],
    'noun': [
        ('tent', 'camping', False),
        ('cake', 'food', False),
        ('uncle', 'family', False),
        ('car', 'transportation', False),
        ('poster', 'decorations', False),
        ('leg', 'body_parts', False),
        ('head', 'body_parts', False),
        ('ears', 'body_parts', True),
        ('Taj-Mahal', 'place', False),
        ('Chiang Rai', 'place', False),
        ('Moon', 'place', False),
        ('Pluto', 'place', False),
        ('Hawaii', 'place', False),
        ('Tokyo', 'place', False),
    ]
}

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
            return word

    # list of words given pos
    pos_words = words[pos]

    # plural == None means we don't care whether plural or not
    if plural != None:
        tpws = [tp for tp in pos_words if topic == tp[1] and bool(plural) == bool(tp[2])]
        # matches POS, topic and plural
        return choose(random.choice(tpws)[0])

    if topic:
        topic_words = [tp for tp in pos_words if topic == tp[1]]
        if len(topic_words) != 0:
            return choose(random.choice(topic_words)[0])

    # if no topic words, fall back on random word with same POS
    return choose(random.choice(pos_words)[0])
