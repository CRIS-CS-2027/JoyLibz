import os
import sys
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from data.random_words import randword

mad_text = f'''Every year, you should go visit the doctor. It is a very {randword('adj')} visit.
Usually, you have to skip going to {randword('noun','places')} to go. Your doctor is usually
a/an {randword('adj')} man or woman who is wearing a/an {randword('adj','color')} {randword('noun')}.
They will look at your {randword('noun','body_parts')}, {randword('noun','body_parts')}, and {randword('noun','body_parts')}.
Sometimes, they can be very {randword('adj')} . Afterwards, they will give you a {randword('noun')}
 and a {randword('noun')} and your mom or dad will take you to {randword('noun')}
 as a treat. All in all, the doctor's office isn't so {randword('adj')}!'''

print(mad_text)