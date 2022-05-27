import numpy as np

# quotes = ["However bad life may seem, there is always something you can do and succeed at. Where there's life, there's hope. - Stephen Hawking"]
quotes = np.genfromtxt("quotes.txt", dtype='str', delimiter='-')
# phrase = quotes[:,0]
# author = quotes[:,1]
print(len(quotes))
# def add():
    # print("Add a motivational quote")
    # phrase = str(input())
    # print("Who said it?")
    # author = str(input())
    # quotes.append(phrase + " - " + author)

# add()
# print(quotes)








