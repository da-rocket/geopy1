"""
This module has two functions: fahr_to_celsius and temp_classifier. Check help <function> to get more information

Author: 
    Vlad Usyukov

License:
    MIT License

    Copyright (c) 2020 Vlad Usyukov

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

"""


def fahr_to_celsius(temp_fahrenheit):
    """Function to convert degrees in Fahrenheit to degrees in Celsius
    Parameters
    ----------
        temp_fahrenheit - <numerical>
    
    Returns
    ----------
        converted_temp - <numerical>
    """
    
    converted_temp = (temp_fahrenheit - 32) / 1.8
    return round(converted_temp, 2)


def temp_classifier(temp_celsius):
    """This function takes temperature in Celsius and classify it into four different classes.
    Parameter:
    ---------
        temp_celsius - <float>
    
    Return:
    ---------
        return temprature classified into 1 of 4 different classes
        0, 1, 2 or 3 - <integer>
    """
    if temp_celsius < -2:
        return 0
    elif temp_celsius >= -2 and temp_celsius < 2:
        return 1
    elif temp_celsius >= 2 and temp_celsius < 15:
        return 2
    else:
        return 3