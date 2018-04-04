import json
import argparse


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as source_file:
        source_data = source_file.read()
        return source_data


def get_json_content(data_to_parse):
    parsed_data = json.loads(data_to_parse)
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


def keyboard_input(input_value):
    example_data = 'longitude=37.621587946152012 latitude=55.765366956608361'
    value_error_message = ('Entering value is incorrect! '
                           'The correct format is float: {}').format(example_data)
    if input_value is 'longitude':
        print('To find the nearest bar for you, you have to enter your coordinates.\n'
              'Please enter your longitude:')
        while True:
            try:
                longitude = float(input())
                return longitude
            except ValueError:
                print(value_error_message)
                print('Please enter your longitude:')
                continue
    elif input_value is 'latitude':
        print('Please enter your latitude:')
        while True:
            try:
                longitude = float(input())
                return longitude
            except ValueError:
                print(value_error_message)
                print('Please enter your latitude:')
                continue


def print_content(required, longitude=0.0, latitude=0.0):
    if required is 'biggest':
        print('The largest bar - ', get_bar_by_size(json_content, 'biggest'))
    elif required is 'smallest':
        print('The smallest bar - ', get_bar_by_size(json_content, 'smallest'))
    elif required is 'closest':
        print('The nearest bar - ', get_closest_bar(json_content, longitude, latitude))


def get_args():
    script_usage = 'python bars.py  <path to file>'
    parser = argparse.ArgumentParser(
        description="How to run bars.py:",
        usage=script_usage
    )
    parser.add_argument(
        "source_data",
        help="Specify the path to the source data file"
    )
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    example_data = 'longitude=37.621587946152012 latitude=55.765366956608361'
    args = get_args()
    try:
        file_to_load = load_data(args.source_data)
    except IOError:
        exit("No such file or directory {}".format(args.source_data))
    try:
        json_content = get_json_content(file_to_load)
    except ValueError:
        exit('The source-file is not a valid JSON or empty! Check the file content!')
    longitude = keyboard_input('longitude')
    latitude = keyboard_input('latitude')
    for required_content in ['biggest', 'smallest', 'closest']:
        print_content(required_content, longitude, latitude)
