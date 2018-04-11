import json
import argparse


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as source_file:
        source_data = source_file.read()
        json_content = json.loads(source_data)
        return json_content


def get_smallest_bar(bars):
    bar = min(
        bars,
        key=lambda bar: bar['properties']['Attributes']['SeatsCount']
    )
    return bar


def get_biggest_bar(bars):
    bar = max(
        bars,
        key=lambda bar: bar['properties']['Attributes']['SeatsCount']
    )
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
    print('To find the nearest bar for you, enter your coordinates.\n'
          'Please enter your longitude and latitude,separated by whitespace:')
    cord1, cord2 = input().split(' ')
    longitude, latitude = float(cord1), float(cord2)
    return longitude, latitude

if __name__ == '__main__':
    args = get_args()
    try:
        json_content = load_data(args.source_data)
        longitude, latitude = keyboard_input()
    except FileNotFoundError:
        exit('No such file or directory - {} !'.format(args.source_data))
    except json.JSONDecodeError:
        exit('The source-file is not a valid JSON or empty! Check the file content!')
    except ValueError:
        example_data = 'longitude=37.621587946152012 latitude=55.765366956608361'
        exit('Entering value is incorrect!\n'
             'The correct format is float: {}\n'
             'Enter the correct values,separated by whitespace!'.format(example_data)
             )
    bars = json_content['features']
    biggest_bar = get_biggest_bar(bars)
    smallest_bar = get_smallest_bar(bars)
    closest_bar = get_closest_bar(bars, longitude, latitude)
    print('The biggest bar --> {}'.format(get_bar_name(biggest_bar)))
    print('The smallest bar --> {}'.format(get_bar_name(smallest_bar)))
    print('The closest bar --> {}'.format(get_bar_name(closest_bar)))
