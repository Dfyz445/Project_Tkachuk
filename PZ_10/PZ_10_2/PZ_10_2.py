"""
Из предложенного текстового файла (text18-18.txt) вывести на экран его содержимое,
количество знаков пунктуации в первых четырёх строках. Сформировать новый файл,
в который поместить текст в стихотворной форме выведя строки в обратном порядке.
"""
import string

with open('text18-18.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

print("Содержимое файла:")
print("".join(lines))
print("")

punctuation_count = 0
for i in range(min(4, len(lines))):
    for char in lines[i]:
        if char in string.punctuation:
            punctuation_count += 1

print("Количество знаков пунктуации в первых 4 строках:", punctuation_count)

with open('result_poem.txt', 'w', encoding='utf-8') as file:
    for line in reversed(lines):
        file.write(line)

print("Новый файл 'result_poem.txt' создан со строками в обратном порядке")