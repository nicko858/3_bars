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
- ```get_bar_by_size()``` - accepts the file content  from the  ```load_data()``` function and returns the biggest bar, or the smallest bar, depending on the function arguments
- ```get_closest_bar()```- function accepts the file content  from the  ```load_data()``` function and returns the closest bar (using gps-coordinates entering by user)
- ```keyboard_input()```-  function accepts the user keyboard input
- ```print_content()``` - prints the biggest ,smallest and closest bar depending on the function arguments
The program uses these libs from Python Standart Library:

```python
json
sys
re
sys
```

How in works:
- The program reads  the first command-line argument(path to json-file)
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
The largest bar -  Спорт бар «Красная машина»
The smallest bar -  Фреш-бар
The nearest bar -  Юнион Джек
```

The program check command-line arguments and if it is wrong,  you will see the warning message ```Incorrect line argument!``` and usage-message.

If the content of source-file is not in JSON-format,  you will see the following warning messages:
```Decoding JSON has failed!```
```The source-file is not a valid JSON! Check the file content!```
Else if the entering data is incorrect(equal or less null), you will see the following:

```Entering data is incorrect! The correct format is: longitude=37.621587946152012 latitude=55.765366956608361```

In the cases above, the program will not run.


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
