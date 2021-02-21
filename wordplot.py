import anvil.server
from anvil.tables import app_tables
import anvil.media

anvil.server.connect("K7XKRLX7OOYMPWGVQ6ENWSBR-56CWRXFDWIEOE5Q6")
@anvil.server.callable
def wordplot(articles):
    from wordcloud import WordCloud, STOPWORDS
    comment_words = ''
    stopwords = set(STOPWORDS)
    for val in articles:

        val = str(val)

        tokens = val.split()

        for i in range(len(tokens)):
            tokens[i] = tokens[i].lower()

        comment_words += " ".join(tokens) + " "

    wordcloud = WordCloud(width=800, height=800,
                          background_color='white',
                          stopwords=stopwords,
                          min_font_size=10).generate(comment_words)

    wordcloud.to_file('foo.png')
    newmedia = anvil.media.from_file('foo.png','image/png')
    app_tables.images.add_row(Pics = newmedia)

anvil.server.wait_forever()



