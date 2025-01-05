"""
Retrieve and print words from a URL.

Usage:
    python3 words.py <URL>
"""

import sys
from urllib.request import urlopen


def fetch_words(url):
    """Fetch a list of words from a URL.

        :param url: The URL of a UTF-8 text document.
        :return: A list of strings containing the world from the document.
    """
    story_words = []

    story = urlopen(url)
    for line in story:
        line_words = line.decode('utf8').split()
        for word in line_words:
            story_words.append(word)
    story.close()

    return story_words


def print_items(items):
    """Print items one per line.

        Args:
            An iterable series of printable items.
    """
    for item in items:
        print(item)


def main(url):
    """Print each word from a text document from at a URL.

    :param url: The URL of a UTF-8 text document.
    :return: None.
    """
    words = fetch_words(url)
    print_items(words)


# csak akkor fut le ez a metódus, ha ez van main-ként (programként) futtatva.
if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main('http://sixty-north.com/c/t.txt')
