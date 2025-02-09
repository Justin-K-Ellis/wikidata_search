# Wikidata Search

## About

This is a simple program that allows the user to submit either a single term over on the command line or a list of terms in a .csv file and find out if there is a Wikipedia page about that term. This script uses the Wikipedia API, and if the API returns hit, the corresponding URL for the page will be printed to the terminal (if there is more than one hit, the first URL will be printed). If there is no corresponding Wikipedia page, the output will indicate that there is no hit.

## Requirements

- Python 3.13 or later.
- The `requests` module.

## Usage

For a single term, append the term when running the program in the terminal. For multiple terms, use a .csv file. I.e.:

`python wikidata_search.py <string>`
or
`python wikidata_search.py <filename.csv>`

Examples:

- `python wikidata_search.py cats`
- `python wikidata_search.py dogs.csv`
