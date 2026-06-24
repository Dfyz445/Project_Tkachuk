"""
Из исходного текстового файла (expansion.txt) выбрать имена файлов,
соответствующие типам: .xls, .xml, .html, .css, .py.
Посчитать количество полученных элементов.
"""
import re
from pathlib import Path

def find_files_by_extensions(text: str, extensions: list) -> list:
    escaped_exts = sorted(
        (re.escape(ext) for ext in extensions),
        key = len,
        reverse = True
    )
    pattern = re.compile(
        r'\b[\w.-]+?(?:' + '|'.join(escaped_exts) + r')\b',
        re.IGNORECASE
    )
    matches = pattern.findall(text)
    return matches

input_file = Path("expansion.txt")
try:
    with open(input_file) as f:
        content = f.read()
except FileNotFoundError:
    print(f"Ошибка: Файл {input_file} не найден!")

extensions = ['.xls', '.xml', '.html', '.css', '.py']
found_files = find_files_by_extensions(content, extensions)

print(f"Найдено файлов: {len(found_files)}")
print("Имена найденных файлов:")

if found_files:
    unique_files = list(dict.fromkeys(found_files))

    for i, filename in enumerate(unique_files, 1):
        print(f"  {i}. {filename}")