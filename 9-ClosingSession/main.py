#To be typed into the REPL
import tkinter
from urllib.request import urlopen
import random

num = random.randint(0, 1000)

with urlopen('http://numbersapi.com/' + str(num)) as fact:
    fact_words = ''
    for line in fact:
        # line_words = line.split()
        line_words = line.decode('utf-8').split()
        for word in line_words:
            fact_words += ' ' + word

window = tkinter.Tk()

window.title('Number Facts are Cool?')
window.geometry('700x50')



label = tkinter.Label( window, text=fact_words )
label.pack()
window.mainloop()
