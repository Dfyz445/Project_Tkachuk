"""
Средствами языка Python сформировать текстовый файл (.txt),
содержащий последовательность из целых положительных и отрицательных чисел.
Сформировать новый текстовый файл (.txt) следующего вида,
предварительно выполнив требуемую обработку элементов:

Количество элементов:
Среднее арифметическое элементов:
Последовательность, в которой каждый последующий элемент равен квадрату суммы двух
соседних элементов:
"""
with open('numbers.txt', 'w', encoding='utf-8') as file:
    content = file.write("1 2 46 -865 868 69 -89 0")

with open('numbers.txt', 'r') as file:
    content = file.read()
    parts = content.split()
    numbers = []
    for part in parts:
        numbers.append(int(part))

count = len(numbers)
average = sum(numbers) / count

new_sequence = []
n = len(numbers)

for i in range(n):
    left = numbers[(i - 1) % n]
    right = numbers[(i + 1) % n]
    new_value = (left + right) ** 2
    new_sequence.append(new_value)

with open('result.txt', 'w', encoding='utf-8') as file:
    file.write(f"Количество элементов: {count}\n")
    file.write(f"Среднее арифметическое элементов: {average:}\n")
    file.write("Новая последовательность: ")
    str_sequence = []
    for num in new_sequence:
        str_sequence.append(str(num))
    file.write(' '.join(str_sequence))
print(f"Количество элементов: {count}")
print(f"Среднее арифметическое элементов: {average:}")
print(f"Новая последовательность: {new_sequence}")