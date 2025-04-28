import tkinter as tk
from tkinter import messagebox, font
import json


available_gestures = ["Open", "Close", "Pointer", "Vit", "Fireball", "Rock'n'Roll"]
current_sequence = []


root = tk.Tk()
root.title("PlaceHolder")
root.geometry("520x600")
root.configure(bg="#e8f0fe")  # Soft blue background


title_font = font.Font(family="Helvetica", size=20, weight="bold")
section_font = font.Font(family="Helvetica", size=12)
button_font = font.Font(family="Helvetica", size=11)
