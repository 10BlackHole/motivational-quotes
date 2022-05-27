import random
from quotes import quotes

# quotes = ["However bad life may seem, there is always something you can do and succeed at. Where there's life, there's hope. - Stephen Hawking"]





def main():
    n = random.randint(0, len(quotes)-1)
    print(quotes[n])

main()


