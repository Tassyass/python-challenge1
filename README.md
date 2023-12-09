# python-challenge1

Python Utility Functions
This repository contains three Python functions that perform different tasks:

1. ## Consonant Substrings Calculator
     ## Introduction
The solve function in the consonant_substrings.py script calculates the highest value of consonant substrings in a given lowercase string. Consonants are defined as any alphabet letter except 'aeiou', and each consonant is assigned a value.

Usage
python
Copy code
from consonant_substrings import solve

result = solve("example_string")
print(result)
Example
python
Copy code
print(solve("zodiacs"))    # Output: 26
print(solve("strength"))   # Output: 57

2. ## Count Positive Integers
      ## Introduction
The count_positive_integers function in the count_positive.py script counts the number of positive integers among three given integers and returns True if exactly two of them are positive, and False otherwise.

Usage
python
Copy code
from count_positive import count_positive_integers

result = count_positive_integers(1, -2, 3)
print(result)
Example
python
Copy code
print(count_positive_integers(2, 4, -3))    # Output: True
print(count_positive_integers(-4, 6, 8))    # Output: True
print(count_positive_integers(-14, -3, -4)) # Output: False

3. ## 12-hour Time to 24-hour Time Converter
     ## Introduction
The convert_to_24_hour function in the time_converter.py script converts a 12-hour time (hour, minute, period) to 24-hour time.

usage
python
Copy code
from time_converter import convert_to_24_hour

result = convert_to_24_hour(8, 30, "am")
print(result)
Example
python
Copy code
print(convert_to_24_hour(8, 30, "am"))  # Output: 0830
print(convert_to_24_hour(8, 30, "pm"))  # Output: 2030
print(convert_to_24_hour(12, 0, "pm"))  # Output: 1200

## License
This repository is licensed under the MIT License.

## Author
Tasniim Yasin