#Генератор (yield), который преобразует все буквенные символы в строчные.

def yield_generator(iterable):
    for char in iterable:
        if char.isalpha():
            yield char.lower()
        else:
            yield char

if __name__ == "__main__":
    text = "HeLlo WorLd! 123 АБВГД"
    print(f"Исходный текст: {text}")

    result_chars = list(yield_generator(text))
    result_string = ''.join(result_chars)

    print(f"После генератора: {result_string}")
