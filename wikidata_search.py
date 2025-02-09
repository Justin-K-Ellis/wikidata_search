#!/usr/bin/env python3
import csv
import requests
import sys

useage = """
Usage: include either a single term or the filename of a .csv file to search with the 
Wikipedia API. I.e.:

python wikidata_search.py <string>
or
python wikidata_search.py <filename.csv>

Examples:

python wikidata_search.py cats
python wikidata_search.py dogs.csv
"""

def main():
    try:
        arg = sys.argv[1]
        if arg[-4:] == ".csv":
            filename = arg
            check_csv(filename)
        else:
            has_hit, first_url = search_wikidata(arg)
            check_hits(has_hit, first_url, arg)
    except IndexError:
        print(useage)
        sys.exit()
    except KeyboardInterrupt:
        print("\nProgram ended.")
        sys.exit()


def check_csv(filename):
    with open(filename) as file:
                reader = csv.reader(file)
                for row in reader:
                    keyword = row[0]
                    has_hit, first_url = search_wikidata(keyword)
                    check_hits(has_hit, first_url, keyword)


def check_hits(has_hit, first_url, keyword):
    if has_hit:
        print(f"Keyword: '{keyword}' - Hit: {first_url}")
    else:
        print(f"Keyword: '{keyword}' - No hit")


def search_wikidata(keyword):
    """
    Search for a keyword on Wikidata using the wbsearchentities API.

    Args:
        keyword (str): The search term.

    Returns:
        tuple: (bool, str or None)
               bool = True if any results were found, False otherwise.
               str  = URL of the first matching entity if found, else None.
    """
    url = "https://www.wikidata.org/w/api.php"
    params = {
        "action": "wbsearchentities",
        "search": keyword,
        "language": "en",
        "format": "json"
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()
    except Exception as e:
        print(f"Error searching for '{keyword}': {e}")
        return False, None

    # Grab the search results
    results = data.get("search")

    # If there are results, return True and the first concept URI
    if results:
        # 'concepturi' gives the direct link to the Wikidata entity
        first_uri = results[0].get("concepturi", None)
        return True, first_uri

    # Otherwise, return False with no URL
    return False, None


if __name__ == "__main__":
    main()
