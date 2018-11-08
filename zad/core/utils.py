from core import dicts


def convert_number_to_words(number):
    if number == 0:
        return dicts.ZERO

    words = []
    if number < 0:
        words.append('minus')
        number = str(number)[1:]
    number = str(number)

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
    """
    :param list_of_digits: number converted to list of digits
    :param size: size of a chunk
    :return: digits divided into chunks of selected size
    ex. list of digits=[1, 2, 3, 4, 5, 6, 7, 8, 9], size=3
    result = [1, 2, 3], [4, 5, 6], [7, 8, 9]
    """
    for i in range(0, len(list_of_digits), size):
        yield list_of_digits[i:i + size]


def number_form(number):
    """
    :param number: number as int
    :return: index of correct word form of number from tuple in dict
    ex. when result = 1
    dicts.THOUSANDS[2][result] == 'miliony'
    dicts.THOUSANDS[1][result] == 'tysiące'
    """
    if number == 1:
        return 0
    elif 1 < number % 10 < 5 and number % 100 not in [12, 13, 14]:
        return 1
    else:
        return 2
