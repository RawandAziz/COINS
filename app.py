import tkinter as tk
from tkinter import ttk
import extractor

path = r"C:\Users\there\Documents\Code\Numismatics\OCR\pdfs\simple\Ariel and Berman - The Coins from Khirbat Burin.pdf"

values = [
    "ID",
    "Name",
    "Latitude",
    "Longitude",
    "Start_Year",
    "End_Year",
    "Num_Coins_Found",
    "Reference",
    "Comment",
    "External_Link",
    "None"
    ]

maps = []

def on_button_click():
    labels = extractor.getLabels(path)
    create_boxes(labels)
    
    # label.config(text="Extracting...")
    button.destroy()

def create_boxes(labels):
    n = len(labels)
    boxes = []
    frames = []
    for i in range(n):
        frame = tk.Frame(app)
        map = tk.StringVar()
        box = ttk.Combobox(master=frame, values=values, textvariable=map, state="readonly")
        box.set("None")
        boxes.append(box)
        frames.append(frame)
        maps.append(map)
        
    for i in range(len(boxes)):
        box = boxes[i]
        frame = frames[i]
        
        labelText = tk.StringVar()
        labelText.set(labels[i])
        label = tk.Label(frame, textvariable=labelText, height=1)
        label.pack(side="left")  # Pack each label on a new row
        box.pack(side="left")
        frame.pack(side="top", padx=8, pady=8)
    
def run():
    mapping = {}
    for i, map in enumerate(maps):
        if map != "None":
            mapping[i] = map

    extractor.run(mapping, None, "Ruler", path)

# Main application window
app = tk.Tk()
app.title("COINS")

label = tk.Label(app, text="COINS")
label.pack()

button = tk.Button(app, text="Extract Tables", command=on_button_click)
button.pack()

runButton = tk.Button(app, text="Run", command=run)
runButton.pack()

app.mainloop()