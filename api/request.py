import json
from isbnlib import info
from isbnlib import meta
from isbnlib.registry import bibformatters
from google_trans_new import google_translator

def request(isbn):
    try:
        translator = google_translator()
        language = info(isbn) # Isso contém o país 
        bibtex = bibformatters["json"]
        metadata = json.loads(bibtex(meta(isbn)))
        metadata['language'] = language
        metadata['type'] = translator.translate(metadata['type'], lang_tgt='pt')
        metadata['language'] = translator.translate(metadata['language'], lang_tgt='pt')
        authors = list()
        for author in metadata['author']:
            authors.append(author['name'])
        metadata['author'] = str(authors)
        metadata['identifier'] = int(metadata['identifier'][0]['id'])

        return metadata

    except:
        return 'Não foi possível encontrar o isbn fornecido'