def keygen(freq_text: dict, freq_ru: dict) -> dict:
    """
    This funcrion generates key
    :param freq_text: Frequency analysis of the text
    :param freq_ru: Frequency analysis of ru alphabet
    :return: key
    """

    sorted_rate_text = sorted(freq_text.items(), key=lambda x: x[1], reverse=True)
    sorted_rate_ru = sorted(freq_ru.items(), key=lambda x: x[1], reverse=True)

    key = {}

    for i, (my_char, _) in enumerate(sorted_rate_text):
        if i < len(sorted_rate_ru):
            russian_char, _ = sorted_rate_ru[i]
            key[my_char] = russian_char
        else:
            key[my_char] = ""

    return key


def decoder(text: str, key: dict) -> str:
    """
    This function decodes the text.
    :param text: encrypted text
    :param key: key
    :return: decoded text
    """
    text = text.upper()
    decoded_text = ""

    for i in text:
        if i in key:
            decoded_text += key[i]
        else:
            decoded_text += i

    return decoded_text
