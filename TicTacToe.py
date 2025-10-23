import tkinter as tk
from tkinter import messagebox

def check_winner():
    combos = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for combo in combos:
        if (buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != ""):
            for i in combo:
                buttons[i].config(bg="lightgreen")
            messagebox.showinfo("Tic Tac Toe", f"Player {buttons[combo[0]]['text']} wins!")
            root.quit()
            return True

    if all(button["text"] != "" for button in buttons):
        messagebox.showinfo("Tic Tac Toe", "It's a Draw!")
        root.quit()
        return True
    return False


def button_click(index):
    global current_player
    if buttons[index]["text"] == "" and not check_winner():
        buttons[index]["text"] = current_player
        if not check_winner():
            toggle_player()


def toggle_player():
    global current_player
    current_player = "O" if current_player == "X" else "X"
    label.config(text=f"Player {current_player}'s Turn")


root = tk.Tk()
root.title("Tic Tac Toe")

current_player = "X"

label = tk.Label(root, text=f"Player {current_player}'s Turn", font=("Arial", 16))
label.grid(row=0, column=0, columnspan=3)

buttons = []

for i in range(9):
    btn = tk.Button(root, text="", font=("Arial", 24), width=5, height=2,
                    command=lambda i=i: button_click(i))
    btn.grid(row=(i // 3) + 1, column=i % 3)
    buttons.append(btn)

root.mainloop()
