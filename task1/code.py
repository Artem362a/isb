def caesar(text: str, shift: int, alphabet: str) -> str:
    """
    Function for encoding text
    :param text: text to coding
    :param shift: alphabet shift
    :param alphabet: rus alphabet
    :return: encoded text
    """
    coded_txt = ""
    for i in text:
        if i in alphabet:
            shifted_char = chr(
                (ord(i) - ord(alphabet[0]) + shift) % len(alphabet) + ord(alphabet[0])
            )
            coded_txt += shifted_char
        else:
            coded_txt += i
    return coded_txt
