import logging
from data import config

import requests
from bs4 import BeautifulSoup
from googletrans import Translator


def translate(string):
    translator = Translator()
    return translator.translate(string, src='en', dest='ru').text


class Word:
    """ Класс для получения информации по слову."""
    found = False
    root_url = f"{config.HOST}{config.URL_ROOT}"
    headers = config.HEADERS
    pronunciations = {'uk': {'tran': None,
                             'file': None,
                             'file_content': None},
                     'us': {'tran': None,
                            'file': None,
                            'file_content': None},
                      }
    # description = {'en': None, 'ru': None}
    description = []
    word = {'en': None, 'ru': None}

    def __init__(self, word, more=False):
        self.word['en'] = word
        self.word['ru'] = translate(self.word['en'])
        self.more = more
        self.set_data()

    def get_content(self):
        session = requests.Session()
        url = f"{self.root_url}{self.word['en']}"
        try:
            response = session.get(url=url, headers=self.headers)
            if response.status_code != 200:
                print("Error")
                return False
            if response.url != url:
                print("Word not found.")
                return False
            self.found = True
            return response.text
        except OSError as err:
            logging.error(err)
            return False

    def get_file(self, lang):
        session = requests.Session()
        url = f"{config.HOST}{self.pronunciations[lang]['file']}"
        try:
            response = session.get(url=url, headers=self.headers)
            if response.status_code != 200:
                print("Error")
                return False
            if response.url != url:
                print("Word not found.")
                return False
            return response.content
        except OSError as err:
            logging.error(err)
            return False

    def set_data(self):
        content = self.get_content()
        if self.found:
            soup = BeautifulSoup(content, 'lxml')
            for tag in self.pronunciations.keys():
                tran = soup.select(f"span.{tag}.dpron-i > span.pron.dpron > span")
                self.pronunciations[tag]['tran'] = tran[0].text if tran else None
                file = soup.select(f'span.{tag} amp-audio > source:nth-child(2)')
                self.pronunciations[tag]['file'] = file[0].attrs['src'] if file else None
                self.pronunciations[tag]['file_content'] = self.get_file(tag)
            if self.more:
                descriptions = soup.select('#page-content div.ddef_h > div')
                self.description = [{'en': description.text, 'ru': translate(description.text)}
                                    for description in descriptions]
            # self.word['ru'] = translate(self.word['en'])

# '#page-content > div.page > div:nth-child(1) > div.link > div > div.di-body > div > div > div > div.pos-body > div:nth-child(1) > div.sense-body.dsense_b > div.def-block.ddef_block > div.ddef_h > div'
# selector1 = "#page-content div.ddef_h > div"