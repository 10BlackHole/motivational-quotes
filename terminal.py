import random
import tkinter as tk
from quotes import quotes, phrases, authors

def main():
    n = random.randint(0, len(quotes)-1)
    print(phrases[n] + ' - ' + authors[n])

main()

