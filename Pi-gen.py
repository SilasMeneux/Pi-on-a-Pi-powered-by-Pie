import tkinter as tk
from decimal import Decimal, getcontext
from math import factorial

def chudnovsky(digits):
    getcontext().prec = digits + 5
    C = Decimal(426880) * (Decimal(10005) ** Decimal(0.5))
    a = Decimal(0)
    for q in range(digits // 15 + 2):
        a += Decimal(factorial(6*q)) / Decimal((factorial(3*q))*Decimal((factorial(q))**Decimal(3))) * (Decimal(545140134)*Decimal(q) + Decimal(13591409)) / (Decimal(-262537412640768000)**Decimal(q))
    return str(C * a**-1)[:-5]

class PiGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pi Generator")
        self.root.attributes('-fullscreen', True)  # Fullscreen mode
        self.root.config(bg='black')  # Background color
        self.label = tk.Label(root, font=("Courier", 200), fg="white", bg="black")
        self.label.pack(expand=True)
        self.digits = 0
        self.pi_str = ""
        self.current_digit_index = 0
        self.input_entry = tk.Entry(root, font=("Arial", 30))
        self.input_entry.pack(pady=50)
        self.input_entry.focus_set()
        self.start_button = tk.Button(root, text="Start Generating", font=("Arial", 30), command=self.start_generation)
        self.start_button.pack()

    def start_generation(self):
        self.digits = int(self.input_entry.get())
        self.pi_str = chudnovsky(self.digits)
        self.update_pi_digit()

    def update_pi_digit(self):
        if self.current_digit_index < len(self.pi_str):
            pi_digit = self.pi_str[self.current_digit_index]
            self.label.config(text=pi_digit)
            self.current_digit_index += 1
            self.root.after(1000, self.update_pi_digit)

root = tk.Tk()
app = PiGeneratorApp(root)
# Create a label widget for the pi decoration
pi_label = tk.Label(root, text="π", font=("Courier", 100), fg="white", bg="black")
pi_label.pack(anchor="center")
root.mainloop()
