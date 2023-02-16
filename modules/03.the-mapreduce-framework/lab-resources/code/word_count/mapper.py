import sys


def write_kv_array(kv_array):
    for kv in kv_array:
        print(f'{kv["key"]}\t{kv["value"]}')


def text_to_words(text):
    key_values = []

    for line in text:
        for word in line.strip().split():
            key_values.append({'key': word, 'value': 1})

    return key_values


if __name__ == '__main__':
    write_kv_array(text_to_words(sys.stdin))
