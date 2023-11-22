import tkinter as tk
from tkinter import messagebox
import math

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Function to find the power of a number modulo p
def power(a, i, p):
    result = 1
    a %= p
    while i > 0:
        if i & 1:
            result = (result * a) % p
        a = (a * a) % p
        i >>= 1
    return result

# Function to find the order of a modulo p
def ord(a, p):
    for i in range(1, p):
        if (p - 1) % i != 0:
            continue
        if power(a, i, p) == 1:
            return i
    return -1

# Function to find all primitive roots modulo p
def find_primitive_roots(p):
    if not is_prime(p) or p % 2 == 0:
        return []

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def euler_phi(n):
        result = n
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                while n % i == 0:
                    n //= i
                result -= result // i
        if n > 1:
            result -= result // n
        return result

    g = next(g for g in range(2, p) if all(power(g, (p - 1) // f, p) != 1 for f in range(2, p) if (p - 1) % f == 0))
    roots = [power(g, k, p) for k in range(1, p) if gcd(k, p - 1) == 1]
    return roots

# GUI functions
def calculate_order():
    try:
        a = int(a_entry.get())
        p = int(p_entry.get())
        if not is_prime(p):
            messagebox.showerror("Error", "p must be a prime number.")
            return
        order_result.set(f"ord {p}({a}) = {ord(a, p)}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter integers for a and p.")

def calculate_primitive_roots():
    try:
        p = int(prime_entry.get())
        if not is_prime(p) or p % 2 == 0:
            messagebox.showerror("Error", "Input must be an odd prime number.")
            return
        roots = find_primitive_roots(p)
        primitive_roots_result.set(f"Primitive roots modulo {p}: {' '.join(map(str, roots))}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter an odd prime number for p.")

def clear_fields():
    a_entry.delete(0, tk.END)
    p_entry.delete(0, tk.END)
    prime_entry.delete(0, tk.END)
    order_result.set("")
    primitive_roots_result.set("")

def show_about():
    messagebox.showinfo("About", "Information Security Mathematical Fundamentals Lab 4\nVersion 1.0\nCopyright © 2023 Mu Xinzhe")

# Create the main window
root = tk.Tk()
root.title("Math Functions")

# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Add menu items
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Clear", command=clear_fields)
file_menu.add_separator()
file_menu.add_command(label="About", command=show_about)

# Order calculation inputs
tk.Label(root, text="Calculate Order").grid(row=0, column=0, columnspan=2)
tk.Label(root, text="Enter a:").grid(row=1, column=0)
a_entry = tk.Entry(root)
a_entry.grid(row=1, column=1)
tk.Label(root, text="Enter p (prime):").grid(row=2, column=0)
p_entry = tk.Entry(root)
p_entry.grid(row=2, column=1)
order_result = tk.StringVar()
tk.Label(root, textvariable=order_result).grid(row=3, column=0, columnspan=2)
tk.Button(root, text="Calculate Order", command=calculate_order).grid(row=4, column=0, columnspan=2)

# Primitive roots calculation inputs
tk.Label(root, text="Find Primitive Roots").grid(row=5, column=0, columnspan=2)
tk.Label(root, text="Enter an odd prime number:").grid(row=6, column=0)
prime_entry = tk.Entry(root)
prime_entry.grid(row=6, column=1)
primitive_roots_result = tk.StringVar()
tk.Label(root, textvariable=primitive_roots_result).grid(row=7, column=0, columnspan=2)
tk.Button(root, text="Find Primitive Roots", command=calculate_primitive_roots).grid(row=8, column=0, columnspan=2)

# Run the application
root.mainloop()
