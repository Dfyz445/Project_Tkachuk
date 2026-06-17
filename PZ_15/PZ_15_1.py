"""
Вариант 18
Приложение СТРАХОВАЯ КОМПАНИЯ для некоторой организации.
БД должна содержать таблицу Договор со следующей структурой записи:
дата заключения, страховая сумма, вид страхования, тарифная ставка и филиал,
в котором заключался договор.
"""
import sqlite3
import re
from datetime import datetime

DB_NAME = "insurance.db"
TABLE_NAME = "Договор"

#Создание таблицы
def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            дата_заключения TEXT NOT NULL,
            страховая_сумма REAL NOT NULL,
            вид_страхования TEXT NOT NULL,
            тарифная_ставка REAL NOT NULL,
            филиал TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

#Проверка даты
def is_valid_date(date_str):
    pattern = r"^\d{4}-\d{2}-\d{2}$"
    if not re.match(pattern, date_str):
        return False
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

#Ввод положительного числа
def input_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Значение должно быть положительным. Попробуйте снова.")
                continue
            return value
        except ValueError:
            print("Ошибка: введите число (например, 1000.50).")

#Функция ввода
def insert_initial_data():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(f"SELECT COUNT(*) FROM {TABLE_NAME}")
    count = cursor.fetchone()[0]
    if count >= 10:
        print("В таблице уже есть 10 или более записей. Ввод пропущен.")
        conn.close()
        return

    print("\n--- Ввод 10 записей в таблицу 'Договор' ---")
    for i in range(1, 11):
        print(f"\nЗапись {i}:")
        while True:
            date_input = input("Дата заключения (ГГГГ-ММ-ДД): ")
            if is_valid_date(date_input):
                break
            print("Неверный формат даты. Используйте ГГГГ-ММ-ДД.")

        sum_insured = input_positive_float("Страховая сумма (руб.): ")
        insurance_type = input("Вид страхования: ")
        tariff_rate = input_positive_float("Тарифная ставка (%): ")
        branch = input("Филиал: ")

        try:
            cursor.execute(f"""
                INSERT INTO {TABLE_NAME}
                (дата_заключения, страховая_сумма, вид_страхования,
                 тарифная_ставка, филиал)
                VALUES (?, ?, ?, ?, ?)
            """, (date_input, sum_insured, insurance_type, tariff_rate, branch))
            conn.commit()
            print("Запись добавлена.")
        except sqlite3.Error as e:
            print(f"Ошибка при вставке: {e}")

    conn.close()
    print("\nВвод 10 записей завершен.")

#Функция поиска
def search_records():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    print("\n--- Поиск записей ---")
    print("Выберите тип поиска:")
    print("1. По филиалу и минимальной страховой сумме")
    print("2. По виду страхования и дате (начиная с указанной)")
    print("3. По диапазону тарифной ставки")

    choice = input("Ваш выбор (1-3): ")

    try:
        if choice == "1":
            branch = input("Введите филиал: ")
            min_sum = input_positive_float("Введите минимальную страховую сумму: ")
            cursor.execute(f"""
                SELECT * FROM {TABLE_NAME}
                WHERE филиал = ? AND страховая_сумма >= ?
                ORDER BY страховая_сумма DESC
            """, (branch, min_sum))
            rows = cursor.fetchall()
            print(f"\nНайдено записей: {len(rows)}")
            for row in rows:
                print(row)

        elif choice == "2":
            ins_type = input("Введите вид страхования: ")
            start_date = input("Введите начальную дату (ГГГГ-ММ-ДД): ")
            if not is_valid_date(start_date):
                print("Неверный формат даты.")
                conn.close()
                return
            cursor.execute(f"""
                SELECT * FROM {TABLE_NAME}
                WHERE вид_страхования = ? AND дата_заключения >= ?
                ORDER BY дата_заключения
            """, (ins_type, start_date))
            rows = cursor.fetchall()
            print(f"\nНайдено записей: {len(rows)}")
            for row in rows:
                print(row)

        elif choice == "3":
            min_rate = input_positive_float("Введите минимальную тарифную ставку: ")
            max_rate = input_positive_float("Введите максимальную тарифную ставку: ")
            cursor.execute(f"""
                SELECT * FROM {TABLE_NAME}
                WHERE тарифная_ставка BETWEEN ? AND ?
                ORDER BY тарифная_ставка
            """, (min_rate, max_rate))
            rows = cursor.fetchall()
            print(f"\nНайдено записей: {len(rows)}")
            for row in rows:
                print(row)

        else:
            print("Неверный выбор.")

    except sqlite3.Error as e:
        print(f"Ошибка при поиске: {e}")

    conn.close()

#Функция удаления
def delete_records():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    print("\n--- Удаление записей ---")
    print("Выберите тип удаления:")
    print("1. По филиалу")
    print("2. По виду страхования и дате (раньше указанной)")
    print("3. По тарифной ставке (выше указанной)")
    choice = input("Ваш выбор (1-3): ")

    try:
        if choice == "1":
            branch = input("Введите филиал для удаления: ")
            cursor.execute(f"DELETE FROM {TABLE_NAME} WHERE филиал = ?", (branch,))
            conn.commit()
            print(f"Удалено записей: {cursor.rowcount}")

        elif choice == "2":
            ins_type = input("Введите вид страхования: ")
            end_date = input("Введите дату (ГГГГ-ММ-ДД), раньше которой удалить: ")
            if not is_valid_date(end_date):
                print("Неверный формат даты.")
                conn.close()
                return
            cursor.execute(f"""
                DELETE FROM {TABLE_NAME}
                WHERE вид_страхования = ? AND дата_заключения < ?
            """, (ins_type, end_date))
            conn.commit()
            print(f"Удалено записей: {cursor.rowcount}")

        elif choice == "3":
            rate_threshold = input_positive_float("Введите тарифную ставку (выше которой удалить): ")
            cursor.execute(f"DELETE FROM {TABLE_NAME} WHERE тарифная_ставка > ?", (rate_threshold,))
            conn.commit()
            print(f"Удалено записей: {cursor.rowcount}")

        else:
            print("Неверный выбор.")

    except sqlite3.Error as e:
        print(f"Ошибка при удалении: {e}")
    conn.close()

#Функция редактирования
def update_records():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    print("\n--- Редактирование записей ---")
    print("Выберите тип редактирования:")
    print("1. Увеличить страховую сумму на процент для филиала")
    print("2. Изменить тарифную ставку для вида страхования")
    print("3. Обновить филиал для договоров с датой позже указанной")
    choice = input("Ваш выбор (1-3): ")

    try:
        if choice == "1":
            branch = input("Введите филиал: ")
            percent = input_positive_float("Введите процент увеличения (например, 10 для 10%): ")
            cursor.execute(f"""
                UPDATE {TABLE_NAME}
                SET страховая_сумма = страховая_сумма * (1 + ? / 100)
                WHERE филиал = ?
            """, (percent, branch))
            conn.commit()
            print(f"Обновлено записей: {cursor.rowcount}")

        elif choice == "2":
            ins_type = input("Введите вид страхования: ")
            new_rate = input_positive_float("Введите новую тарифную ставку: ")
            cursor.execute(f"""
                UPDATE {TABLE_NAME}
                SET тарифная_ставка = ?
                WHERE вид_страхования = ?
            """, (new_rate, ins_type))
            conn.commit()
            print(f"Обновлено записей: {cursor.rowcount}")

        elif choice == "3":
            date_from = input("Введите дату (ГГГГ-ММ-ДД), позже которой обновить филиал: ")
            if not is_valid_date(date_from):
                print("Неверный формат даты.")
                conn.close()
                return
            new_branch = input("Введите новый филиал: ")
            cursor.execute(f"""
                UPDATE {TABLE_NAME}
                SET филиал = ?
                WHERE дата_заключения > ?
            """, (new_branch, date_from))
            conn.commit()
            print(f"Обновлено записей: {cursor.rowcount}")

        else:
            print("Неверный выбор.")

    except sqlite3.Error as e:
        print(f"Ошибка при редактировании: {e}")

    conn.close()

#Главное меню
def main_menu():
    create_table()
    while True:
        print("\n" + "=" * 50)
        print("        СТРАХОВАЯ КОМПАНИЯ - Управление договорами")
        print("=" * 50)
        print("1. Ввести 10 записей")
        print("2. Поиск записей")
        print("3. Удаление записей")
        print("4. Редактирование записей")
        print("5. Показать все записи")
        print("6. Выход")
        print("=" * 50)
        choice = input("Выберите действие (1-6): ")

        if choice == "1":
            insert_initial_data()
        elif choice == "2":
            search_records()
        elif choice == "3":
            delete_records()
        elif choice == "4":
            update_records()
        elif choice == "5":
            show_all_records()
        elif choice == "6":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

def show_all_records():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute(f"SELECT * FROM {TABLE_NAME}")
        rows = cursor.fetchall()
        if not rows:
            print("Таблица пуста.")
        else:
            print("\n--- Все записи ---")
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(f"Ошибка при чтении данных: {e}")
    conn.close()

if __name__ == "__main__":
    main_menu()