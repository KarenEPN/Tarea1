# Libraries
import os
import tkinter as tk
from tkinter import messagebox

# Function
def search_term():
    term = entry.get()
    results = []
    folder = "./libros"

    # Iterate through each document
    for file in os.listdir(folder):
        if file.endswith(".txt"):  # Only process text files
            document_path = os.path.join(folder, file)
        
            # Check if the search term appears in the document
            with open(document_path, 'r', encoding='utf-8') as f:
                content = f.read().lower()
                if term.lower() in content:
                    results.append(file)
    
    # Show the results in a popup window
    if results:
        message = f"The term '{term}' was found in the following documents:\n\n"
        for doc in results:
            message += f"- {doc}\n"
        messagebox.showinfo("Results", message)
    else:
        messagebox.showinfo("Results", f"The term '{term}' does not appear in any document.")

# Create the main window
window = tk.Tk()
window.title("SEARCH TASK")
window.geometry("400x250")

# Create an input field
label = tk.Label(window, text="Enter the term you want to search:")
label.pack(pady=5)
entry = tk.Entry(window, width=40)
entry.pack(pady=5)

# Create a button to start the search
search_button = tk.Button(window, text="Search", command=search_term)
search_button.pack(pady=5)

# Run the application
window.mainloop()
