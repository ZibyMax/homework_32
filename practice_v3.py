import requests


def translate_it(lang, text):
    """
    YANDEX translation plugin

    docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/

    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]

    :param lang: <str> translation direction, for instance 'ru-en'.
    :param text: <str> text for translation.
    :return: <str> translated text.
    """
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'

    params = {
        'key': key,
        'lang': lang,
        'text': text,
    }
    response = requests.get(url, params=params).json()
    return ' '.join(response.get('text', []))


def translate_file(input_file, output_file, original_lang, target_lang):
    lang = original_lang + '-' + target_lang

    input_file = open(input_file, 'r', encoding='utf8')
    output_file = open(output_file, 'w', encoding='utf8')

    for line in input_file:
        output_file.write(translate_it(lang, line))

    output_file.close()
    input_file.close()


def homework_32():
    initial_data = [
        {
            'input_file': 'DE.txt',
            'original_lang': 'de',
            'target_lang': 'ru',
            'output_file': 'DE-RU.txt'
        }, {
            'input_file': 'ES.txt',
            'original_lang': 'es',
            'target_lang': 'ru',
            'output_file': 'ES-RU.txt'
        }, {
            'input_file': 'FR.txt',
            'original_lang': 'fr',
            'target_lang': 'ru',
            'output_file': 'FR-RU.txt'
        }
    ]

    for data in initial_data:
        translate_file(data['input_file'], data['output_file'], data['original_lang'], data['target_lang'])


homework_32()
