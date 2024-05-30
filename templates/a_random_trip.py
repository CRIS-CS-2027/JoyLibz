import os
import sys
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from data.random_words import randword

mad_text = f'''Candy loves to {randword('verb', 'action')} at the {randword('noun', 'place')} with Prim. 
They would {randword('verb', 'action')} the {randword('adj')} {randword('noun')} and {randword('verb', 'action')} the {randword('noun', 'True')}.
Everytime they go there, Amy will {randword('verb')} at the {randword('noun', 'animals')}.
That's why you should always go secretly.'''