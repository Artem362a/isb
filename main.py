from task1.code import *
from fileinput import *
from task2.freq_analysis import *
from task2.decoder import *


def part2():
    """
    This function realise second part of task
    :return: None
    """
    try:
        config = json_file_open("Task2config.json")
        text = file_open(config["coded_text2"])
        ru_freq = json_file_open(config["ru_freq"])
        text_freq = freq_analysis(text)
        json_file_save(config["text_freq"], text_freq)
        key2 = keygen(text_freq, ru_freq)
        json_file_save(config["key2"], key2)

        norm_text = decoder(text, key2)
        file_save(config["decoded_text"], norm_text)
    except Exception as e:
        print(f"Ошибка в part2: {e}")


def main():
    """
    This function realise first part of task
    :return: None
    """
    try:
        config = json_file_open("config.json")
        text = file_open(config["input_text"])
        key = json_file_open(config["key"])

        coded_text = caesar(text, key["shift"], config["alphabet"])
        file_save(config["coded_text"], coded_text)

    except Exception as e:
        print(f"Ошибка в main: {e}")
    part2()
    return 0


if __name__ == "__main__":
    main()
