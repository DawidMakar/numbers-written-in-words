from core import dicts


def convert_number_to_words(number):
    if int(number) == 0:
        return dicts.ZERO

    words = []
    number = number.lstrip('0')

    if len(number) % 3 is not 0:
        for i in range(0, 3-len(number) % 3):
            number = '0' + number

    number_as_list = [int(n) for n in number]
    chunks = list(split_list(number_as_list, 3))
    chunk_amount = len(chunks)

    for chunk in chunks:
        if int(''.join(str(i) for i in chunk)) == 1 and chunk_amount is not 1:
            pass
        else:
            if chunk[0] > 0:
                value = dicts.HUNDREDS[chunk[0]]
                words.append(value)
            if chunk[1] > 1:
                value = dicts.TWENTIES[chunk[1]]
                words.append(value)
            if chunk[1] == 1:
                value = dicts.TENS[chunk[2]]
                words.append(value)
            elif chunk[2] > 0:
                value = dicts.ONES[chunk[2]]
                words.append(value)

        chunk_amount -= 1

        if chunk_amount > 0:
            number = int(''.join(str(i) for i in chunk))
            value = dicts.THOUSANDS[chunk_amount][number_form(number)]
            words.append(value)

    result = ' '.join(words)
    return result


def split_list(list_of_digits, size):
    for i in range(0, len(list_of_digits), size):
        yield list_of_digits[i:i + size]


def number_form(number):
    if number == 1:
        return 0
    elif 1 < number % 10 < 5 and number % 100 not in [12, 13, 14]:
        return 1
    else:
        return 2
