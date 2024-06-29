import requests
from pypdf import PdfReader
import os
from pathlib import Path
from tkinter.filedialog import askopenfilename
from tkinter import *

API_KEY = os.environ["API_KEY"]

root = Tk()
root.geometry("360x150")
root.title("PDF To Audio")
text = ""


def open_file():
    global text
    text = ""
    pdf_file = askopenfilename()
    if pdf_file:
        reader = PdfReader(pdf_file)
        for page in reader.pages:
            text += page.extract_text() + "\n"
        file_name_label.config(text=f"Opened: {os.path.basename(pdf_file)}", fg="green")


def save_file(out_file="audio.mp3"):
    global text
    parameters["src"] = text
    out_file = Path(f"~/Desktop/{out_file}").expanduser()
    response = requests.get(url="http://api.voicerss.org/", params=parameters)
    response.raise_for_status()
    with open(out_file, "wb") as file:
        file.write(response.content)
    success_label.config(text="File saved successfully to Desktop!", fg="green")


parameters = {
    "key": API_KEY,
    "hl": "en-us",
    "src": text,
}

title = Label(root, text="Open a file to convert", font=("fixedsys", 22))
title.grid(row=0, column=0, columnspan=2)

file_name_label = Label(root, text="", font=("fixedsys", 12))
file_name_label.grid(row=1, column=0, columnspan=2)

open_button = Button(root, text="Open File", font=("fixedsys", 12), command=open_file)
open_button.grid(row=2, column=0)

success_label = Label(root, text="", font=("fixedsys", 12))
success_label.grid(row=3, column=0, columnspan=2)

save_button = Button(root, text="Save File", font=("fixedsys", 12), command=save_file)
save_button.grid(row=2, column=1)

root.mainloop()
