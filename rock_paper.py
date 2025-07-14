import tkinter as tk
import random

# Initialize scores
user_score = 0
computer_score = 0

# Main function to determine the result
def play(choice):
    global user_score, computer_score
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)

    user_choice_label.config(text=f"Your Choice: {choice}")
    computer_choice_label.config(text=f"Computer Choice: {computer_choice}")

    if choice == computer_choice:
        result_label.config(text="It's a Tie!", fg="blue")
    elif (choice == "Rock" and computer_choice == "Scissors") or \
         (choice == "Paper" and computer_choice == "Rock") or \
         (choice == "Scissors" and computer_choice == "Paper"):
        result_label.config(text="You Win!", fg="green")
        user_score += 1
    else:
        result_label.config(text="Computer Wins!", fg="red")
        computer_score += 1

    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")

# Create main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("400x350")
root.configure(bg="lightblue")

# Title
title_label = tk.Label(root, text="Rock-Paper-Scissors", font=("Helvetica", 18, "bold"), bg="lightblue")
title_label.pack(pady=10)

# Choices Labels
user_choice_label = tk.Label(root, text="Your Choice: ", font=("Helvetica", 12), bg="lightblue")
user_choice_label.pack()

computer_choice_label = tk.Label(root, text="Computer Choice: ", font=("Helvetica", 12), bg="lightblue")
computer_choice_label.pack()

# Result Label
result_label = tk.Label(root, text="", font=("Helvetica", 14, "bold"), bg="lightblue")
result_label.pack(pady=10)

# Score Label
score_label = tk.Label(root, text="Score - You: 0 | Computer: 0", font=("Helvetica", 12), bg="lightblue")
score_label.pack(pady=10)

# Buttons
button_frame = tk.Frame(root, bg="lightblue")
button_frame.pack(pady=10)

rock_btn = tk.Button(button_frame, text="Rock", width=10, command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(button_frame, text="Paper", width=10, command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=10)

# Start the GUI loop
root.mainloop()
