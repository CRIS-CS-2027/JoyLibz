import os
import sys
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from data.random_words import randword

# modified public domain poem 
# She Walks in Beauty, by Lord Byron
# https://hitrecord.org/records/3565436

mad_text = f'''Her {randword('noun', 'body_parts')} in beauty, like the {randword('noun', 'place')} 
Of {randword('adj', 'action')} climes and {randword('adj', '')} skies
And all that’s {randword('adj', 'action')} of {randword('adj', '')} and {randword('adj', 'action')}
Meet in her aspect and her {randword('noun', 'body_parts')} Thus mellowed to that tender {randword('noun', '')}
Which heaven to {randword('adj', 'action')} {randword('noun', '')} denies.'''