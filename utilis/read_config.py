import configparser

parse = configparser.RawConfigParser()
parse.read(r'.\configg\file.ini')


def get_values(tags, keys):
    x = parse.get(tags, keys)
    return x


