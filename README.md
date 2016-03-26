# simplified-contract-english

Simplified Contract English (SCE) is a proposed [controlled natural language](https://en.wikipedia.org/wiki/Controlled_natural_language) for writing contracts. It is inspired by [Simplified Technical English](https://en.wikipedia.org/wiki/Simplified_Technical_English) and similar efforts.

## Overview

Simplified Contract English has two main parts:

1. Rules
2. Vocabularies

## Rules
TBD

## Vocabularies

Every word in an SCE document should come from an approved list of words, called a **vocabulary**. SCE provides a base vocabulary. Additional vocabularies can be added, depending on the document's subject. For example, company formation documents could use both the SCE base vocabulary and an additional corporate law vocabulary.

In SCE, words are approved for **one meaning only**. For example, the SCE's base vocabulary approves `contract` as a noun meaning "a binding agreement between two or more persons that is enforceable by law". The word `contract` cannot be used as a verb in SCE.

Vocabularies are specified in JSON. For each approved word, the approved part of speech and approved meaning are specified. The approved meaning is linked to [WordNet](http://wordnet.princeton.edu/).

As an example, again using `contract`:

```json
"contract": {
    "pos": "n",
    "WordNet": "contract.n.01"
}
```

`contract.n.01` is WordNet's identifier for the approved meaning.
