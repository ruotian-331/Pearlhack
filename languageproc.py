import anvil.server
anvil.server.connect("K7XKRLX7OOYMPWGVQ6ENWSBR-56CWRXFDWIEOE5Q6")

@anvil.server.callable
def languageProcess(text):
    import spacy
    import nltk
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    import ssl
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context
    nltk.download('vader_lexicon')
    nlp = spacy.load('en_core_web_sm')
    tokenizedA = []
    compiled = ' '.join(text)
    for article in text:
        tokens = []
        doc = nlp(article)
        for token in doc:
            tokens.append(token.text)
        tokenizedA.append(tokens)
    tokCompiled = nlp(compiled)

    items = [x.text for x in tokCompiled.ents]

    # list of finance news specific words
    # New words and values
    new_words = {
        'crushes': 10,
        'great': 5,
        'improvement': 5,
        'beats': 5,
        'misses': -5,
        'sold': -5,
        'mistake': -10,
        'trouble': -10,
        'falls': -10
    }

    vader = SentimentIntensityAnalyzer()
    vader.lexicon.update(new_words)
    scores = []
    for article in text:
        scores.append(vader.polarity_scores(article))
    return scores

anvil.server.wait_forever()