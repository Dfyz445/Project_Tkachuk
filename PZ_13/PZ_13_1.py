"""
Из исходного текстового файла (expansion.txt) выбрать имена файлов,
соответствующие типам: .xls, .xml, .html, .css, .py.
Посчитать количество полученных элементов.
"""
file = open("expansion.txt", "r")
content = file.read()
file.close()

extensions = [".xls", ".xml", ".html", ".css", ".py"]
words = content.split()
found_files = []

for word in words:
    clean_word = word.strip(",.;:!?\"'()[]{}")

    for ext in extensions:
        if clean_word.endswith(ext):
            found_files.append(clean_word)
            break

print("Найденные файлы:")
for file_name in found_files:
    print(file_name)

print(f"Количество найденных элементов: {len(found_files)}")