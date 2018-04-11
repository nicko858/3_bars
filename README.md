

# The Closest Bars

The code reads a file with arbitrary data in JSON format and provides the following info:
• the largest bar;
• the smallest bar;
• The closest bar (the current gps coordinates are entered by the user from the keyboard).

# Quickstart

The program is represented by the module ```bars.py```.
Module ```bars.py``` contains the following functions:

- ```load_data()``` - open input file to read
- ```get_json_content() ``` - load file content in json-format
- ```get_args()``` - parses script command-line arguments
- ```get_smallest_bar()``` - accepts the file content  from the  ```load_data()``` function and returns  the smallest bar(by seats count) 
- ```keyboard_input()``` - accepts the user's keyboard-input and returns float value
- ```get_bar_name``` - accepts the bar-string(json-line) and returns the bar name
- ```get_biggest_bar``` accepts the file content  from the  ```load_data()``` function and returns  the biggest bar(by seats count) 
- ```get_closest_bar()```- function accepts the file content  from the  ```load_data()``` function and returns the closest bar (using gps-coordinates entering by user)
- ```get_length_to_bar()``` - function accepts float-values and calculate length between two points

The program uses these libs from Python Standart Library:

```python
json
argparse
```

How in works:
- First, you need to get source data from [this url](https://data.mos.ru) and save it to the source-file
- The program reads  the first command-line argument(path to json source-file)
- loads it using  ```json.loads()``` -function
- suggests user to enter the gps-coordinates
- returns info about the biggest, smallest and closest bars using ```get_bar_by_size()``` , ```get_closest_bar```  functions
and prints content using ```print_content()```-function

Example of script launch on Linux, Python 3.5:

```bash

$ python bars.py <path to file>

```
in the console  output you will see something  like this:
```bash
The largest bar  --> Спорт бар «Красная машина»
The smallest bar  --> Фреш-бар
The closest bar  --> Юнион Джек
```

The program check command-line arguments and if it is wrong,  you will see the warning message ```Incorrect line argument!``` and usage-message.

If the content of source-file is not in JSON-format,  you will see the following warning messages:
```Decoding JSON has failed!```
```The source-file is not a valid JSON! Check the file content!```
Else if the entering data is incorrect(equal or less null), you will see the following:

```Entering data is incorrect! The correct format is``` ```float: longitude=37.621587946152012``` ```latitude=55.765366956608361```
```Enter the correct values,separated by whitespace!```

In the cases above, the program will not run.


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)


