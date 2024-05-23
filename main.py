import csv

def get_word_list(filename):
    """
    A function that opens a CSV file and returns a list of dictionaries of data
    """
    with open(filename, encoding ='utf-8') as words:
        words_list = []
        reader = csv.DictReader(words, skipinitialspace=True)
        for row in reader:
        #     print(row)
        #     for words in row.items():
        #         for letter in words:
        #             if letter == 0:
        #                 letter == "False"
        #             elif letter == 1:
        #                 letter == "True"
        #             print(letter)
            words_list += [row]
        return words_list

my_list = get_word_list("words-lists/nouns.csv")

for list in my_list:
    for words in list.items():
        for plural in words:
            if plural == "0":
                print("False")   #idk how to put it into the list
            elif plural == "1":
                print("True")
            else:
                continue
print(my_list)