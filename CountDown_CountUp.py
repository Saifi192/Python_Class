import time #Used to manage time delays with time.sleep().
import tkinter as tk # Imports the Tkinter library for GUI development
from tkinter import messagebox #Enables pop-up dialogs (e.g., for information or errors)

def countdown(): 
    try:
        t = int(entry.get()) # Reads the user input from the entry field and converts it to an integer
        while t: # Continues the loop as long as t > 0.
            mins, secs = divmod(t, 60) # Converts the time in seconds into minutes and seconds.
            timer = '{:02d}:{:02d}'.format(mins, secs)   # Formats the time as "MM:SS".
            label.config(text=timer)   # Updates the label to display the current time.
            root.update()    # Refreshes the GUI to show the updated time.
            time.sleep(1)    # Pauses the program for 1 second.
            t -= 1     # Decreases the remaining time by 1 second.
        label.config(text="Timer completed!")    # Updates the label when the countdown is complete.
        messagebox.showinfo("Info", "Countdown completed!")     # Shows a pop-up to inform the user the timer is done.
    except ValueError:     # If the user enters invalid input (e.g., text instead of a number):
        messagebox.showerror("Error", "Please enter a valid number!")  # Displays an error pop-up.

def countup():
    try:
        t = int(entry.get())    # Reads the user input from the entry field and converts it to an integer.
        current_time = 0   # Initializes the timer at 0 seconds.
        while current_time <= t:    # Continues the loop until the current time reaches the input value.
            mins, secs = divmod(current_time, 60)    # Converts the time in seconds into minutes and seconds.
            timer = '{:02d}:{:02d}'.format(mins, secs)   # Formats the time as "MM:SS".
            label.config(text=timer)      # Updates the label to display the current time.
            root.update()    # Refreshes the GUI to show the updated time.
            time.sleep(1)    # Pauses the program for 1 second.
            current_time += 1    # Increments the timer by 1 second.
        label.config(text="Timer completed!")   # Updates the label when the countup is complete.
        messagebox.showinfo("Info", "Countup completed!")   # Shows a pop-up to inform the user the timer is done
    except ValueError:   # If the user enters invalid input (e.g., text instead of a number):
        messagebox.showerror("Error", "Please enter a valid number!")    # Displays an error pop-up.

# Create the main window
root = tk.Tk()     # Initializes the main GUI window.
root.title("Timer GUI")    # Sets the title of the window to "Timer GUI".

# Input field and label
tk.Label(root, text="Enter time in seconds:").pack(pady=10)   # Adds a label prompting the user to input time.
entry = tk.Entry(root, width=20)   # Creates an input field where the user can type a time in seconds.
entry.pack(pady=5)    # Places the input field in the window with padding.

# Buttons for CountDown and CountUp
tk.Button(root, text="CountDown", command=countdown).pack(pady=10)    # Adds a button to start the countdown.
tk.Button(root, text="CountUp", command=countup).pack(pady=10)    # Adds a button to start the countup.

# Timer display
label = tk.Label(root, text="", font=("Helvetica", 24))   # Creates a label to display the timer.
label.pack(pady=20)    # Places the label in the window with padding.

# Run the application
root.mainloop()    # Runs the main event loop of the GUI, keeping the window open and responsive.
