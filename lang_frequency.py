import argparse


def load_data(filepath):
    with open(filepath) as f:
        text = f.read()
    return text


def get_most_frequent_words(text):
    freq_dict = dict()
    for key in text:
        if key in freq_dict:
            freq_dict[key] += 1
        else:
            freq_dict[key] = 1
    freq_dict = sorted(freq_dict.items(), key=lambda kv: -kv[1])
    return freq_dict[:10]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Prints top 10 symbols with frequencies from text file.')
    parser.add_argument('filepath', metavar='f', type=str,
                        help='path to text file')
    args = parser.parse_args()
    text_loaded = load_data(args.filepath)
    freq_dict = get_most_frequent_words(text_loaded)
    print("\n".join(["'{0}': {1}".format(x[0], x[1]) for x in freq_dict]))
