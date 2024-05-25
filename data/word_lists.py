import csv
from pprint import pprint

def dict_val(row):
    '''returns given csv.DictReader row as a dictionary'''
    try:
        row['plural'] = bool(int(row['plural']))
    except:
        row['plural'] = None
    return row

def tuple_val(row):
    '''returns given csv.DictReader row as a tuple'''
    row = dict_val(row)
    return (row['word'], row['topic'], row['plural'])

def get_word_list(filename, item_type='dict'):
    """
    opens CSV file and returns list of <item_type> data
    where <item_type> in ('dict', 'tuple')
    """
    val_func = dict_val if item_type=='dict' else tuple_val

    with open(filename, encoding ='utf-8') as words:
        words_list = []
        reader = csv.DictReader(words, skipinitialspace=True)
        for row in reader:
            words_list += [val_func(row)]
        return words_list

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        fname = sys.argv[1]
    else:
        fname = "../words-lists/nouns.csv"
    dict_list = get_word_list(fname)
    pprint(dict_list)

    tuple_list = get_word_list(fname, 'tuple')
    pprint(tuple_list)