#2 вариант
import tkinter as tk

okno = tk.Tk()
okno.title("Заявка на работу в зоопарке")
okno.geometry("600x850")
okno.configure(bg="#e8e8e8")

zagolovok = tk.Label(okno, text="Форма заявки на работу в зоопарке", font=("Arial", 13, "bold"), bg="#e8e8e8")
zagolovok.pack(pady=10)

podzagolovok = tk.Label(okno, text="Пожалуйста, заполните форму. Обязательные поля помечены *", font=("Arial", 9), bg="#e8e8e8", fg="gray")
podzagolovok.pack()

canvas = tk.Canvas(okno, bg="#e8e8e8", highlightthickness=0)
polzunok = tk.Scrollbar(okno, orient="vertical", command=canvas.yview)
vnutrennyaya_ramka = tk.Frame(canvas, bg="#e8e8e8")

canvas.create_window((0, 0), window=vnutrennyaya_ramka, anchor="nw")
canvas.configure(yscrollcommand=polzunok.set)
vnutrennyaya_ramka.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

canvas.pack(side="left", fill="both", expand=True)
polzunok.pack(side="right", fill="y")

ramka1 = tk.LabelFrame(vnutrennyaya_ramka, text="Контактная информация", font=("Arial", 10, "bold"), bg="#e8e8e8", padx=10, pady=5)
ramka1.pack(fill="x", padx=20, pady=10)

kontakt = tk.Frame(ramka1, bg="#e8e8e8")
kontakt.pack(pady=10)

tk.Label(kontakt, text="Имя *", bg="#e8e8e8", font=("Arial", 9)).grid(row=0, column=0, padx=5, pady=5, sticky="e")
imya = tk.Entry(kontakt, width=25)
imya.grid(row=0, column=1, padx=5, pady=5)

tk.Label(kontakt, text="Телефон", bg="#e8e8e8", font=("Arial", 9)).grid(row=1, column=0, padx=5, pady=5, sticky="e")
telefon = tk.Entry(kontakt, width=25)
telefon.grid(row=1, column=1, padx=5, pady=5)

tk.Label(kontakt, text="Email *", bg="#e8e8e8", font=("Arial", 9)).grid(row=2, column=0, padx=5, pady=5, sticky="e")
email = tk.Entry(kontakt, width=25)
email.grid(row=2, column=1, padx=5, pady=5)

ramka2 = tk.LabelFrame(vnutrennyaya_ramka, text="Персональная информация", font=("Arial", 10, "bold"), bg="#e8e8e8", padx=10, pady=5)
ramka2.pack(fill="x", padx=20, pady=10)

personal = tk.Frame(ramka2, bg="#e8e8e8")
personal.pack(pady=10)

tk.Label(personal, text="Возраст *", bg="#e8e8e8", font=("Arial", 9)).grid(row=0, column=0, padx=5, pady=5, sticky="e")
vozrast = tk.Entry(personal, width=10)
vozrast.grid(row=0, column=1, padx=5, pady=5, sticky="w")

tk.Label(personal, text="Пол", bg="#e8e8e8", font=("Arial", 9)).grid(row=1, column=0, padx=5, pady=5, sticky="e")
spisok_pola = tk.Listbox(personal, height=2, width=30)
spisok_pola.insert(1, "Женщина")
spisok_pola.insert(2, "Мужчина")
spisok_pola.select_set(0)
spisok_pola.grid(row=1, column=1, padx=5, pady=5, sticky="w")

tk.Label(personal, text="Личные качества", bg="#e8e8e8", font=("Arial", 9)).grid(row=2, column=0, padx=5, pady=5, sticky="e")
kachestva = tk.Text(personal, width=30, height=3)
kachestva.grid(row=2, column=1, padx=5, pady=5)

ramka3 = tk.LabelFrame(vnutrennyaya_ramka, text="Выберите ваших любимых животных", font=("Arial", 10, "bold"), bg="#e8e8e8", padx=10, pady=5)
ramka3.pack(fill="x", padx=20, pady=10)

zivotnye = ["Зебра", "Кошак", "Анаконда", "Человек", "Слон", "Антилопа", "Голубь", "Краб"]

frame_zivotnye = tk.Frame(ramka3, bg="#e8e8e8")
frame_zivotnye.pack(pady=10)

chekboxy = []
for i in range(len(zivotnye)):
    var = tk.BooleanVar()
    chekboxy.append(var)
    stroka = i // 4
    stolbec = i % 4
    cb = tk.Checkbutton(frame_zivotnye, text=zivotnye[i], variable=var, bg="#e8e8e8", font=("Arial", 9))
    cb.grid(row=stroka, column=stolbec, padx=15, pady=5, sticky="w")

frame_knopki = tk.Frame(vnutrennyaya_ramka, bg="#e8e8e8")
frame_knopki.pack(fill="x", padx=20, pady=15)



def otpravit():
    rezultat.delete(1.0, tk.END)

    oshibki = []
    if not imya.get().strip():
        oshibki.append("Имя")
    if not email.get().strip():
        oshibki.append("Email")
    if not vozrast.get().strip():
        oshibki.append("Возраст")

    if oshibki:
        rezultat.insert(tk.END, f"ОШИБКА!\nЗаполните: {', '.join(oshibki)}")
        return

    try:
        leta = int(vozrast.get())
    except:
        rezultat.insert(tk.END, "ОШИБКА!\nВозраст должен быть числом")
        return

    vybranny_pol = spisok_pola.get(spisok_pola.curselection())

    vybrannye = []
    for i in range(len(zivotnye)):
        if chekboxy[i].get():
            vybrannye.append(zivotnye[i])

    rezultat.insert(tk.END, "ЗАЯВКА ОТПРАВЛЕНА!\n\n")
    rezultat.insert(tk.END, f"Имя: {imya.get()}\n")
    rezultat.insert(tk.END, f"Телефон: {telefon.get() if telefon.get() else 'не указан'}\n")
    rezultat.insert(tk.END, f"Email: {email.get()}\n")
    rezultat.insert(tk.END, f"Возраст: {vozrast.get()}\n")
    rezultat.insert(tk.END, f"Пол: {vybranny_pol}\n")
    rezultat.insert(tk.END,
                    f"Качества: {kachestva.get('1.0', tk.END).strip() if kachestva.get('1.0', tk.END).strip() else 'не указаны'}\n\n")
    rezultat.insert(tk.END, f"Любимые животные: {', '.join(vybrannye) if vybrannye else 'не выбраны'}")

knopka = tk.Button(frame_knopki, text="Отправить информацию", command=otpravit, font=("Arial", 9), padx=15, pady=3)
knopka.pack(side="left")

ramka4 = tk.LabelFrame(vnutrennyaya_ramka, text="Результат", font=("Arial", 10, "bold"), bg="#e8e8e8", padx=10, pady=5)
ramka4.pack(fill="both", expand=True, padx=20, pady=10)

rezultat = tk.Text(ramka4, height=8, width=50, wrap=tk.WORD)
rezultat.pack(fill="both", expand=True, padx=5, pady=5)

okno.mainloop()