import json
import argparse


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as source_file:
        source_data = source_file.read()
    try:
        bars = json.loads(source_data)
        return bars
    except ValueError:
        return None


def get_smallest_bar(bars):
    bar = min(
        bars,
        key=lambda bar: bar['properties']['Attributes']['SeatsCount']
    )
    return bar


def get_biggest_bar(bars):
    bar = max(bars, key=lambda bar: bar['properties']['Attributes']['SeatsCount'])
    return bar


def get_length_to_bar(longitude, latitude, bar_longitude, bar_latitude):
    length_to_bar = (longitude - bar_longitude) ** 2 + (latitude - bar_latitude) ** 2
    return length_to_bar


def get_closest_bar(bars, longitude, latitude):
    bar = min(
        bars,
        key=lambda bar: get_length_to_bar(
            longitude,
            latitude,
            *bar['geometry']['coordinates']
        )
    )
    return bar


def get_bar_name(bar):
    return bar['properties']['Attributes']['Name']


def get_bar_info(bars, required, longitude=0.0, latitude=0.0):
    if required is 'biggest':
        return get_biggest_bar(bars)
    elif required is 'smallest':
        return get_smallest_bar(bars)
    elif required is 'closest':
        return get_closest_bar(bars, longitude, latitude)


def get_args():
    script_usage = 'python bars.py  <path to file>'
    parser = argparse.ArgumentParser(
        description='How to run bars.py:',
        usage=script_usage
    )
    parser.add_argument(
        'source_data',
        help='Specify the path to the source data file'
    )
    args = parser.parse_args()
    return args


def keyboard_input():
    try:
        output_value = float(input())
        return output_value
    except ValueError:
        return None

if __name__ == '__main__':
    args = get_args()
    example_data = 'longitude=37.621587946152012 latitude=55.765366956608361'
    try:
        bars = load_data(args.source_data)
        if bars is None:
            exit('The source-file is not a valid JSON or empty! Check the file content!')
    except FileNotFoundError:
        exit('No such file or directory {}'.format(args.source_data))
    print('To find the nearest bar for you, enter your coordinates.\n'
          'Please enter your longitude:')
    longitude = keyboard_input()
    print('Please enter your latitude:')
    latitude = keyboard_input()
    if (longitude is None) or (latitude is None):
        exit('Entering value is incorrect!\n'
             'The correct format is float: {}'.format(example_data))
    for required in ['biggest', 'smallest', 'closest']:
        bar = get_bar_info(bars['features'], required, longitude, latitude)
        bar_name = get_bar_name(bar)
        print('The {} bar --> {}'.format(required, bar_name))

