from tkinter import *

def convert_temp():
    celsius = float(celsius_entry.get())
    fahrenheit = (celsius * 9/5) + 32
    fahrenheit_label.config(text=f"{fahrenheit:.2f} градусов Фаренгейта")

root = Tk()
root.title("Конвертер температуры")
root.geometry("300x150")

celsius_label = Label(root, text="Введите температуру в градусах Цельсия:")
celsius_label.pack()

celsius_entry = Entry(root)
celsius_entry.pack()

convert_button = Button(root, text="Конвертировать", command=convert_temp)
convert_button.pack()

fahrenheit_label = Label(root, text="")
fahrenheit_label.pack()

root.mainloop()
