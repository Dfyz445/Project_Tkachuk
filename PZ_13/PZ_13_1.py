"""
Из исходного текстового файла (expansion.txt) выбрать имена файлов,
соответствующие типам: .xls, .xml, .html, .css, .py.
Посчитать количество полученных элементов.
"""
import re
from pathlib import Path

def count_files_by_extensions(text: str, extensions: list) -> int:
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
    return len(matches)

def main():
    input_file = Path("expansion.txt")

    with open(input_file) as f:
        content = f.read()
    extensions = ['.xls', '.xml', '.html', '.css', '.py']

    count = count_files_by_extensions(content, extensions)
    print(f"Количество найденных файлов с расширениями {', '.join(extensions)}: = {count}")

if __name__ == "__main__":
    main()