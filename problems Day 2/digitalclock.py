import tkinter as tk
from time import strftime

# Create window
root = tk.Tk()
root.title("Digital Clock")

# Label for time
label = tk.Label(root, font=("Verdana", 50), bg="black", fg="cyan")
label.pack(anchor="center")

# Function to update time
def time():
    current_time = strftime("%H:%M:%S")
    label.config(text=current_time)
    label.after(1000, time)  # update every second

time()
root.mainloop()
