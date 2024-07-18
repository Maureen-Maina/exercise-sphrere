import tkinter as tk
from tkinter import messagebox
import sqlite3

# Function to create the database and table if they don't exist
def create_database():
    conn = sqlite3.connect('shopkeeper.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        product_no INTEGER PRIMARY KEY,
        product_name TEXT NOT NULL,
        buying_price REAL NOT NULL,
        selling_price REAL NOT NULL,
        date_sold TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

# Function to insert product into the database
def insert_product():
    product_name = entry_name.get()
    product_no = entry_no.get()
    buying_price = entry_buying.get()
    selling_price = entry_selling.get()
    date_sold = entry_date.get()
    
    if not (product_name and product_no and buying_price and selling_price and date_sold):
        messagebox.showerror("Error", "All fields are required")
        return
    
    try:
        conn = sqlite3.connect('shopkeeper.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO products (product_no, product_name, buying_price, selling_price, date_sold) VALUES (?, ?, ?, ?, ?)",
                       (product_no, product_name, buying_price, selling_price, date_sold))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Product added successfully")
        entry_name.delete(0, tk.END)
        entry_no.delete(0, tk.END)
        entry_buying.delete(0, tk.END)
        entry_selling.delete(0, tk.END)
        entry_date.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to display all products and total profit
def display_products():
    try:
        conn = sqlite3.connect('shopkeeper.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()
        total_profit = sum([p[3] - p[2] for p in products])
        conn.close()
        
        display_text = ""
        for product in products:
            display_text += f"Product No: {product[0]}, Name: {product[1]}, Buying Price: {product[2]}, Selling Price: {product[3]}, Date Sold: {product[4]}\n"
        display_text += f"\nTotal Profit: {total_profit}"
        
        display_label.config(text=display_text)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Tkinter window setup
window = tk.Tk()
window.title("Shopkeeper Application")

# Labels and Entries
tk.Label(window, text="Product No:").grid(row=0, column=0)
entry_no = tk.Entry(window)
entry_no.grid(row=0, column=1)

tk.Label(window, text="Product Name:").grid(row=1, column=0)
entry_name = tk.Entry(window)
entry_name.grid(row=1, column=1)

tk.Label(window, text="Buying Price:").grid(row=2, column=0)
entry_buying = tk.Entry(window)
entry_buying.grid(row=2, column=1)

tk.Label(window, text="Selling Price:").grid(row=3, column=0)
entry_selling = tk.Entry(window)
entry_selling.grid(row=3, column=1)

tk.Label(window, text="Date Sold (YYYY-MM-DD):").grid(row=4, column=0)
entry_date = tk.Entry(window)
entry_date.grid(row=4, column=1)

# Buttons
tk.Button(window, text="Add Product", command=insert_product).grid(row=5, column=0, columnspan=2)
tk.Button(window, text="Display Products and Total Profit", command=display_products).grid(row=6, column=0, columnspan=2)

# Display Label
display_label = tk.Label(window, text="", justify=tk.LEFT)
display_label.grid(row=7, column=0, columnspan=2)

# Create the database and table
create_database()

# Start the Tkinter loop
window.mainloop()
