from random import choice
my_list = []
def text_read():
    with open('word.txt','r') as words:
        words_list = words.readlines()
        return choice(words_list).strip()
text_reader = text_read()
for i in text_reader:
    my_list.append(i)
