# heatmap_app.py
import tkinter as tk
from tkinter import ttk, filedialog
import heatmap

class HeatmapApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Cambodia Map to Sustainability")
        self.configure(bg="#FAF0E6")  # Set creamy background color

        self.heatmap = heatmap.Heatmap()

        # Configure button colors
        button_bg = "#8B4513"  # Darker brown color
        button_fg = "white"
        button_hover_bg = "#A0522D"  # Lighter brown color for hover effect

        # Create style for ttk widgets
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TCombobox', fieldbackground=button_bg, background=button_bg, foreground=button_fg, arrowcolor=button_fg)
        style.map('TCombobox', fieldbackground=[('readonly', button_bg)], background=[('readonly', button_bg)], foreground=[('readonly', button_fg)], arrowcolor=[('readonly', button_fg)])

        # Title label
        title_label = tk.Label(self, text="Cambodia Map to Sustainability", bg="#FAF0E6", fg="#333", font=('Helvetica', 24, 'bold', 'underline'))
        title_label.pack(side="top", pady=20)

        # Frame to hold buttons
        self.button_frame = tk.Frame(self, bg="#FAF0E6")
        self.button_frame.pack(side="top", fill="x")

        # Combobox for selecting between deforestation and floods
        self.selection = tk.StringVar()
        self.combobox = ttk.Combobox(self.button_frame, textvariable=self.selection, values=["Deforestation", "Floods"], state="readonly", style="TCombobox")
        self.combobox.set("Select")
        self.combobox.pack(side="left", padx=5, pady=10, ipady=8, ipadx=8)  # Adjust ipady and ipadx values

        self.load_button = tk.Button(self.button_frame, text="Load Data", command=self.load_data, bg=button_bg, fg=button_fg, activebackground=button_hover_bg, relief=tk.FLAT, height=2, width=15)
        self.load_button.pack(side="left", padx=5, pady=10)

        self.visualize_button = tk.Button(self.button_frame, text="Visualize Heatmap", command=self.visualize_heatmap, bg=button_bg, fg=button_fg, activebackground=button_hover_bg, relief=tk.FLAT, height=2, width=15)
        self.visualize_button.pack(side="left", padx=5, pady=5)

        self.save_button = tk.Button(self.button_frame, text="Save Data", command=self.save_data, bg=button_bg, fg=button_fg, activebackground=button_hover_bg, relief=tk.FLAT, height=2, width=15)
        self.save_button.pack(side="left", padx=5, pady=5)

        self.quit_button = tk.Button(self.button_frame, text="Quit", command=self.quit, bg=button_bg, fg=button_fg, activebackground=button_hover_bg, relief=tk.FLAT, height=2, width=15)
        self.quit_button.pack(side="left", padx=5, pady=5)

        # Set button fonts
        button_font = ('Arial', 12, 'bold')
        self.combobox.config(font=button_font)
        self.load_button.config(font=button_font)
        self.visualize_button.config(font=button_font)
        self.save_button.config(font=button_font)
        self.quit_button.config(font=button_font)

        # Set button bindings for hover effect
        self.load_button.bind("<Enter>", self.on_enter)
        self.load_button.bind("<Leave>", self.on_leave)
        self.visualize_button.bind("<Enter>", self.on_enter)
        self.visualize_button.bind("<Leave>", self.on_leave)
        self.save_button.bind("<Enter>", self.on_enter)
        self.save_button.bind("<Leave>", self.on_leave)
        self.quit_button.bind("<Enter>", self.on_enter)
        self.quit_button.bind("<Leave>", self.on_leave)

        # Custom separator
        separator = tk.Frame(self, height=2, bg="#8B4513", bd=0, relief=tk.SUNKEN)
        separator.pack(fill='x', pady=10)

        # Set the initial size of the GUI window
        self.geometry("800x500")  # Width x Height

    def load_data(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            self.heatmap = heatmap.Heatmap(filePath=file_path)
            print("Data loaded successfully from:", file_path)

    def visualize_heatmap(self):
        selection = self.selection.get()
        if selection == "Deforestation":
            print("Visualizing deforestation heatmap")
        elif selection == "Floods":
            print("Visualizing floods heatmap")
        self.heatmap.constructHeatmap()

    def save_data(self):
        # Placeholder function for saving data
        print("Save Data button clicked")

    def on_enter(self, event):
        event.widget.config(bg="#A0522D")  # Lighter brown color on hover

    def on_leave(self, event):
        event.widget.config(bg="#8B4513")  # Restore brown color

def main():
    app = HeatmapApp()
    app.mainloop()

if __name__ == '__main__':
    main()
