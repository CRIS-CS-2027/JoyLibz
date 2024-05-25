import csv

def get_word_list(filename):
    """
    A function that opens a CSV file and returns a list of dictionaries of data
    """
    with open(filename, encoding ='utf-8') as words:
        words_list = []
        reader = csv.DictReader(words, skipinitialspace=True)
        for row in reader:
            row['plural'] = bool(int(row['plural']))
            words_list += [row]
        return words_list

if __name__ == '__main__':
    my_list = get_word_list("../words-lists/nouns.csv")
    print(my_list)