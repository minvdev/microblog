import requests
from flask_babel import _
from flask import current_app

def translate(text, source_language, dest_language):
    if 'TRANSLATOR_KEY' not in current_app.config or \
        not current_app.config['TRANSLATOR_KEY']:
            return _('Error: the translation service is not configured.')
    url = 'https://translation.googleapis.com/language/translate/v2'
    params = {
        'key': current_app.config['TRANSLATOR_KEY'],
        'q': text,
        'source': source_language,
        'target': dest_language
    }
    r = requests.post(url=url, params=params)
    if r.status_code != 200:
        return _('Error: the translation service failed.')
    return r.json()['data']['translations'][0]['translatedText']
