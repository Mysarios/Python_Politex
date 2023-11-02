import math
def count_letters(text):
    count_symbols = {}
    for symbol in text:
            if symbol.isalpha():
                if symbol.lower() not in count_symbols:
                    count_symbols[symbol.lower()] = 0
                else:
                    count_symbols[symbol.lower()] += 1


    return count_symbols

def calculate_frequency(symbols_dictunary):
    count_symbols = 0
    for key in symbols_dictunary:
        count_symbols += symbols_dictunary[key]

    frequency_symbols = {}
    for key in symbols_dictunary:
        frequency_symbols[key] = symbols_dictunary[key] / count_symbols

    return frequency_symbols


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

result_dict = calculate_frequency(count_letters(main_str))

check = 0
for key in result_dict:
    print(key+": {:.2f}".format(result_dict[key]))
    check += result_dict[key]
# проверка на сумму частот
#print("\nSym =       ", check)