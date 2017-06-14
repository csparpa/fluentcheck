# check
_Fluent assertions for Python values_

Bored of using `assert` multiple times to check types, intervals, etc. for the data fed to your Python functions?
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


## Installation
```shell
python2 setup.py install
```


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
is_complex()
is_not_complex()
is_positive()
is_negative()
is_zero()
is_at_least(lower)
is_at_most(upper)
is_between(lowerupper)

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
is_json()
is_not_json()
is_yaml()
is_not_yaml()
is_xml()
is_not_xml()

# Sequences
is_empty()
is_not_empty()
is_iterable()
is_not_iterable()

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

# Custom types
is_of_type(_type)
is_not_of_type(_type)

# ...
```