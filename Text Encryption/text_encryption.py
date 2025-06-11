import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import locale


LANGUAGES = {
    "English": {
        "title": "Text Encryption Tool",
        "message": "Message:",
        "algorithm": "Algorithm:",
        "key": "Key (if needed):",
        "view": "View",
        "hide": "Hide",
        "encrypt": "Encrypt",
        "decrypt": "Decrypt",
        "clear": "Clear",
        "encrypted_text": "Encrypted Text:",
        "decrypted_text": "Decrypted Text:",
        "copy": "Copy",
        "ready": "Ready.",
        "cleared": "Cleared all fields.",
        "encryption_success": "Encryption successful!",
        "encryption_failed": "Encryption failed.",
        "decryption_success": "Decryption successful!",
        "decryption_failed": "Decryption failed.",
        "key_required": "Key is required for {}.",
        "weak_key": "{} key should be at least 8 characters.",
        "no_encrypted": "No encrypted text to decrypt.",
        "nothing_to_copy": "Nothing to copy.",
        "copied_encrypted": "Encrypted text copied to clipboard.",
        "copied_decrypted": "Decrypted text copied to clipboard.",
        "invalid_rsa": "Invalid encrypted text format for RSA.",
        "drag_drop": "Drag and drop a file or text here.",
        "strength_weak": "Weak",
        "strength_moderate": "Moderate",
        "strength_strong": "Strong",
        "strength_label": "Key Strength:"
    },
    "Hindi": {
        "title": "पाठ्य एन्क्रिप्शन टूल",
        "message": "संदेश:",
        "algorithm": "एल्गोरिदम:",
        "key": "कुंजी (यदि आवश्यक हो):",
        "view": "देखें",
        "hide": "छुपाएँ",
        "encrypt": "एन्क्रिप्ट करें",
        "decrypt": "डिक्रिप्ट करें",
        "clear": "साफ करें",
        "encrypted_text": "एन्क्रिप्टेड पाठ:",
        "decrypted_text": "डिक्रिप्टेड पाठ:",
        "copy": "कॉपी करें",
        "ready": "तैयार.",
        "cleared": "सभी फ़ील्ड साफ़ किए गए.",
        "encryption_success": "एन्क्रिप्शन सफल!",
        "encryption_failed": "एन्क्रिप्शन असफल.",
        "decryption_success": "डिक्रिप्शन सफल!",
        "decryption_failed": "डिक्रिप्शन असफल.",
        "key_required": "{} के लिए कुंजी आवश्यक है.",
        "weak_key": "{} कुंजी कम से कम 8 अक्षरों की होनी चाहिए.",
        "no_encrypted": "डिक्रिप्ट करने के लिए कोई एन्क्रिप्टेड पाठ नहीं.",
        "nothing_to_copy": "कॉपी करने के लिए कुछ नहीं.",
        "copied_encrypted": "एन्क्रिप्टेड पाठ क्लिपबोर्ड पर कॉपी किया गया.",
        "copied_decrypted": "डिक्रिप्टेड पाठ क्लिपबोर्ड पर कॉपी किया गया.",
        "invalid_rsa": "RSA के लिए अमान्य एन्क्रिप्टेड पाठ प्रारूप.",
        "drag_drop": "यहाँ फ़ाइल या पाठ ड्रैग और ड्रॉप करें.",
        "strength_weak": "कमज़ोर",
        "strength_moderate": "मध्यम",
        "strength_strong": "मजबूत",
        "strength_label": "कुंजी की ताकत:"
    }
    
}

current_lang = "English"
T = LANGUAGES[current_lang]

def set_language(lang):
    global current_lang, T
    current_lang = lang
    T = LANGUAGES[lang]
    update_ui_language()

def update_ui_language():
    title.config(text=T["title"])
    msg_label.config(text=T["message"])
    algo_label.config(text=T["algorithm"])
    key_label.config(text=T["key"])
    view_key_btn.config(text=T["view"] if key_entry.cget('show') == '*' else T["hide"])
    encrypt_btn.config(text=T["encrypt"])
    decrypt_btn.config(text=T["decrypt"])
    clear_btn.config(text=T["clear"])
    enc_label.config(text=T["encrypted_text"])
    dec_label.config(text=T["decrypted_text"])
    copy_enc_btn.config(text=T["copy"])
    copy_dec_btn.config(text=T["copy"])
    status_var.set(T["ready"])
    strength_label.config(text=T["strength_label"])
    drag_drop_label.config(text=T["drag_drop"])

# --- Encryption Strength Indicator ---
def get_key_strength(key):
    if len(key) < 8:
        return "weak"
    elif len(key) < 16:
        return "moderate"
    else:
        return "strong"

def update_strength_indicator(*args):
    key = key_input.get()
    strength = get_key_strength(key)
    if strength == "weak":
        strength_val_label.config(text=T["strength_weak"], fg="#e53935")
    elif strength == "moderate":
        strength_val_label.config(text=T["strength_moderate"], fg="#fbc02d")
    else:
        strength_val_label.config(text=T["strength_strong"], fg="#388e3c")

# --- Dark Mode Toggle ---
is_dark = False
def toggle_dark_mode():
    global is_dark
    is_dark = not is_dark
    if is_dark:
        dark_btn.config(text="🌙")  
        root.configure(bg="#23272e")
        frame.config(bg="#2d333b")
        for w in frame.winfo_children():
            if isinstance(w, tk.Label):
                w.config(bg="#2d333b", fg="#e0e0e0")
            elif isinstance(w, tk.Entry):
                w.config(bg="#23272e", fg="#e0e0e0", insertbackground="#e0e0e0")
            elif isinstance(w, tk.Button):
                w.config(bg="#444c56", fg="#e0e0e0", activebackground="#373e47")
            elif isinstance(w, ttk.Combobox):
                w.config(background="#23272e", foreground="#e0e0e0")
        status_bar.config(bg="#2d333b", fg="#e0e0e0")
        drag_drop_label.config(bg="#2d333b", fg="#bdbdbd")
    else:
        dark_btn.config(text="☀️")  
        root.configure(bg="#f0f4f8")
        frame.config(bg="#e3eaf2")
        for w in frame.winfo_children():
            if isinstance(w, tk.Label):
                w.config(bg="#e3eaf2", fg=label_fg)
            elif isinstance(w, tk.Entry):
                w.config(bg=entry_bg, fg="#000", insertbackground="#000")
            elif isinstance(w, tk.Button):
                w.config(bg="#bdbdbd", fg="#000", activebackground="#bdbdbd")
            elif isinstance(w, ttk.Combobox):
                w.config(background=entry_bg, foreground="#000")
        status_bar.config(bg="#e3eaf2", fg="#333")
        drag_drop_label.config(bg="#e3eaf2", fg="#888")

# --- Drag & Drop Support for Text Input ---
def on_drop(event):
    try:
        data = event.data
        if data.startswith('{') and data.endswith('}'):
            data = data[1:-1]
        if data.endswith('.txt'):
            with open(data, 'r', encoding='utf-8') as f:
                message_input.set(f.read())
        else:
            message_input.set(data)
        status_var.set("Text loaded from drag & drop.")
    except Exception as e:
        status_var.set(f"Failed to load: {e}")

def enable_drag_and_drop(widget):
    try:
        import tkinterdnd2 as tkdnd
        widget.drop_target_register(tkdnd.DND_FILES, tkdnd.DND_TEXT)
        widget.dnd_bind('<<Drop>>', on_drop)
    except ImportError:
        drag_drop_label.config(text="Install tkinterdnd2 for drag & drop support.")

from aes_encryption import aes_encrypt, aes_decrypt
from des_encryption import des_encrypt, des_decrypt
from rsa_encryption import generate_keys, rsa_encrypt, rsa_decrypt

public_key, private_key = generate_keys()

def encrypt():
    algo = algo_var.get()
    msg = message_input.get()
    key = key_input.get()
    if not msg:
        status_var.set("Please enter a message to encrypt.")
        return
    try:
        if algo == "AES":
            if not key:
                messagebox.showerror("Error", "Key is required for AES encryption.")
                return
            if len(key) < 8:
                messagebox.showwarning("Weak Key", "AES key should be at least 8 characters.")
            output.set(aes_encrypt(msg, key))
        elif algo == "DES":
            if not key:
                messagebox.showerror("Error", "Key is required for DES encryption.")
                return
            if len(key) < 8:
                messagebox.showwarning("Weak Key", "DES key should be at least 8 characters.")
            output.set(des_encrypt(msg, key))
        elif algo == "RSA":
            encrypted = rsa_encrypt(msg, public_key)
            output.set(encrypted.hex())
        status_var.set("Encryption successful!")
    except Exception as e:
        messagebox.showerror("Encryption Error", str(e))
        status_var.set("Encryption failed.")

def decrypt():
    algo = algo_var.get()
    enc = output.get()
    key = key_input.get()
    if not enc:
        status_var.set("No encrypted text to decrypt.")
        return
    try:
        if algo == "AES":
            if not key:
                messagebox.showerror("Error", "Key is required for AES decryption.")
                return
            decrypted.set(aes_decrypt(enc, key))
        elif algo == "DES":
            if not key:
                messagebox.showerror("Error", "Key is required for DES decryption.")
                return
            decrypted.set(des_decrypt(enc, key))
        elif algo == "RSA":
            try:
                decrypted.set(rsa_decrypt(bytes.fromhex(enc), private_key))
            except ValueError:
                messagebox.showerror("Decryption Error", "Invalid encrypted text format for RSA.")
        status_var.set("Decryption successful!")
    except Exception as e:
        messagebox.showerror("Decryption Error", str(e))
        status_var.set("Decryption failed.")

def on_algo_change(event=None):
    if algo_var.get() == "RSA":
        key_entry.config(state="disabled", show="")
        key_input.set("")
    else:
        key_entry.config(state="normal", show="*")

def clear_fields():
    message_input.set("")
    key_input.set("")
    output.set("")
    decrypted.set("")
    status_var.set("Cleared all fields.")

def copy_encrypted():
    if output.get():
        root.clipboard_clear()
        root.clipboard_append(output.get())
        status_var.set("Encrypted text copied to clipboard.")
    else:
        status_var.set("Nothing to copy.")

def copy_decrypted():
    if decrypted.get():
        root.clipboard_clear()
        root.clipboard_append(decrypted.get())
        status_var.set("Decrypted text copied to clipboard.")
    else:
        status_var.set("Nothing to copy.")

def create_tooltip(widget, text):
    tooltip = tk.Toplevel(widget)
    tooltip.withdraw()
    tooltip.overrideredirect(True)
    label = tk.Label(tooltip, text=text, background="#ffffe0", relief="solid", borderwidth=1, font=("tahoma", "8", "normal"))
    label.pack()
    def enter(event):
        x = event.x_root + 10
        y = event.y_root + 10
        tooltip.geometry(f"+{x}+{y}")
        tooltip.deiconify()
    def leave(event):
        tooltip.withdraw()
    widget.bind("<Enter>", enter)
    widget.bind("<Leave>", leave)

def toggle_key_visibility():
    if key_entry.cget('show') == '*':
        key_entry.config(show='')
        view_key_btn.config(text="Hide")
    else:
        key_entry.config(show='*')
        view_key_btn.config(text="View")

# GUI Setup
try:
    from tkinterdnd2 import TkinterDnD
    root = TkinterDnD.Tk()
except ImportError:
    root = tk.Tk()

root.title(T["title"])
root.geometry("500x480")
root.resizable(False, False)
root.configure(bg="#f0f4f8")

# Variables
message_input = tk.StringVar()
key_input = tk.StringVar()
output = tk.StringVar()
decrypted = tk.StringVar()
algo_var = tk.StringVar(value="AES")
status_var = tk.StringVar(value=T["ready"])

# Widgets
frame = tk.Frame(root, padx=20, pady=20, bg="#e3eaf2")
frame.pack(fill="both", expand=True)

label_fg = "#1a237e"
entry_bg = "#ffffff"

title = tk.Label(frame, text=T["title"], bg="#e3eaf2", fg="#0d47a1", font=("Arial", 16, "bold"))
title.grid(row=0, column=1, columnspan=2, pady=(0, 15), sticky="w")

# Language Selector on the left
lang_combo = ttk.Combobox(frame, values=list(LANGUAGES.keys()), state="readonly", width=10)
lang_combo.set(current_lang)
lang_combo.grid(row=0, column=0, sticky="nw", padx=(0, 8), pady=(0, 0)) 

def on_lang_change(event):
    set_language(lang_combo.get())
lang_combo.bind("<<ComboboxSelected>>", on_lang_change)


dark_btn = tk.Button(frame, text="☀️", command=toggle_dark_mode, width=3, bg="#bdbdbd")
dark_btn.grid(row=0, column=2, sticky="ne", padx=(0, 16), pady=(0, 0))  

# Message
msg_label = tk.Label(frame, text=T["message"], bg="#e3eaf2", fg=label_fg)
msg_label.grid(row=1, column=0, sticky="e", pady=5, padx=(0, 8))
msg_entry = tk.Entry(frame, textvariable=message_input, width=40, bg=entry_bg)
msg_entry.grid(row=1, column=1, columnspan=2, sticky="w", pady=5)
create_tooltip(msg_entry, "Enter the message you want to encrypt or decrypt.")

# Drag & Drop Label
drag_drop_label = tk.Label(frame, text=T["drag_drop"], bg="#e3eaf2", fg="#888", font=("Arial", 8, "italic"))
drag_drop_label.grid(row=2, column=1, columnspan=2, sticky="w", pady=(0, 5))
enable_drag_and_drop(msg_entry)

# Algorithm
algo_label = tk.Label(frame, text=T["algorithm"], bg="#e3eaf2", fg=label_fg)
algo_label.grid(row=3, column=0, sticky="e", pady=5, padx=(0, 8))
algo_combo = ttk.Combobox(frame, textvariable=algo_var, values=["AES", "DES", "RSA"], state="readonly", width=37)
algo_combo.grid(row=3, column=1, columnspan=2, sticky="w", pady=5)
algo_combo.bind("<<ComboboxSelected>>", on_algo_change)
create_tooltip(algo_combo, "Choose the encryption algorithm.")

# Key
key_label = tk.Label(frame, text=T["key"], bg="#e3eaf2", fg=label_fg)
key_label.grid(row=4, column=0, sticky="e", pady=5, padx=(0, 8))
key_entry = tk.Entry(frame, textvariable=key_input, width=32, bg=entry_bg, show="*")
key_entry.grid(row=4, column=1, sticky="w", pady=5)
create_tooltip(key_entry, "Enter the key (password) for AES or DES. Not needed for RSA.")

view_key_btn = tk.Button(frame, text=T["view"], command=toggle_key_visibility, width=7, bg="#bdbdbd")
view_key_btn.grid(row=4, column=2, sticky="w", pady=5, padx=(8, 0))
create_tooltip(view_key_btn, "Show or hide the key.")

# Encryption Strength Indicator
strength_label = tk.Label(frame, text=T["strength_label"], bg="#e3eaf2", fg=label_fg)
strength_label.grid(row=5, column=0, sticky="e", pady=5, padx=(0, 8))
strength_val_label = tk.Label(frame, text="", bg="#e3eaf2", fg="#e53935", font=("Arial", 10, "bold"))
strength_val_label.grid(row=5, column=1, sticky="w", pady=5)
key_input.trace_add("write", update_strength_indicator)

# Buttons
encrypt_btn = tk.Button(frame, text=T["encrypt"], command=encrypt, width=18, bg="#1976d2", fg="white", activebackground="#1565c0")
encrypt_btn.grid(row=6, column=0, pady=15, padx=2)
decrypt_btn = tk.Button(frame, text=T["decrypt"], command=decrypt, width=18, bg="#388e3c", fg="white", activebackground="#2e7d32")
decrypt_btn.grid(row=6, column=1, pady=15, padx=2)
clear_btn = tk.Button(frame, text=T["clear"], command=clear_fields, width=10, bg="#e53935", fg="white", activebackground="#b71c1c")
clear_btn.grid(row=6, column=2, pady=15, padx=2)

# Encrypted Text
enc_label = tk.Label(frame, text=T["encrypted_text"], bg="#e3eaf2", fg=label_fg)
enc_label.grid(row=7, column=0, sticky="e", pady=5, padx=(0, 8))
enc_entry = tk.Entry(frame, textvariable=output, width=40, state="readonly", bg=entry_bg)
enc_entry.grid(row=7, column=1, sticky="w", pady=5)
copy_enc_btn = tk.Button(frame, text=T["copy"], command=copy_encrypted, width=8, bg="#ffb300", fg="black")
copy_enc_btn.grid(row=7, column=2, sticky="w", padx=(8, 0))
create_tooltip(enc_entry, "This is the encrypted output. You can copy it.")

# Decrypted Text
dec_label = tk.Label(frame, text=T["decrypted_text"], bg="#e3eaf2", fg=label_fg)
dec_label.grid(row=8, column=0, sticky="e", pady=5, padx=(0, 8))
dec_entry = tk.Entry(frame, textvariable=decrypted, width=40, state="readonly", bg=entry_bg)
dec_entry.grid(row=8, column=1, sticky="w", pady=5)
copy_dec_btn = tk.Button(frame, text=T["copy"], command=copy_decrypted, width=8, bg="#ffb300", fg="black")
copy_dec_btn.grid(row=8, column=2, sticky="w", padx=(8, 0))
create_tooltip(dec_entry, "This is the decrypted output. You can copy it.")

# Status Bar
status_bar = tk.Label(root, textvariable=status_var, bd=1, relief="sunken", anchor="w", bg="#e3eaf2", fg="#333")
status_bar.pack(side="bottom", fill="x")

on_algo_change()  
update_strength_indicator()
update_ui_language()

root.mainloop()