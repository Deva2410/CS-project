import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import hashlib
import subprocess
import webbrowser

# Function to create an account
def create_account():
    username = username_entry.get()
    password = hashlib.sha256(password_entry.get().encode()).hexdigest()

    conn = sqlite3.connect('car_rental.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Account created successfully!")

# Function to launch the car rental app
def launch_car_rental_app():
    try:
        subprocess.Popen(["python", r"D:\Los Pollos Hermanos Rentals\main.py"])
    except Exception as e:
        print(f"Error launching car rental app: {e}")

# Function to open a website
def open_website(url):
    webbrowser.open(url)

# GUI Setup
app = tk.Tk()
app.title("Los Pollos Hermanos Rentals")

# Labels
username_label = tk.Label(app, text="Username:")
password_label = tk.Label(app, text="Password:")

# Entry Widgets
username_entry = tk.Entry(app)
password_entry = tk.Entry(app, show='*')  # Entry widget for password (show='*' to hide characters)

# Buttons
create_account_button = tk.Button(app, text="Create Account", command=create_account)
launch_app_button = tk.Button(app, text="Launch Car Rental App", command=launch_car_rental_app)



# Grid Layout
username_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
username_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")
password_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
password_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")
create_account_button.grid(row=2, column=0, columnspan=2, pady=10, sticky="n")
launch_app_button.grid(row=3, column=0, columnspan=2, pady=10, sticky="n")

# Styling
app.geometry("400x250")
app.configure(bg="#2E2E2E", padx=20, pady=20)

# Additional widgets
info_label = tk.Label(app, text="Welcome to Los Pollos Hermanos Rentals", fg="white", bg="#2E2E2E")
info_label.grid(row=4, column=0, columnspan=2, pady=10)

# Additional Frames
frame1 = ttk.Frame(app, padding=10)
frame1.grid(row=5, column=0, columnspan=2, pady=10)

frame2 = ttk.Frame(app, padding=10)
frame2.grid(row=6, column=0, columnspan=2, pady=10)

# Additional Labels
label1 = tk.Label(frame1, text="About us", fg="white", bg="#2E2E2E")
label1.pack()



# Additional Buttons
button1 = tk.Button(frame1, text="Website", command=lambda: open_website("D:\Los Pollos Hermanos Rentals\index.html"))
button1.pack(pady=5)


# Run the GUI
app.mainloop()
