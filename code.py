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
            shifted_char = (alphabet.index(i) + shift) % len(alphabet)
            coded_txt += alphabet[shifted_char]
        else:
            coded_txt += i
    return coded_txt
def caesar_decoder(text: str, shift: int, alphabet: str) -> str:
    """
    Funtion for decoding text
    :param text: text to decoding
    :param shift: alphabet shift
    :param alphabet: rus alphabet
    :return: decoded text
    """
    decoded_txt = ""
    for i in text:
        if i in alphabet:
            shifted_char = (alphabet.index(i) - shift) % len(alphabet)
            decoded_txt += alphabet[shifted_char]
        else:
            decoded_txt += i
    return decoded_txt
