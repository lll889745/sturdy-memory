import tkinter as tk
from tkinter import messagebox, filedialog
import random
import math
# import gmpy2

# Improved is_prime function using Miller-Rabin primality test
def is_prime(n, k=5):  # number of tests = k
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Write (n - 1) as 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Witness loop
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)  # Compute a^d % n
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
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
# Optimized to find only one primitive root and generate the rest
def find_primitive_roots(p):
    if not is_prime(p):
        return []

    phi = p - 1  # Euler's totient function for prime p is p-1
    factors = set()
    n = phi
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.add(i)
            while n % i == 0:
                n //= i
    if n > 1:
        factors.add(n)

    # Find the first primitive root
    for g in range(2, p):
        if all(pow(g, phi // f, p) != 1 for f in factors):
            # Once we find a primitive root, we can generate the rest
            return [pow(g, i, p) for i in range(1, phi) if math.gcd(i, phi) == 1]
    return []

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

# Function to save the roots to a file
def save_to_file(roots):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text Documents", "*.txt")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(' '.join(map(str, roots)))
        messagebox.showinfo("Success", f"Primitive roots have been saved to {file_path}")

# GUI function to calculate primitive roots and handle large output
def calculate_primitive_roots():
    try:
        p = int(prime_entry.get())
        if not is_prime(p):
            messagebox.showerror("Error", "Input must be a prime number.")
            return
        roots = find_primitive_roots(p)
        if len(roots) > 30:  # Arbitrary limit for display in GUI
            answer = messagebox.askyesno("Large Output",
                                         "The number of primitive roots is very large. Would you like to save the output to a file?")
            if answer:
                save_to_file(roots)
            else:
                primitive_roots_result.set("Output is too large to display.")
        else:
            primitive_roots_result.set(f"Primitive roots modulo {p}: {' '.join(map(str, roots))}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a prime number for p.")

def clear_fields():
    a_entry.delete(0, tk.END)
    p_entry.delete(0, tk.END)
    prime_entry.delete(0, tk.END)
    order_result.set("")
    primitive_roots_result.set("")

def show_about():
    messagebox.showinfo("About", "Information Security Mathematical Fundamentals Lab 4\nVersion 2.0\nCopyright © 2023 Mu Xinzhe")

# Create the main window
root = tk.Tk()
root.title("Math Lab 4")

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
