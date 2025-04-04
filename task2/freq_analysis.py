def freq_analysis(text: str) -> dict:
    """
    This function complete frequency analysis
    :param text: text to analysis
    :return: frequency of letters in text
    """
    text = text.upper()
    frequency = {}
    for i in text:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1
    rate = {}
    for i in frequency:
        rate[i] = frequency[i] / len(text)

    return rate
