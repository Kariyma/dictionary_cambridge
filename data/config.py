from pathlib import Path
from environs import Env


env = Env()
env.read_env(override=True)

ROOT_PATH = str(Path(__file__).parent.parent)
OUT_PATH = env.str('OUT_PATH', ROOT_PATH)
DEFAULT_PRONUNCIATION = env.str('DEFAULT_PRONUNCIATION', 'uk')
#
# Адреса
HOST = 'https://dictionary.cambridge.org/'
URL_ROOT = 'dictionary/english/'
# URL_ROOT = 'dictionary/new/'

# URL_API = 'https://api.nasdaq.com/api/marketmovers?assetclass=stocks'


# Заголовки
HEADERS = {
    "User-Agent": "Mozilla/5.0(WindowsNT10.0;WOW64)AppleWebKit/537.36(KHTML,likeGecko)"
                 "Chrome/88.0.4324.192Safari/537.36OPR/74.0.3911.218(EditionYx)",
    "content-type": "text/html;charset=UTF-8"}

HEADERS_JSON = {
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'origin': 'https://www.nasdaq.com',
    'referer': 'https://www.nasdaq.com/',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}
HEADERS1 = {
        'Connection': 'keep-alive',
        'Content-Encoding': 'gzip',
        'Content-Language': 'en',
        'Content-Type': 'text/html;charset=UTF-8',
        'Date': 'Tue, 15 Mar 2022 12:23:30 GMT',
        'Pragma': 'no-cache',
        'Referrer-Policy': 'strict-origin-when-cross-origin',
        'Server': 'nginx',
        'Set-Cookie': 'loginPopup=8; Expires=Wed, 16-Mar-2022 12:23:30 GMT; Path=/',
        'Strict-Transport-Security': 'max-age=31536000 ; includeSubDomains',
        'Transfer-Encoding': 'chunked',
        'Vary': 'Accept-Encoding',
        'X-Content-Type-Options': 'nosniff',
        'X-XSS-Protection': '1; mode=block',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Host': 'dictionary.cambridge.org',
        'Referer': 'https://dictionary.cambridge.org/dictionary/english/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': 'Windows',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
}
