"""The module of the class for word to searching for voicing \
and translation of English words."""
import logging
from enum import Enum

import requests
from bs4 import BeautifulSoup
from googletrans import Translator

from data import config

SOURCE = 'file'


class Language(Enum):
    """Enumeration for used languages."""

    english = 'en'
    russian = 'ru'


def translate(string: str) -> str:
    """Translate form Russian to English.

    Arguments:
        string: string to translate

    Returns:
        str: translation
    """
    translator = Translator()
    return translator.translate(
        string, src=Language.english.value, dest=Language.russian.value,
    ).text


class Word(object):
    """Класс для получения информации по слову."""

    root_url = '{0}{1}'.format(config.HOST, config.URL_ROOT)
    headers = config.HEADERS
    pronunciations = {
        'uk': {
            'tran': None,
            'file': None,
            'file_content': None,
        },
        'us': {
            'tran': None,
            'file': None,
            'file_content': None,
        },
    }
    error = None
    word = {
        Language.english.value: '',
        Language.russian.value: '',
    }

    def __init__(self, word: str, more: bool = False):
        """Class for get voicing and pronunciation form word.

        Arguments:
            word: word to search
            more: flag to get or not description
        """
        self.word[Language.english.value] = word
        self.word[Language.russian.value] = translate(
            str(self.word[Language.english.value]),
        )
        self.more = more
        self.found = False
        self.description = []
        self.set_data()

    def get_content(self) -> str:
        """Get content from url.

        Returns:
            str: response
        """
        session = requests.Session()
        url = '{0}{1}'.format(
            self.root_url,
            self.word[Language.english.value],
        )

        try:
            response = session.get(url=url, headers=self.headers)
        except OSError as err:
            logging.error(err)
            return ''

        response.raise_for_status()
        self.found = True
        if response.url != url:
            logging.error('Word not found.')
            return ''

        return response.text

    def get_file(self, lang: str) -> bytes:
        """Get file with voicing from url.

        Arguments:
            lang: pronunciation to get

        Returns:
            bytes: file content
        """
        session = requests.Session()
        url = '{0}{1}'.format(config.HOST, self.pronunciations[lang][SOURCE])

        try:
            response = session.get(url=url, headers=self.headers)
        except OSError as err:
            logging.error(err)
            return bytes(0)

        response.raise_for_status()
        if response.url != url:
            logging.error('Word not found.')
            return bytes(0)

        return response.content

    def set_pronunciations_dict(self, soup: BeautifulSoup):
        """Set data to pronunciations dictionary.

        Arguments:
            soup: object of class BeautifulSoup
        """
        for tag in self.pronunciations.keys():
            if not soup.select('span.{0}'.format(tag)):
                continue
            tran = soup.select(
                'span.{0}.dpron-i > span.pron.dpron > span'.format(tag),
                )
            self.pronunciations[tag]['tran'] = tran[0].text if tran else None
            audio_tag = soup.select(
                'span.{0} amp-audio > source:nth-child(2)'.format(tag),
            )
            if audio_tag:
                self.pronunciations[tag][SOURCE] = audio_tag[0].attrs['src']
            self.pronunciations[tag]['file_content'] = self.get_file(tag)

    def set_data(self) -> bool:
        """Set data to object Word.

        Returns:
            bool: result
        """
        data_content = self.get_content()

        if not self.found:
            return False

        soup = BeautifulSoup(data_content, 'lxml')

        self.set_pronunciations_dict(soup)

        if self.more:
            descriptions = soup.select('#page-content div.ddef_h > div')
            self.description = [
                {
                    Language.english.value: description.text,
                    Language.russian.value: translate(description.text),
                } for description in descriptions
            ]
