from tkinter import Tk, Button, Label
from random import choice

avaliable_choices = ["paper", "rock", "scissors"]
#cpu = choice(avaliable_choices)
player = None

def cpu_choice():
    return choice(avaliable_choices)

def play(player, cpu):
    win_with = {"paper": "rock", "rock": "scissors", "scissors": "paper"}

    if player == cpu:
        return None
    elif win_with[player] == cpu:
        return True
    else:
        return False

def click_action(player_choice, text_label):

    user_win = play(player_choice, cpu_choice())
    if user_win == True:
        text_label.config(text="You win, next round?", fg='green')
    elif user_win == False:
        text_label.config(text="I win :D, next round? ", fg="red")
    else:
        text_label.config(text="Tie! let's try again", fg="blue")


root = Tk()
root.title("Paper, Rock, Scissors Game")
root.geometry("400x250")

text_label = Label(root, font=50, fg="blue", text="Let's play paper, rock, scissors!")
text_label.pack()

button_paper = Button(root, text="📃 Paper", font=30, width=12)
button_paper.pack()
button_rock = Button(root, text="🤘 Rock", font=30, width=12)
button_rock.pack()
button_scissors = Button(root, text="✂️ Scissors", font=30, width=12)
button_scissors.pack()

button_rock.config(command=lambda: click_action('rock', text_label))
button_paper.config(command=lambda: click_action('paper', text_label))
button_scissors.config(command=lambda: click_action('scissors', text_label))



root.mainloop()