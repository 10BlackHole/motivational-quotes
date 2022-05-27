import numpy as np

quotes = np.loadtxt("quotes.txt", dtype='str', delimiter='-')
phrases= np.loadtxt("quotes.txt", usecols=0, dtype='str', delimiter='-')
authors = np.loadtxt("quotes.txt", usecols=1, dtype='str', delimiter='-')

# def add():
    # print("Add a motivational quote")
    # phrase = str(input())
    # print("Who said it?")
    # author = str(input())
    # quotes.append(phrase + " - " + author)

# add()
# print(quotes)








