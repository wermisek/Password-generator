import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length=12, use_lowercase=True, use_uppercase=True, use_digits=True, use_special_chars=True):
    characters = ""
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_to_file(password):
    with open("generated_password.txt", "w") as file:
        file.write(password)

def generate_button_click():
    try:
        length = int(length_entry.get())
        use_lowercase = lowercase_var.get()
        use_uppercase = uppercase_var.get()
        use_digits = digits_var.get()
        use_special_chars = special_chars_var.get()

        if not (use_lowercase or use_uppercase or use_digits or use_special_chars):
            messagebox.showerror("Error", "Select at least one character category.")
            return

        unique = unique_var.get()
        password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_special_chars)

        if unique:
            while password in generated_passwords:
                password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_special_chars)
            generated_passwords.append(password)

        password_label.config(text=f"Password: {password}")

        generate_button.config(bg="green")
        app.after(200, restore_button_color)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid password length.")

def save_button_click():
    password = password_label.cget("text").split("Password: ")[1]
    save_to_file(password)
    messagebox.showinfo("Saved", "Password saved to 'generated_password.txt'.")

def generate_sentence_password(words):
    if not words:
        return ""
    special_chars = "!@#$%^&*()-_=+[]{}|;:',.<>?/"
    password = " ".join(words)
    password = password.replace(" ", random.choice(special_chars), len(words) - 1)
    return password

def generate_sentence_password_click():
    words = sentence_words_entry.get().split()
    password = generate_sentence_password(words)
    password_label.config(text=f"Password: {password}")

def copy_password():
    password = password_label.cget("text").split("Password: ")[1]
    app.clipboard_clear()
    app.clipboard_append(password)
    app.update()

def restore_button_color():
    generate_button.config(bg="#007BFF")

app = tk.Tk()
app.title("Password Generator")
app.geometry("400x500")
app.configure(bg="#f0f0f0")

generated_passwords = []

length_label = tk.Label(app, text="Password Length:", bg="#f0f0f0", font=("Arial", 12))
length_label.pack(pady=10)

length_entry = tk.Entry(app, font=("Arial", 12), width=20)
length_entry.pack()

lowercase_var = tk.BooleanVar()
lowercase_check = tk.Checkbutton(app, text="Lowercase Letters", variable=lowercase_var, bg="#f0f0f0", font=("Arial", 12))
lowercase_check.pack()

uppercase_var = tk.BooleanVar()
uppercase_check = tk.Checkbutton(app, text="Uppercase Letters", variable=uppercase_var, bg="#f0f0f0", font=("Arial", 12))
uppercase_check.pack()

digits_var = tk.BooleanVar()
digits_check = tk.Checkbutton(app, text="Digits", variable=digits_var, bg="#f0f0f0", font=("Arial", 12))
digits_check.pack()

special_chars_var = tk.BooleanVar()
special_chars_check = tk.Checkbutton(app, text="Special Characters", variable=special_chars_var, bg="#f0f0f0", font=("Arial", 12))
special_chars_check.pack()

unique_var = tk.BooleanVar()
unique_check = tk.Checkbutton(app, text="Unique Password", variable=unique_var, bg="#f0f0f0", font=("Arial", 12))
unique_check.pack()

generate_button = tk.Button(app, text="Generate Password", command=generate_button_click, font=("Arial", 14), bg="#007BFF", fg="white")
generate_button.pack(pady=10)

save_button = tk.Button(app, text="Save Password to File", command=save_button_click, font=("Arial", 14), bg="#007BFF", fg="white")
save_button.pack()

sentence_words_label = tk.Label(app, text="Enter words for sentence password:", bg="#f0f0f0", font=("Arial", 12))
sentence_words_label.pack(pady=10)

sentence_words_entry = tk.Entry(app, font=("Arial", 12), width=30)
sentence_words_entry.pack()

generate_sentence_button = tk.Button(app, text="Generate Sentence Password", command=generate_sentence_password_click, font=("Arial", 14), bg="#007BFF", fg="white")
generate_sentence_button.pack()

copy_button = tk.Button(app, text="Copy Password", command=copy_password, font=("Arial", 14), bg="#007BFF", fg="white")
copy_button.pack(pady=10)

password_label = tk.Label(app, text="Password: ", font=("Arial", 14), bg="#f0f0f0")
password_label.pack()

app.mainloop()
