#Генератор (yield), который преобразует все буквенные символы в строчные.
from typing import Iterator, Union

text_data = ["Hello", "WoRlD", "123", "Python", "GeNeRaToR"]
text_line = "ПРИВЕТ Мир! 2024"

def lowercase_letters_generator(items: Iterator[Union[str, any]]) -> Iterator[str]:
    """
    Генератор, который принимает итератор и преобразует все буквенные символы
    в каждом элементе в строчные. Небуквенные символы остаются без изменений.
    """
    for item in items:
        s = str(item)
        transformed = ''.join(
            ch.lower() if ch.isalpha() else ch
            for ch in s
        )
        yield transformed

print("Исходные данные:", text_data)
gen = lowercase_letters_generator(text_data)
result_list = list(gen)

print("Результат (все буквы в нижнем регистре):", result_list)
print("Исходная строка:", text_line)
gen_from_str = lowercase_letters_generator([text_line])  # оборачиваем в список
print("Результат:", next(gen_from_str))