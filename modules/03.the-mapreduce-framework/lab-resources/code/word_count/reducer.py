import sys


def read_kv_array(text):
    key_values = []

    for line in text:
        key, value = line.split('\t')
        key_values.append({'key': key, 'value': value})

    return key_values


def write_kv_dict(key_values):
    for k, v in key_values.items():
        print(f'{k}\t{v}')


def word_count(words):
    key_values = {}

    for w in words:
        key_values[w['key']] = key_values.get(w['key'], 0) + int(w['value'])

    return key_values


if __name__ == '__main__':
    write_kv_dict(word_count(read_kv_array(sys.stdin)))
