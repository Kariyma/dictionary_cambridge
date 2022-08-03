"""The main module of the script for the search for voicing \
and translation of English words."""
import argparse
import logging
from os import path

from data import config
from word.word import Word


def save_file(file_name, word, lng):
    """Save voicing to file.

    Arguments:
        file_name: file name
        word: word for saving
        lng: pronounce
    """
    filename = path.join(config.OUT_PATH, '{0}_{1}.mp3'.format(word, lng))
    with open(filename, 'wb') as output_file:
        output_file.write(file_name)
    message = 'Произношение слова {0} c акцентом {1} загружено в файл {2}'
    logging.info(message.format(word, lng.upper(), filename))


def check_pronunciation(word: Word, lng: str) -> bool:
    """Check pronunciation is existing.

    Arguments:
        word: word
        lng: pronunciation

    Returns:
        bool: result of check
    """
    if not word.found:
        return False
    lng_dict = word.pronunciations.get(lng, None)
    if not lng_dict:
        logging.error('Произношение {0} не поддерживается.'.format(lng))
        return False
    if not lng_dict.get('tran', None):
        logging.error(
            'Произношение {0} для слова {1} не найдено.'.format(
                lng, word.word['en'],
            ),
        )
        return False
    return True


def main(find: str, lng: str, more: bool) -> bool:
    """Find word and get its voicing.

    Arguments:
        find: Word to search
        lng: Pronunciation
        more: Flag if need description about word

    Returns:
        bool: result
    """
    word = Word(find, more)

    if not check_pronunciation(word, lng):
        return False

    for key in word.pronunciations.keys():
        if not lng or key == lng:
            logging.info('{0}'.format(word.pronunciations[key]['tran']))
            save_file(
                word.pronunciations[key]['file_content'],
                word.word['en'],
                key,
                    )

    if more:
        for description in word.description:
            logging.info(description['en'])
            logging.info(description['ru'])

    logging.info(word.word['ru'])

    return True


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser()
    parser.add_argument('word', type=str, help='Слово для озвучивания')
    parser.add_argument(
        '-p',
        '--pronounce',
        type=str,
        help='Акцент озвучивания, по умолчанию Бритаский (uk)',
        choices=['uk', 'us'],
        default=config.DEFAULT_PRONUNCIATION,
    )
    parser.add_argument(
        '-m',
        '--more',
        help='Выводить ли значения',
        action='store_true',
    )
    arguments = parser.parse_args()
    main(arguments.word, arguments.pronounce, arguments.more)
