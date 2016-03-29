from nltk.corpus import wordnet
import click


@click.command()
@click.option('--pos', default=None, help='Part of speech')
@click.argument('word')
def lookup(word, pos=None):
    """
    Lookup meanings in WordNet
    """
    print("%s (%s)" % (word, pos))

    if pos is None:
        ss = wordnet.synsets(word)
    else:
        if pos == 'n':
            ss = wordnet.synsets(word, pos=wordnet.NOUN)
        elif pos == 'v':
            ss = wordnet.synsets(word, pos=wordnet.VERB)

    for item in ss:
        print("%s: %s" % (item, item.definition()))


if __name__ == '__main__':
    lookup()
