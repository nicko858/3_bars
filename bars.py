import json
import sys


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as source_file:
        source_data = source_file.read()
    try:
        parsed_data = json.loads(source_data)
        return parsed_data
    except ValueError:
        return None


def get_bar_by_size(data, size):
    bar_size_dict = {}
    for x in data['features']:
        bar_name = x['properties']['Attributes']['Name']
        bar_seats_count = x['properties']['Attributes']['SeatsCount']
        bar_size_dict[bar_name] = bar_seats_count
    if size == 'biggest':
        return max(bar_size_dict, key=lambda SeatsCount: bar_size_dict[SeatsCount])
    elif size == 'smallest':
        return min(bar_size_dict, key=lambda SeatsCount: bar_size_dict[SeatsCount])


def get_closest_bar(data, longitude, latitude):
    bar_coords_dict = {}
    length_to_bar_dict = {}
    for x in data['features']:
        bar_name = x['properties']['Attributes']['Name']
        bar_coords = x['geometry']['coordinates']
        bar_coords_dict[bar_name] = bar_coords
        bar_longitude = bar_coords_dict[bar_name][0]
        bar_latitude = bar_coords_dict[bar_name][1]
        length_to_bar = (longitude - bar_longitude) ** 2 + (latitude - bar_latitude) ** 2
        length_to_bar_dict[bar_name] = length_to_bar
    return min(length_to_bar_dict, key=lambda length_to_bar: length_to_bar_dict[length_to_bar])


def check_is_or_less_null(variable):
    if variable <= 0:
        return True
    else:
        return False


if __name__ == '__main__':
    script_usage = 'python bars.py  <path to file>'
    example_data = 'longitude=37.621587946152012 latitude=55.765366956608361'
    if len(sys.argv) != 2:
        exit('Incorrect line argument!''\n' 'Using: %s' % script_usage)
    try:
        print('To find the nearest bar for you, you have to enter your coordinates.')
        print('Please enter your longitude:')
        longitude = float(input())
        if check_is_or_less_null(longitude):
            print('Check the type of entering data! The {} is equal or less null! '.format(longitude))
            raise ValueError
        else:
            print('Your longitude is {} '.format(longitude))
            print('Please enter your latitude:')
        latitude = float(input())
        if check_is_or_less_null(latitude):
            print('Check the type of entering data! The {} is equal or less null! '.format(latitude))
            raise ValueError
        else:
            print('Your latitude is {}'.format(latitude))
            try:
                json_content = load_data(sys.argv[1])
                print('The largest bar - ', get_bar_by_size(json_content, 'biggest'))
                print('The smallest bar - ', get_bar_by_size(json_content, 'smallest'))
                print('The nearest bar - ', get_closest_bar(json_content, longitude, latitude))
            except ValueError:
                print('Decoding JSON has failed!')
                exit('The source-file is not a valid JSON! Check the file content!')
    except ValueError:
        exit('Entering data is incorrect! The correct format is {}'.format(example_data))
