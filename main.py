import random
import tkinter as tk
from quotes import quotes, phrases, authors

def text():
    n = random.randint(0, len(quotes)-1)
    # print(phrases[n] + ' - ' + authors[n])
    return(phrases[n] + ' - ' + authors[n])
    # return phrases[n], authors[n]

def ventana(x):
    ventana = tk.Tk()
    ventana.title("Motivation Quote")
    ventana.geometry("1200x300")
    ventana.configure(bg="dark turquoise")
    label1 = tk.Label(ventana, text=x)
    label1.pack()
    ventana.mainloop()

def main():
    return ventana(text())

main()

