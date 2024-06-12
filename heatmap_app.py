import sys
import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
import heatmap
import os

#tkinter is used for the GUI

class HeatmapApp(tk.Tk):
    def __init__(self):
        super().__init__()

        #title with colour background
        self.title("Cambodia Map to Sustainability")
        self.configure(bg="#F0F6FC")

        #initialise heatmap object
        self.heatmap = heatmap.Heatmap()

        #Button colours
        button_bg = "#2196F3"
        button_fg = "white"
        button_hover_bg = "#64B5F6"

        #style for widgets
        style = ttk.Style()
        style.theme_use('clam')

        #title label
        title_label = tk.Label(self, text="Cambodia Map to Sustainability", bg="#F0F6FC", fg="#333", font=('Helvetica', 24, 'bold', 'underline'))
        title_label.grid(row=0, column=0, columnspan=5, pady=20, sticky="ew")

        #button frame
        self.button_frame = tk.Frame(self, bg="#F0F6FC")
        self.button_frame.grid(row=1, column=0, columnspan=5, pady=(0, 10), sticky="ew")
        self.button_frame.grid_columnconfigure(0, weight=1)
        self.button_frame.grid_columnconfigure(1, weight=1)
        self.button_frame.grid_columnconfigure(2, weight=1)
        self.button_frame.grid_columnconfigure(3, weight=1)

        # Create buttons for loading data, visualizing heatmap, saving data, and quitting
        self.load_button = tk.Button(self.button_frame, text="Load Data", command=self.load_data, bg=button_bg, fg=button_fg, activebackground=button_hover_bg, relief=tk.FLAT, height=2, width=15)
        self.load_button.grid(row=0, column=0, padx=5, pady=10, sticky="ew")
        self.visualize_button = tk.Button(self.button_frame, text="Visualize Heatmap", command=self.visualize_heatmap, bg=button_bg, fg=button_fg, activebackground=button_hover_bg, relief=tk.FLAT, height=2, width=15)
        self.visualize_button.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.save_button = tk.Button(self.button_frame, text="Save Data", command=self.save_data, bg=button_bg, fg=button_fg, activebackground=button_hover_bg, relief=tk.FLAT, height=2, width=15)
        self.save_button.grid(row=0, column=2, padx=5, pady=5, sticky="ew")
        self.quit_button = tk.Button(self.button_frame, text="Quit", command=self.quit, bg=button_bg, fg=button_fg, activebackground=button_hover_bg, relief=tk.FLAT, height=2, width=15)
        self.quit_button.grid(row=0, column=3, padx=5, pady=5, sticky="ew")
        button_font = ('Arial', 12, 'bold')
        self.load_button.config(font=button_font)
        self.visualize_button.config(font=button_font)
        self.save_button.config(font=button_font)
        self.quit_button.config(font=button_font)

        #the line underneath the buttons
        separator = tk.Frame(self, height=2, bg="#1976D2", bd=0, relief=tk.SUNKEN)  # Dark blue separator
        separator.grid(row=2, column=0, columnspan=5, sticky="ew", pady=(0, 10))

        # Load the guide image
        self.guide_image = Image.open("guide.jpg")
        self.guide_photo = ImageTk.PhotoImage(self.guide_image)

        # Create a label to display the guide image
        self.guide_label = tk.Label(self, image=self.guide_photo, bg="#F0F6FC")
        self.guide_label.grid(row=3, column=0, padx=20, pady=20, rowspan=3, sticky="nsew")

        # frame for the input widgets and the submit button
        input_frame = tk.Frame(self, bg="#F0F6FC")
        input_frame.grid(row=3, column=1, columnspan=4, padx=20, pady=20, sticky="nsew")

        #labels for inputs
        coordinate_label = tk.Label(input_frame, text="Coordinate:", bg="#F0F6FC", fg="#333", font=('Arial', 12, 'bold'))
        coordinate_label.grid(row=0, column=0, padx=(0, 5), pady=10, sticky="e")

        #entry widgets for coordinates and description
        self.coordinate_entry = tk.Entry(input_frame, bg="white", fg="black", relief=tk.FLAT, width=10)
        self.coordinate_entry.grid(row=0, column=1, padx=(0, 5), pady=10, sticky="ew")
        description_label = tk.Label(input_frame, text="Description:", bg="#F0F6FC", fg="#333", font=('Arial', 12, 'bold'))
        description_label.grid(row=1, column=0, padx=(0, 5), pady=10, sticky="e")
        self.description_entry = tk.Entry(input_frame, bg="white", fg="black", relief=tk.FLAT, width=20)
        self.description_entry.grid(row=1, column=1, padx=(0, 5), pady=10, sticky="ew")

        #submit button
        self.submit_button = tk.Button(input_frame, text="Submit", command=self.log_incident, bg=button_bg, fg=button_fg, activebackground=button_hover_bg, relief=tk.FLAT, height=2, width=15)
        self.submit_button.grid(row=0, column=2, rowspan=2, padx=5, pady=10, sticky="ns")
        self.submit_button.config(font=button_font)

        #guide text below the submit button and input fields
        guide_text = ("HOW TO USE:\n"
                      "1. Press load data\n"
                      "2. Press data.txt\n"
                      "3. Press visualize\n"
                      "4. Plot the coordinate (e.g. A1) using the guide and write any description\n"
                      "5. Press submit\n"
                      "6. Press visualize to see how it is updated\n"
                      "7. Press save if you are happy with it")

        guide_frame = tk.Frame(input_frame, bg="#2196F3", bd=2, relief=tk.SOLID)
        guide_frame.grid(row=2, column=0, columnspan=3, pady=20, sticky="ew")

        guide_label = tk.Label(guide_frame, text=guide_text, bg="#2196F3", fg="black", font=('Arial', 10), anchor="w", justify="left")
        guide_label.pack(padx=10, pady=10, fill="both", expand=True)

        # Configure row and column weights to make the content resize with the window
        for i in range(4):
            self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(i, weight=1)

        print("GUI initialized successfully.")

    def load_data(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            self.heatmap = heatmap.Heatmap(filePath=file_path)
            print("Data loaded successfully from:", file_path)

    def visualize_heatmap(self):
        self.heatmap.constructHeatmap()
        print("Heatmap visualized.")
        # Show the generated heatmap image
        heatmap_image = Image.open("generatedHeatmap.jpg")
        heatmap_photo = ImageTk.PhotoImage(heatmap_image)
        
        # label to display the generated heatmap image
        if hasattr(self, "heatmap_label"):
            self.heatmap_label.destroy()
        
        self.heatmap_label = tk.Label(self, image=heatmap_photo, bg="#F0F6FC")
        self.heatmap_label.image = heatmap_photo
        self.heatmap_label.grid(row=3, column=0, padx=20, pady=20, rowspan=3, sticky="nsew")


    def save_data(self):
        print("Save Data button clicked")
        self.heatmap.saveHeatmapData()
        print("Data saved successfully.")

    def quit(self):
        self.destroy()
        sys.exit()

    def log_incident(self):
        coordinates = self.coordinate_entry.get()
        description = self.description_entry.get()
        self.heatmap.inputHeatmapData(coordinates, description)
        print("Incident logged:", coordinates, description)

def main():
    app = HeatmapApp()
    app.mainloop()
    print("HeatmapApp main loop started.")

if __name__ == '__main__':
    main()
