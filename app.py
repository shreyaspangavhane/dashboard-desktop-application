import tkinter as tk
from tkinter import filedialog, ttk, messagebox
import pandas as pd

# Create main window
root = tk.Tk()
root.title("CSV Manager")
root.geometry("900x600")
root.configure(bg="#f0f0f0")

data = None
file_path = None
ascending_order = True  # To toggle sorting order

# Apply a modern theme
style = ttk.Style()
style.theme_use("clam")

style.configure("Treeview",
                background="white",
                foreground="black",
                rowheight=25,
                fieldbackground="white")

style.configure("Treeview.Heading",
                font=("Arial", 11, "bold"),
                background="#4CAF50",
                foreground="white")

# Frame for Search & Table
top_frame = tk.Frame(root, bg="white")
top_frame.pack(pady=10, padx=20, fill="x")

search_label = tk.Label(top_frame, text="Search:", bg="white", font=("Arial", 10, "bold"))
search_label.pack(side="left", padx=5)

search_entry = tk.Entry(top_frame, font=("Arial", 10))
search_entry.pack(side="left", padx=5, fill="x", expand=True)

tree_frame = tk.Frame(root, bg="white", bd=2, relief="sunken")
tree_frame.pack(padx=20, pady=10, fill="both", expand=True)

tree = ttk.Treeview(tree_frame, selectmode="browse")
tree.pack(expand=True, fill="both", padx=10, pady=10)

# Input Frame
entry_frame = tk.Frame(root, bg="white", bd=2, relief="ridge")
entry_frame.pack(pady=10, padx=20, fill="x")

# Buttons Frame
buttons_frame = tk.Frame(root, bg="#f0f0f0")
buttons_frame.pack(pady=10)

entries = []
labels = []

def upload_csv():
    global data, file_path
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if file_path:
        data = pd.read_csv(file_path)
        display_data(data)

def display_data(df):
    global entries, labels

    tree.delete(*tree.get_children())

    tree["columns"] = list(df.columns)
    tree["show"] = "headings"

    for col in df.columns:
        tree.heading(col, text=col, command=lambda c=col: sort_column(c))
        tree.column(col, width=120)

    for i, row in df.iterrows():
        color = "lightgray" if i % 2 == 0 else "white"
        tree.insert("", tk.END, values=list(row), tags=(color,))
    tree.tag_configure("lightgray", background="#f9f9f9")

    for widget in entry_frame.winfo_children():
        widget.destroy()

    entries.clear()
    labels.clear()

    for i, col in enumerate(df.columns):
        lbl = tk.Label(entry_frame, text=col, bg="white", font=("Arial", 10, "bold"))
        lbl.grid(row=0, column=i, padx=5, pady=5)
        labels.append(lbl)

        entry = tk.Entry(entry_frame, font=("Arial", 10))
        entry.grid(row=1, column=i, padx=5, pady=5)
        entries.append(entry)

def add_data():
    global data
    new_row = [entry.get() for entry in entries]
    
    if data is not None:
        data.loc[len(data)] = new_row
        display_data(data)

def update_data():
    global data
    selected_item = tree.selection()
    if selected_item:
        index = tree.index(selected_item[0])
        updated_row = [entry.get() for entry in entries]
        data.iloc[index] = updated_row
        display_data(data)

def delete_data():
    global data
    selected_item = tree.selection()
    if selected_item:
        index = tree.index(selected_item[0])
        data = data.drop(data.index[index]).reset_index(drop=True)
        display_data(data)

def save_csv():
    global data, file_path
    if data is not None and file_path is not None:
        data.to_csv(file_path, index=False)
        messagebox.showinfo("Success", "CSV file saved successfully!")

def search_data():
    global data
    query = search_entry.get().lower()
    if data is not None:
        filtered_data = data[data.apply(lambda row: row.astype(str).str.contains(query, case=False).any(), axis=1)]
        display_data(filtered_data)

def sort_column(column):
    global data, ascending_order
    if data is not None:
        data = data.sort_values(by=[column], ascending=ascending_order)
        ascending_order = not ascending_order
        display_data(data)

search_entry.bind("<KeyRelease>", lambda event: search_data())

btn_style = {"font": ("Arial", 10, "bold"), "bg": "#4CAF50", "fg": "white", "padx": 10, "pady": 5, "bd": 2}

btn_upload = tk.Button(root, text="Upload CSV", command=upload_csv, **btn_style)
btn_upload.pack(pady=5)

btn_add = tk.Button(buttons_frame, text="Add", command=add_data, **btn_style)
btn_add.grid(row=0, column=0, padx=10)

btn_update = tk.Button(buttons_frame, text="Update", command=update_data, **btn_style)
btn_update.grid(row=0, column=1, padx=10)

btn_delete = tk.Button(buttons_frame, text="Delete", command=delete_data, **btn_style)
btn_delete.grid(row=0, column=2, padx=10)

btn_save = tk.Button(buttons_frame, text="Save CSV", command=save_csv, **btn_style)
btn_save.grid(row=0, column=3, padx=10)

root.mainloop()
