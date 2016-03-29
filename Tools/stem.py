# nltk.download('punkt')
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import wordnet
import click

stemmer = PorterStemmer()
# http://www.nltk.org/howto/stem.html


def tokenize(input):
    """
    Tokenize a plain text file.
    Returns a list of tokens.
    """
    tokens = []
    for line in input:
        tokens += word_tokenize(line)
    return tokens


@click.command()
@click.argument('input', type=click.File('rb'))
def stem(input):
    """
    Stem words in a file
    """
    tokens = tokenize(input)
    stemmed = [stemmer.stem(token) for token in tokens]
    synsets = [(word, wordnet.synsets(word)) for word in stemmed]
    for pair in synsets:
        print("%s: %d synsets" % (pair[0], len(pair[1])))
        for synset in pair[1]:
            print("\t%s: %s" % (synset.name(), synset.definition()))


if __name__ == '__main__':
    stem()
