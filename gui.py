import tkinter as tk
from tkinter import messagebox, font
import json
import csv

with open('model\keypoint_classifier\keypoint_classifier_label.csv', newline='') as f:
    reader = csv.reader(f)
    gestureList = list(reader)
    print(gestureList)
current_sequence = []


root = tk.Tk()
root.title("PlaceHolder")
root.geometry("520x600")
root.configure(bg="#e8f0fe")  # Soft blue background


title_font = font.Font(family="Helvetica", size=20, weight="bold")
section_font = font.Font(family="Helvetica", size=12)
button_font = font.Font(family="Helvetica", size=11)
