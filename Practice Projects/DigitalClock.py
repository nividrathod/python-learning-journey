import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")
root.geometry("700x350")
root.resizable(False, False)
root.configure(bg="#121212")

def time():
    # Get current time
    current_time = strftime("%H:%M:%S")
    current_date = strftime("%A, %d %B %Y")
    am_pm = strftime("%p")

    # Update labels
    time_label.config(text=current_time)
    am_pm_label.config(text=am_pm)
    date_label.config(text=current_date)
 
    time_label.after(1000, time)

title_label = tk.Label(
    root,
    text="DIGITAL CLOCK",
    font=("Arial", 18, "bold"),
    bg="#121212",
    fg="#00FF99"
)

title_label.pack(pady=(25, 10))

clock_frame = tk.Frame(
    root,
    bg="#1E1E1E",
    padx=30,
    pady=20
)

clock_frame.pack()

time_label = tk.Label(
    clock_frame,
    font=("Consolas", 60, "bold"),
    bg="#1E1E1E",
    fg="#00FF99"
)

time_label.pack()

am_pm_label = tk.Label(
    clock_frame,
    font=("Arial", 16, "bold"),
    bg="#1E1E1E",
    fg="#FFFFFF"
)

am_pm_label.pack()

date_label = tk.Label(
    root,
    font=("Arial", 18),
    bg="#121212",
    fg="#FFFFFF"
)

date_label.pack(pady=20)

footer_label = tk.Label(
    root,
    text="⏱ Time updates every second",
    font=("Arial", 10),
    bg="#121212",
    fg="#777777"
)

footer_label.pack()

time()

root.mainloop()