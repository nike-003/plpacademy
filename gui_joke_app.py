import tkinter as tk
from tkinter import ttk, messagebox
import random

class JokeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Joke Generator App")
        self.root.geometry("500x400")
        self.root.configure(bg='#f0f0f0')
        
        # Jokes database
        self.jokes = [
            "Why don't scientists trust atoms? Because they are made up of everything!",
            "Why did the computer go to therapy? It had too many bytes!",
            "Why do programmers prefer dark mode? Because the light attracts bugs!",
            "Why did the student eat his homework? Because the teacher said it's a piece of cake!",
            "What do you call a bear with no teeth? A gummy bear!",
            "Why don't eggs tell jokes? They'd crack each other up!"
        ]
        
        self.setup_ui()
    
    def setup_ui(self):
        # Title
        title_label = tk.Label(
            self.root, 
            text="😄 Joke Generator", 
            font=("Arial", 24, "bold"),
            bg='#f0f0f0',
            fg='#333'
        )
        title_label.pack(pady=20)
        
        # Joke display frame
        joke_frame = tk.Frame(self.root, bg='#f0f0f0')
        joke_frame.pack(pady=20, padx=20, fill='both', expand=True)
        
        # Joke display
        self.joke_label = tk.Label(
            joke_frame,
            text="Click 'Get Joke' to start laughing!",
            font=("Arial", 12),
            bg='white',
            fg='#333',
            wraplength=400,
            justify='center',
            relief='solid',
            borderwidth=1,
            padx=20,
            pady=20
        )
        self.joke_label.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Buttons frame
        button_frame = tk.Frame(self.root, bg='#f0f0f0')
        button_frame.pack(pady=20)
        
        # Get Joke button
        get_joke_btn = tk.Button(
            button_frame,
            text="Get Joke",
            command=self.get_joke,
            font=("Arial", 12, "bold"),
            bg='#4CAF50',
            fg='white',
            relief='flat',
            padx=20,
            pady=10
        )
        get_joke_btn.pack(side='left', padx=5)
        
        # Add Joke button
        add_joke_btn = tk.Button(
            button_frame,
            text="Add Joke",
            command=self.show_add_joke_dialog,
            font=("Arial", 12, "bold"),
            bg='#2196F3',
            fg='white',
            relief='flat',
            padx=20,
            pady=10
        )
        add_joke_btn.pack(side='left', padx=5)
        
        # View All Jokes button
        view_all_btn = tk.Button(
            button_frame,
            text="View All",
            command=self.show_all_jokes,
            font=("Arial", 12, "bold"),
            bg='#FF9800',
            fg='white',
            relief='flat',
            padx=20,
            pady=10
        )
        view_all_btn.pack(side='left', padx=5)
    
    def get_joke(self):
        joke = random.choice(self.jokes)
        self.joke_label.config(text=joke)
    
    def show_add_joke_dialog(self):
        # Create a new window for adding jokes
        dialog = tk.Toplevel(self.root)
        dialog.title("Add New Joke")
        dialog.geometry("400x200")
        dialog.configure(bg='#f0f0f0')
        
        # Center the dialog
        dialog.transient(self.root)
        dialog.grab_set()
        
        # Title
        tk.Label(
            dialog,
            text="Enter your joke:",
            font=("Arial", 14, "bold"),
            bg='#f0f0f0'
        ).pack(pady=10)
        
        # Text entry
        joke_entry = tk.Text(dialog, height=4, width=40, font=("Arial", 10))
        joke_entry.pack(pady=10, padx=20)
        joke_entry.focus()
        
        # Buttons
        button_frame = tk.Frame(dialog, bg='#f0f0f0')
        button_frame.pack(pady=10)
        
        def add_joke():
            joke_text = joke_entry.get("1.0", tk.END).strip()
            if joke_text:
                self.jokes.append(joke_text)
                messagebox.showinfo("Success", "Joke added successfully!")
                dialog.destroy()
            else:
                messagebox.showerror("Error", "Please enter a joke!")
        
        tk.Button(
            button_frame,
            text="Add Joke",
            command=add_joke,
            bg='#4CAF50',
            fg='white',
            font=("Arial", 10, "bold"),
            relief='flat',
            padx=15,
            pady=5
        ).pack(side='left', padx=5)
        
        tk.Button(
            button_frame,
            text="Cancel",
            command=dialog.destroy,
            bg='#f44336',
            fg='white',
            font=("Arial", 10, "bold"),
            relief='flat',
            padx=15,
            pady=5
        ).pack(side='left', padx=5)
    
    def show_all_jokes(self):
        # Create a new window to show all jokes
        dialog = tk.Toplevel(self.root)
        dialog.title("All Jokes")
        dialog.geometry("500x400")
        dialog.configure(bg='#f0f0f0')
        
        # Title
        tk.Label(
            dialog,
            text=f"All Jokes ({len(self.jokes)} total)",
            font=("Arial", 16, "bold"),
            bg='#f0f0f0'
        ).pack(pady=10)
        
        # Create a scrollable text widget
        text_widget = tk.Text(dialog, height=15, width=60, font=("Arial", 10))
        scrollbar = tk.Scrollbar(dialog, orient="vertical", command=text_widget.yview)
        text_widget.configure(yscrollcommand=scrollbar.set)
        
        text_widget.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        scrollbar.pack(side="right", fill="y")
        
        # Insert all jokes
        for i, joke in enumerate(self.jokes, 1):
            text_widget.insert(tk.END, f"{i}. {joke}\n\n")
        
        text_widget.config(state=tk.DISABLED)

def main():
    root = tk.Tk()
    app = JokeApp(root)
    root.mainloop()

if __name__ == "__main__":
    main() 