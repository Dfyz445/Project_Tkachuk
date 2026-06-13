#В последовательности на n целых элементов найти произведение элементов средней трети.

def product_middle(sequence):
    n = len(sequence)
    if n == 0:
        return 0

    part_size = n // 3
    if n % 3 != 0:
        part_size = (n + 2) // 3

    start = (n - part_size) // 2
    end = start + part_size

    middle_part = sequence[start:end]
    product = 1
    for num in middle_part:
        product *= num

    return product

if __name__ == "__main__":
    seq1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    res1 = product_middle(seq1)
    print(f"Последовательность: {seq1}")
    print(f"Произведение средней трети: {res1}")

    seq2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    res2 = product_middle(seq2)
    print(f"Последовательность: {seq2}")
    print(f"Произведение средней трети: {res2}")