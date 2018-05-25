# check
_Fluent assertions for Python_

Bored of using `assert` multiple times to check types, intervals, etc. on data passed as input to your Python functions?
This generates a lot of boilerplate code. __check__ helps you reducing the lines of code providing you a human-friendly and fluent way to make assertions.

Instead of:

```python
def my_function(n, obj):
    assert n is not None
    assert instanceof(n, float)
    assert 0. < n < 1.
    assert obj is not None
    assert isinstance(obj, MyCustomType)
```

just:

```python
from check import Check

def my_function(n, obj):
    Check(n).is_not_None().is_float().is_between(0., 1.)
    Check(obj).is_not_None().is_of_type(MyCustomType)
```


...of course __check__ can also be used as an assertion framework in tests.


## Installation
```shell
pip2 install fluentcheck
```
or 

```shell
python2 setup.py install
```

## Usage
Simply instantiate the `Check` wrapper around the Python object you want to
check out, then fluently append assertions like this:

```python
from check import Check

Check(my_value).assertion1().assertion2().assertion3() # and so on
```

If the order of assertions matters to your overall goal, then take care of it.

What if an assertion fails? A `CheckError` is issued: just catch it! 


## What can I actually check with it?
This is a (non-exhaustive) list of assertions you can make:

```python
# Numbers
is_none()
is_not_none()
is_number()
is_not_number()
is_integer()
is_not_integer()
is_long()
is_not_long()
is_float()
is_not_float()
is_real()
is_not_real()
is_complex()
is_not_complex()
is_positive()
is_negative()
is_zero()
is_at_least(lower)
is_at_most(upper)
is_between(lowerupper)

# Sequences
is_empty()
is_not_empty()
is_iterable()
is_not_iterable()
is_couple()
is_triplet()
is_nuple(dimension)
has_dimensionality(dimensionality)

# Tuples
is_tuple()

# Lists
is_list()

# Strings
is_string()
is_not_string()
contains_numbers()
not_contains_numbers()
contains_numbers_only()
contains_chars()
not_contains_chars()
contains_chars_only()
contains_spaces()
not_contains_spaces()
contains_char(_char)
not_contains_char(_char)
is_shorter_than(n_chars)
is_longer_than(n_chars)
has_length(n_chars)
has_not_length(n_chars)
is_lowercase()
is_not_lowercase()
is_uppercase()
is_not_uppercase()
is_camelcase()
is_not_camelcase()
is_snakecase()
is_not_snakecase()
is_unicode()
is_not_unicode()
is_json()
is_not_json()
is_yaml()
is_not_yaml()
is_xml()
is_not_xml()
matches(regex)
not_matches(regex)

# Booleans
is_boolean()
is_not_boolean()
is_true()
is_not_true()
is_truthy()
is_not_truthy()
is_false()
is_not_false()
is_falsy()
is_not_falsy()
has_same_truth_of(val)
has_opposite_truth_of(val)

# Dictionaries
is_dict()
is_not_dict()
has_keys(*args)
has_not_keys(*args)

# Functions
is_runnable()
is_not_runnable()

# Modules
is_module()
is_not_module()


# Type hierarchy
is_subtype_of(_type)
is_not_subtype_of(_type)

# Custom types
is_of_type(_type)
is_not_of_type(_type)

# Any type
equals(expected)
not_equals(expected)

# Geographic coords
is_latitude()
is_longitude()
is_azimuth()
is_geopoint()

```

## Coming soon

```python
# Dates
is_today()
is_not_today()
is_yesterday()
is_not_yesterday()
is_tomorrow()
is_not_tomorrow()
is_weekend()
is_not_weekend()
is_this_month()
is_not_this_month()
is_previous_month()
is_not_previous_month()
is_next_month()
is_not_next_month()
is_this_year()
is_not_this_year()
is_last_year()
is_not_last_year()
is_next_year()
is_not_next_year()
is_leap_year()
is_not_leap_year()
is_this_century()
is_not_this_century()
is_before(date)
is_not_before(date)
is_after(date)
is_not_after(date)
is_between_dates(lower, upper)
is_not_between_dates(lower, upper)
is_timezone_aware()
is_not_timezone_aware()
has_timezone(tz)
has_not_timezone(tz)
```