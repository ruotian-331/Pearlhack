import anvil.server
anvil.server.connect("K7XKRLX7OOYMPWGVQ6ENWSBR-56CWRXFDWIEOE5Q6")
@anvil.server.callable
def newspull(user_input):
    import datanews
    global articles
    articles = []
    datanews.api_key = '0cdrnpo4us2ywq4gjg964dgj2'
    response = datanews.news(q = user_input, language=['en'], sortBy='date')

    for i in range(10):
        articles.append(response['hits'][i]['description'])

    numarticles = [1/len(articles)]
    return articles + numarticles

anvil.server.wait_forever()