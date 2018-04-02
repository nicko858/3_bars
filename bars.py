import json
import argparse


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as source_file:
        source_data = source_file.read()
        parsed_data = json.loads(source_data)
        return parsed_data


def get_bar_by_size(parsed_data, size):
    bar_size_dict = {}
    for x in parsed_data['features']:
        bar_name = x['properties']['Attributes']['Name']
        bar_seats_count = x['properties']['Attributes']['SeatsCount']
        bar_size_dict[bar_name] = bar_seats_count
    if size == 'biggest':
        return max(bar_size_dict,
                   key=lambda seats_count: bar_size_dict[seats_count])
    elif size == 'smallest':
        return min(bar_size_dict,
                   key=lambda seats_count: bar_size_dict[seats_count])


def get_closest_bar(parsed_data, longitude, latitude):
    bar_coords_dict = {}
    length_to_bar_dict = {}
    for x in parsed_data['features']:
        bar_name = x['properties']['Attributes']['Name']
        bar_coords = x['geometry']['coordinates']
        bar_coords_dict[bar_name] = bar_coords
        bar_longitude = bar_coords_dict[bar_name][0]
        bar_latitude = bar_coords_dict[bar_name][1]
        length_to_bar = (longitude - bar_longitude) ** 2 + (latitude - bar_latitude) ** 2
        length_to_bar_dict[bar_name] = length_to_bar
    return min(length_to_bar_dict,
               key=lambda length_to_bar: length_to_bar_dict[length_to_bar])


def check_is_or_less_null(value_to_check):
    if value_to_check <= 0:
        return True
    else:
        return False


def keyboard_input(input_value):
    if input_value == 'longitude':
        print('To find the nearest bar for you, you have to enter your coordinates.\n'
              'Please enter your longitude:')
        longitude = float(input())
        return longitude
    elif input_value == 'latitude':
        print('Please enter your latitude:')
        latitude = float(input())
        return latitude


def print_content(required, longitude=0.0, latitude=0.0):
    if required == 'biggest':
        print('The largest bar - ', get_bar_by_size(json_content, 'biggest'))
    elif required == 'smallest':
        print('The smallest bar - ', get_bar_by_size(json_content, 'smallest'))
    elif required == 'closest':
        print('The nearest bar - ', get_closest_bar(json_content, longitude, latitude))


def arg_parser_init():
    script_usage = 'python bars.py  <path to file>'
    parser = argparse.ArgumentParser(description="How to run bars.py:", usage=script_usage)
    parser.add_argument("source_data", help="Specify the path to the source data file")
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    example_data = 'longitude=37.621587946152012 latitude=55.765366956608361'
    longitude = keyboard_input('longitude')
    latitude = keyboard_input('latitude')
    for coord in (longitude, latitude):
        if check_is_or_less_null(coord):
            exit('Entering data is incorrect! The correct format is {}\n'
                 'Check the type of entering data! '
                 'The {} is equal or less null! '.format(example_data, coord))
    try:
        json_content = load_data(arg_parser_init().source_data)
    except ValueError:
        exit('Decoding JSON has failed!\n'
             'The source-file is not a valid JSON! Check the file content!')
    for content in ('biggest', 'smallest', 'closest'):
        print_content(content, longitude, latitude)
