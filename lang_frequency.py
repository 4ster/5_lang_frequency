import argparse
from collections import Counter


def load_data(filepath):
    with open(filepath) as textfile:
        text = textfile.read()
    return text


def get_most_frequent_words(text, top_count):
    symbols_counter = Counter(text)
    return symbols_counter.most_common(top_count)


def create_parser(top_count):
    parser = argparse.ArgumentParser(
        description="Prints top {0} symbols with it's frequencies from text file.".format(top_count))
    parser.add_argument(
        "filepath",
        metavar="f",
        type=str,
        help="path to text file"
    )
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    top_count = 10
    args = create_parser(top_count)
    text_loaded = load_data(args.filepath)
    most_frequent_symbols = get_most_frequent_words(text_loaded, top_count)
    print("\n".join(["'{0}': {1}".format(x[0], x[1])
                     for x in most_frequent_symbols]))
