from tkinter import *
import random

kolko = 0
od_koliko = 20
vreme = 50
lista_widgeta_za_brisanje = []

def ispitaj_rec(event):
    global kolko, rec, brojac
    ta_rec = mesto_za_kucanje.get()
    if ta_rec == rec:
        kolko += 1
        brojac.config(text=f"{kolko} / {od_koliko}")  
        rec = random.choice(reci1)
        rec_label.config(text=rec)
        mesto_za_kucanje.delete(0, END)  
        kraj()  
    else:
        rec = random.choice(reci1)
        rec_label.config(text=rec)
        mesto_za_kucanje.delete(0, END)

def kraj():
    global kolko
    if kolko == 20:
        window.destroy()

def quit():
    window.destroy()

def igraj_opet():
    global play_again, quit_dugme, rip, start_button, kolko, vreme


    if 'play_again' in globals():
        play_again.destroy()
    if 'quit_dugme' in globals():
        quit_dugme.destroy()
    if 'rip' in globals():
        rip.destroy()
    

    kolko = 0
    vreme = 50  


    start_button = Button(text="Start", fg="Black", bg="orange2", font=(None, 50), command=start_game)
    start_button.place(x=250, y=350)

    window.unbind('<Return>')
    window.bind('<Return>', ispitaj_rec)

def start_game():
    global start_button, kolko, od_koliko, vreme_brojac, brojac, lista_widgeta_za_brisanje, rec_label, mesto_za_kucanje, rec

    if 'start_button' in globals():
        start_button.destroy()
    if 'brojac' in globals():
        brojac.destroy()
    if 'vreme_brojac' in globals():
        vreme_brojac.destroy()
    if 'rec_label' in globals():
        rec_label.destroy()
    if 'mesto_za_kucanje' in globals():
        mesto_za_kucanje.destroy()

    brojac = Label(text=f"{kolko} / {od_koliko}", font=(None, 35), bg="peachpuff")
    brojac.place(x=1, y=650)
    vreme_brojac = Label(text=f"Time: {vreme}", font=(None, 35), bg="peachpuff")
    vreme_brojac.place(x=515, y=650)
    rec = random.choice(reci1)
    rec_label = Label(text=rec, bg="peachpuff", fg="Black", font=(None, 40))
    rec_label.place(x=250, y=200)
    
    mesto_za_kucanje = Entry(width=50)
    mesto_za_kucanje.place(x=200, y=300)
    
    lista_widgeta_za_brisanje = [vreme_brojac, brojac, rec_label, mesto_za_kucanje]
    umanji_vreme()


    mesto_za_kucanje.focus()


def umanji_vreme():
    global vreme
    if vreme > 0:
        vreme -= 1
        vreme_brojac.config(text=f"Time: {vreme}")
        window.after(1000, umanji_vreme) 
    elif vreme == 0:
        for widget in lista_widgeta_za_brisanje:
            widget.destroy()
        global rip, quit_dugme, play_again
        rip = Label(text="Isteklo ti je vreme", fg="black", bg="peachpuff", font=(None, 40))
        rip.place(x=150, y=350)
        quit_dugme = Button(text="Quit", fg="Black", bg="orange", font=(None, 20), command=quit)
        quit_dugme.place(x=100, y=500)
        play_again = Button(text="Play again", fg="Black", bg="orange", font=(None, 20), command=igraj_opet)
        play_again.place(x=500, y=500)

reci1 = [
    "hello", "apple", "find", "peach", "red", "banana", "grape", "orange", "watermelon", "blueberry",
    "strawberry", "kiwi", "lemon", "lime", "mango", "pineapple", "cherry", "pear", "plum", "apricot",
    "fig", "pomegranate", "coconut", "papaya", "grapefruit", "melon", "raspberry", "blackberry", "dragonfruit", "guava",
    "lychee", "nectarine", "peach", "persimmon", "quince", "starfruit", "tangerine", "clementine", "cranberry", "date",
    "elderberry", "gooseberry", "honeydew", "jackfruit", "kumquat", "mulberry", "olive", "passionfruit", "rambutan", "soursop",
    "tomato", "avocado", "carrot", "broccoli", "cucumber", "lettuce", "spinach", "onion", "potato", "radish",
    "turnip", "zucchini", "pumpkin", "squash", "asparagus", "beet", "cabbage", "celery", "cauliflower", "eggplant",
    "garlic", "ginger", "kale", "leek", "mushroom", "okra", "parsnip", "pepper", "shallot", "sweetcorn",
    "turnip", "yam", "courgette", "radicchio", "artichoke", "brussels", "sprout", "cauliflower", "chard", "endive",
    "fennel", "kohlrabi", "mustard", "rocket", "swede", "sweetpotato", "watercress", "chayote", "jicama", "kabocha"
]

window = Tk()
window.geometry("700x700")
window.title("Typing game")
window.config(bg="peachpuff")

label1 = Label(text="", height=10, width=200, bg="orange")
label1.place(x=0, y=0)

label2 = Label(text="Typing game", fg="Black", bg="orange", font=("Arial, 30"))
label2.place(x=250, y=50)

start_button = Button(text="Start", fg="Black", bg="orange2", font=(None, 50), command=start_game)
start_button.place(x=250, y=350)

window.bind('<Return>', ispitaj_rec)


window.mainloop()