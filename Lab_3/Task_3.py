def count_letters(text):
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    count_symbols = {}
    for symbol in alphabet:
        count_symbols[symbol] = 0
    for symbol in text:
        for i in range(0, len(ALPHABET)):
            if symbol == ALPHABET[i]:
                count_symbols[alphabet[i]] += 1
                break
            if symbol == alphabet[i]:
                count_symbols[alphabet[i]] += 1
                break
    return count_symbols


def calculate_frequency(symbols_dictunary):
    count_symbols = 0
    for key in symbols_dictunary:
        count_symbols += symbols_dictunary[key]

    frequency_symbols = {}
    for key in symbols_dictunary:
        frequency_symbols[key] = symbols_dictunary[key] / count_symbols

    return frequency_symbols


text = "Hello world"
result_dict = calculate_frequency(count_letters(text))

check = 0
for key in result_dict:
    print("Symbol ", key, ": ", round(result_dict[key], 2))
    check += result_dict[key]
# проверка на сумму частот
print("\nSym =       ", check)
