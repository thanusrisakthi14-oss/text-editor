import tkinter as tk
from tkinter import filedialog

window=tk.Tk()
window.title("Text Editor")
window.geometry("400x400")
text_area=tk.Text(window)
text_area.pack()

def save_file():
    file=filedialog.asksaveasfilename(defaultextension=".txt",filetypes=[("Text Files","*.txt")])
    if file:
        f=open(file,"w")
        f.write(text_area.get("1.0",tk.END))

def open_file():
    file=filedialog.askopenfilename(filetypes=[("Text Files","*.txt")])
    if file:
        text_area.delete("1.0",tk.END)
        f=open(file,"r")
        text_area.insert(tk.END,f.read())

save_btn=tk.Button(window,text="Save File",command=save_file)

save_btn.pack(side="left",padx=10,pady=10)

open_btn=tk.Button(window,text="Open File",command=open_file)

open_btn.pack(side="left",padx=10,pady=10)

window.mainloop()