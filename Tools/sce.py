from datetime import datetime
import json
import os.path

import click
import markdown

from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

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


@click.group()
@click.option('--debug/--no-debug', default=False)
def cli(debug):
    if debug:
        click.echo('Debug mode is on')


def get_synsets(word, pos=None):
    ss = None
    if pos is None:
        ss = wordnet.synsets(word)
    else:
        if pos == 'n':
            ss = wordnet.synsets(word, pos=wordnet.NOUN)
        elif pos == 'v':
            ss = wordnet.synsets(word, pos=wordnet.VERB)
        # TODO: Add other possible POS values from WordNet
        else:
            raise ValueError("Unknown part of speech (so far)")
    return ss


@click.command()
@click.option('--pos', '-p', default=None, help='Part of speech')
@click.argument('word')
def lookup(word, pos=None):
    """
    Lookup meanings in WordNet
    """
    ss = get_synsets(word, pos=pos)

    if return_data:
        return ss

    print("%s (%s)" % (word, pos))

    for item in ss:
        print("%s: %s" % (item, item.definition()))


@click.command()
@click.option('--pos', '-p', default=None, help='Part of speech')
@click.option('--vocabulary', '-v', default='general',
              help='Vocabulary file to add to')
@click.argument('word')
def add(word, pos, vocabulary):
    """
    Add a word to a vocabulary file
    """
    # Build a menu and show it
    choices = get_synsets(word, pos=pos)
    choice_keys = {}
    choice_i = 0
    for choice in choices:
        choice_i += 1
        choice_keys[choice_i] = choice
        click.echo("[%d]\t%s: %s" %
                   (choice_i,
                    choice.name(),
                    choice.definition()))

    # TODO: Handle case where there are 0 choices

    # Get user's choice
    user_input = click.prompt('Select a definition', type=int)
    the_one = choice_keys[user_input]

    # Get POS from user choice

    # Build our new vocabulary item data structure
    new_item = {
        'word': word,
        'pos': the_one.pos(),
        'WordNet': the_one.name(),
        'notes': "Added via sce.py at %s" % (datetime.utcnow())
    }
    click.echo("New item:\t%s" % json.dumps(new_item))

    # Get existing JSON file
    if vocabulary.endswith('.json'):
        filename = vocabulary
    else:
        filename = vocabulary + '.json'

    # Check if file exists, and read it if it does
    if os.path.isfile(filename):
        f = open(filename, 'rb')
        j = json.load(f)
        f.close()
        click.echo("Existing vocabulary:\t%s" % j)
    else:
        j = []
        click.echo("Vocabulary didn't exist.")

    # Write vocabulary file
    j.append(new_item)
    f = open(filename, 'wb')
    json.dump(j, f, indent=2)
    f.close()
    click.echo("Wrote vocabulary file: %s" % filename)


@click.command()
@click.option('--vocabulary', '-v', default='general',
              help='Vocabulary file to render')
@click.option('--format', '-f', default='html',
              type=click.Choice(['html', 'markdown']),
              help='Output format')
def render(vocabulary, format):
    """
    Render a vocabulary file to Markdown or HTML
    """
    # Check if file exists, and read it if it does
    if os.path.isfile(vocabulary):
        f = open(vocabulary, 'rb')
        j = json.load(f)
        f.close()
        # click.echo("Vocabulary:\t%s" % j)
    else:
        click.echo("Vocabulary file didn't exist.")
        return

    # Build Markdown text
    md = ""
    for item in j:
        # click.echo(item)
        ss = wordnet.synset(item['WordNet'])
        md += "* **%s** (%s): %s (`%s`)\n" % (
            item['word'],
            item['pos'],
            ss.definition(),
            item['WordNet'])

    # Write output
    if format == 'markdown':
        click.echo(md)
    elif format == 'html':
        html = markdown.markdown(md)
        click.echo(html)
    else:
        raise Exception("Invalid format: %s" % (format))


cli.add_command(lookup)
cli.add_command(stem)
cli.add_command(add)
cli.add_command(render)

if __name__ == '__main__':
    cli()
