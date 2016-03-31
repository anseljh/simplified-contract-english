# Simplified Contract English

Simplified Contract English (SCE) is a proposed [controlled natural language](https://en.wikipedia.org/wiki/Controlled_natural_language) for writing contracts. It is inspired by [Simplified Technical English](https://en.wikipedia.org/wiki/Simplified_Technical_English) and similar efforts.

## Overview

Simplified Contract English has two main parts:

1. Rules
2. Vocabularies

## Rules

***TBD***

## Vocabularies

Every word in an SCE document should come from an approved list of words, called a **vocabulary**. SCE provides a base vocabulary. Additional vocabularies can be added, depending on the document's subject. For example, company formation documents could use both the SCE base vocabulary and an additional corporate law vocabulary.

In Simplified Technical English, words are approved for **one meaning only**. For example, the SCE's base vocabulary approves `contract` as a noun meaning "a binding agreement between two or more persons that is enforceable by law". The word `contract` cannot be used as a verb in SCE.

As in STE, exceptions are permissible. For example, proper nouns are an obvious acceptable exception. What is important is that **each exception should be purposeful**. The author should think about whether an exception is really necessary. Tools for writing in SCE should reinforce this concept.

During development, vocabularies are specified in the JSON data format. This data can then be compiled automatically into a human-readable document that looks like this:

> * **compile** (v): use a computer program to translate source code written in a particular programming language into computer-readable machine code that can be executed (`compile.v.03`)
> * **computer** (n): a machine for performing calculations automatically (`computer.n.01`)
> * **program** (n): (computer science) a sequence of instructions that a computer can interpret and execute (`program.n.07`)

(From: [computing.md](Vocabularies/computing.md))

For each approved word, the approved part of speech and approved meaning are specified. The approved meaning is linked to [WordNet](http://wordnet.princeton.edu/).

### Data Example

As an example, again using `contract`:

```json
{
  "word": "contract",
  "pos": "n",
  "WordNet": "contract.n.01"
}
```

`contract.n.01` is WordNet's identifier for the approved meaning, which is `a binding agreement between two or more persons that is enforceable by law`.

## Utility

The [`sce.py`](Tools/sce.py) script is provided for convenience. The script makes it easy to add new words to a vocabulary, create human-readable versions of a vocabulary, and other functions.

General usage:

```text
$ python Tools/sce.py --help
Usage: sce.py [OPTIONS] COMMAND [ARGS]...

Options:
  --debug / --no-debug
  --help                Show this message and exit.

Commands:
  add     Add a word to a vocabulary file
  lookup  Lookup meanings in WordNet
  render  Render a vocabulary file to Markdown or HTML
  stem    Stem words in a file
```

`add` command usage:

```text
$ python Tools/sce.py add --help
Usage: sce.py add [OPTIONS] WORD

  Add a word to a vocabulary file

Options:
  -p, --pos TEXT         Part of speech
  -v, --vocabulary TEXT  Vocabulary file to add to
  --help                 Show this message and exit.```

Example use of the `add` command to add the word "condition" to the general vocabulary:

```text
$ python Tools/sce.py add condition -v Vocabularies/general.json
[1]	condition.n.01: a state at a particular time
[2]	condition.n.02: an assumption on which rests the validity or effect of something else
[3]	condition.n.03: a mode of being or form of existence of a person or thing
[4]	circumstance.n.03: information that should be kept in mind when making a decision
[5]	condition.n.05: the state of (good) health (especially in the phrases `in condition' or `in shape' or `out of condition' or `out of shape')
[6]	condition.n.06: an illness, disease, or other medical problem
[7]	condition.n.07: (usually plural) a statement of what is required as part of an agreement
[8]	condition.n.08: the procedure that is varied in order to estimate a variable's effect by comparison with a control condition
[9]	condition.v.01: establish a conditioned response
[10]	discipline.v.01: develop (children's) behavior by instruction and practice; especially to teach self-control
[11]	stipulate.v.01: specify as a condition or requirement in a contract or agreement; make an express demand or provision in an agreement
[12]	condition.v.04: put into a better state
[13]	condition.v.05: apply conditioner to in order to make smooth and shiny
Select a definition: 7
New item:	{"notes": "Added via sce.py at 2016-03-31 21:46:10.388293", "word": "condition", "pos": "n", "WordNet": "condition.n.07"}
Existing vocabulary:	[{u'word': u'contract', u'pos': u'n', u'WordNet': u'contract.n.01'}, {u'word': u'file', u'pos': u'v', u'WordNet': u'file.v.01'}, {u'word': u'sign', u'pos': u'v', u'WordNet': u'sign.v.01'}, {u'word': u'statute', u'pos': u'n', u'WordNet': u'statute.n.01'}]
Wrote vocabulary file: Vocabularies/general.json
```

## References

### Controlled Natural Languages and Simplified Technical English

* [Wikipedia: Controlled natural language](https://en.wikipedia.org/wiki/Controlled_natural_language)
* [ASD-STE100: ASD Simplified Technical English](http://www.asd-ste100.org/) (informational website and specification)

### Discussion of SCE

* Ken Adams, [Using "Simplified Legal English" for Contracts?](http://www.adamsdrafting.com/using-simplified-legal-english-for-contracts/), March 22, 2016

### Other Standards

* [RFC 2119](http://xml2rfc.ietf.org/public/rfc/html/rfc2119.html): Defines key words for requirements in other Internet standards documents. ("MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL")
