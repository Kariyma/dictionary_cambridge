from os import path
import argparse

from data import config
from word.word import Word


def save_file(file, word, lng):
    filename = path.join(config.OUT_PATH, f'{word}_{lng}.mp3')
    with open(filename, 'wb') as f:
        f.write(file)
    print(f"Произношение слова {word} c акцентом {lng.upper()} "
          f"загружено в файл {filename}")


def main(find: str, lng: str, more: bool):
    word = Word(find, more)
    if not word.found:
        return False
    lng_dict = word.pronunciations.get(lng, None)
    if lng_dict:
        if not lng_dict.get('tran', None):
            print(f"Произношение {lng} для слова {find} не найдено.")
            return False
    else:
        print(f"Произношение {lng} не поддерживается.")
        return False
    for key in word.pronunciations.keys():
        print_it = True if not lng or key == lng else False
        if print_it:
            print(f"/{word.pronunciations[key]['tran']}/")
            save_file(word.pronunciations[key]['file_content'],
                      word.word['en'], key)
    if more:
        for description in word.description:
            print(description['en'])
            input("continue...")
            print(description['ru'])
            input("continue...")
    print(word.word['ru'])
    return True


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('word', type=str, help="Слово для озвучивания")
    parser.add_argument(
        '-p', '--pronounce', type=str,
        help="Акцент озвучивания, по умолчанию Бритаский (uk)",
        choices=['uk', 'us'], default=config.DEFAULT_PRONUNCIATION)
    parser.add_argument('-m', '--more', help="Выводить ли значения",
                        action='store_true')
    arguments = parser.parse_args()
    main(arguments.word, arguments.pronounce, arguments.more)
