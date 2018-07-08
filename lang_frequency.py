import argparse
from collections import Counter
import re


def load_data(filepath):
    with open(filepath) as textfile:
        text = textfile.read()
    return text


def get_most_frequent_words(text, top_count = 10):
    words = re.compile("\\b[^\W\d]+\\b", re.I).findall(text)
    words_counter = Counter(words)
    return words_counter.most_common(top_count)


def create_parser(top_count = 10):
    parser = argparse.ArgumentParser(
        description="Prints top {0} words with it's frequencies from text file.".format(top_count))
    parser.add_argument(
        "filepath",
        metavar="f",
        type=str,
        help="path to text file"
    )
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    top_count = 10
    args = create_parser(top_count)
    text_loaded = load_data(args.filepath)
    most_frequent_words = get_most_frequent_words(text_loaded, top_count)
    print("\n".join(["'{0}': {1}".format(word, count)
                     for word, count in most_frequent_words]))
