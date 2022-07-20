from tkinter import Tk, Label, Button

counter = 0

def click_action(button):
    global counter
    counter += 1
    button.config(text=f"Klilnięto {counter} razy :D")

root = Tk()
root.title('Nowe okienko')
root.geometry("1000x700")

label = Label(root, text="Mój napis", font=30, fg="red")


#polecenie command w wierszu definicji
#click_button = Button(root, text="Naciśnij", width=20, command=click_action)
click_button = Button(root, text="Naciśnij", width=20)
click_button.pack()
label.pack()

click_button.config(command=lambda: click_action(click_button))

root.mainloop()