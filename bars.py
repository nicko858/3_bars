import json
import argparse


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as source_file:
        source_data = source_file.read()
    try:
        parsed_data = json.loads(source_data)
        return parsed_data
    except ValueError:
        return None


def get_smallest_bar(parsed_data):
    biggest_bar_count = min(bar['properties']['Attributes']['SeatsCount']
                            for bar in parsed_data)
    for bar in parsed_data:
        bar_name = bar['properties']['Attributes']['Name']
        bar_seats_count = bar['properties']['Attributes']['SeatsCount']
        if bar_seats_count == biggest_bar_count:
            return bar_name


def get_biggest_bar(parsed_data):
    biggest_bar_count = max(bar['properties']['Attributes']['SeatsCount']
                            for bar in parsed_data)
    for bar in parsed_data:
        bar_name = bar['properties']['Attributes']['Name']
        bar_seats_count = bar['properties']['Attributes']['SeatsCount']
        if bar_seats_count == biggest_bar_count:
            return bar_name


def get_closest_bar(parsed_data, longitude, latitude):

    def get_length_to_bar(longitude, latitude, bar_longitude, bar_latitude):
        length_to_bar = (longitude - bar_longitude) ** 2 + (latitude - bar_latitude) ** 2
        return length_to_bar
    closest_bar_line = min(
        parsed_data,
        key=lambda bar: get_length_to_bar(
            longitude,
            latitude,
            *bar['geometry']['coordinates']
        )
    )
    return closest_bar_line['properties']['Attributes']['Name']


def print_content(parsed_data, longitude, latitude):
    print('The biggest bar -->', get_biggest_bar(parsed_data))
    print('The smallest bar -->', get_smallest_bar(parsed_data))
    print('The closest bar -->', get_closest_bar(parsed_data, longitude, latitude))


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


if __name__ == '__main__':
    args = get_args()
    example_data = 'longitude=37.621587946152012 latitude=55.765366956608361'
    try:
        json_content = load_data(args.source_data)['features']
        if json_content is None:
            exit('The source-file is not a valid JSON or empty! Check the file content!')
    except IOError:
        exit('No such file or directory {}'.format(args.source_data))
    print('To find the nearest bar for you, enter your coordinates.\n'
          'Please enter your longitude:')
    try:
        longitude = float(input())
        print('Please enter your latitude:')
        latitude = float(input())
    except ValueError:
        exit('Entering value is incorrect! ''The correct format is float: {}'.format(example_data))
    print_content(json_content, longitude, latitude)
