import re


# preprocess and clean sentence
def preprocess_sentence(sentence):
    # remove urls
    sentence = re.sub(r"http\S+", "URL", sentence)

    #remove numbers
    sentence = re.sub('\d{2}\:\d{2}', '', sentence)
    #remove dates
    sentence = re.sub('\d{2}\s(January|February|March|April|May|June|July|August|September|October|Novvember|December)\s\d{4}', '', sentence)
    
    #remove words '(UTC)' and '(talk)'
    sentence = sentence.replace('(UTC)', '')
    sentence = sentence.replace('(talk)', '')

    # #remove names
    # # find all the words that look like names
    # sentence = re.sub( r"(\b[A-Z][a-z]+('s)?\b)",'', sentence)
    
    # find all propperties and replace them
    for prop in re.findall(r'\bP\w+', sentence):
        sentence = sentence.replace(prop, '[PROP]')
    sentence = sentence.replace('[PROP] [PROP]', '[PROP]')
    sentence = sentence.replace('[[[PROP]]]', '[PROP]')

    # find all items and replace them
    for item in re.findall(r'\bQ\w+', sentence):
        sentence = sentence.replace(item, '[ITEM]')
    sentence = sentence.replace('[ITEM] [ITEM]', '[ITEM]')
    sentence = sentence.replace('[[[ITEM]]]', '[ITEM]')

    # find user names and replace them
    for user in re.findall(r'[@]\S*', sentence):
        sentence = sentence.replace(user, '[USER]')
    sentence = sentence.replace('[USER] [USER]', '[USER]')
    sentence = sentence.replace('[[[USER]]]', '[USER]')

    # strip sentence from left and right
    sentence = sentence.strip().lstrip(",.?':$%&/").rstrip("':$%&/")

    # clean other symbols
    sentence = sentence.replace('\n', ' ').replace('-', '').replace('{{', '').replace('}}', '').replace('[[', '').replace(']]', '').replace('URL', '[URL]').replace('* s ', '').replace('*', '') # .replace(':', '')

    # remove multiple spaces
    sentence = re.sub(' +', ' ', sentence).strip()

    # remove parenthesis and texts
    # sentence = re.sub(r"\([^()]*\)", "", sentence)

    # find all code elements and replace them
    sentence = re.sub(r"<code>*[^()]*<\/code>", "[CODE]", sentence)

    # remove user with ping|user
    sentence_words = []
    for word in sentence.split():
        if word.startswith('Q|'):
            sentence_words.append('[ITEM]')
        elif word.startswith('P|'):
            sentence_words.append('[PROP]')
        elif word.startswith('ping|'):
            last_chunk = word.split('|')[-1]
            if last_chunk.startswith('Q|') or last_chunk == ('[ITEM]'):
                sentence_words.append('[ITEM]')
            elif last_chunk.startswith('P') or last_chunk == ('[PROP]'):
                sentence_words.append('[PROP]')
            else:
                sentence_words.append('[USER]')
        else:
            sentence_words.append(word)
    sentence = ' '.join(sentence_words)

    return sentence