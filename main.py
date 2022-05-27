import random
from quotes import quotes

def main():
    n = random.randint(0, len(quotes)-1)
    print(quotes[n])

main()


