"""
Переделать практическую в tkinter
Практическая 7_1
Дана строка. Преобразовать в ней все строчные буквы (как латинские, так и русские)
в прописные, а прописные — в строчные.
"""
import tkinter as tk

def swap_case(text):
    return text.swapcase()

def convert():
    text = entry.get()
    result = swap_case(text)
    label_result.config(text=result)

root = tk.Tk()
root.title("Преобразование регистра")
root.geometry("400x200")

label = tk.Label(root, text="Введите строку:")
label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

btn = tk.Button(root, text="Преобразовать", command=convert)
btn.pack(pady=10)

label_result = tk.Label(root, text="Результат: ", font=("Arial", 10, "bold"))
label_result.pack(pady=10)

root.mainloop()