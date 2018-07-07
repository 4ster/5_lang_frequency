import argparse
from collections import Counter

TOP_COUNT = 10

def load_data(filepath):
    with open(filepath) as f:
        text = f.read()
    return text


def get_most_frequent_words(text):
    symbols_counter = Counter(text)

    return symbols_counter.most_common(TOP_COUNT)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Prints top {0} symbols with frequencies from text file.'.format(TOP_COUNT))
    parser.add_argument('filepath', metavar='f', type=str,
                        help='path to text file')
    args = parser.parse_args()
    text_loaded = load_data(args.filepath)
    freq_dict = get_most_frequent_words(text_loaded)
    print("\n".join(["'{0}': {1}".format(x[0], x[1]) for x in freq_dict]))
