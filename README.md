# Fluentcheck
_Fluent assertion framework for Python_

Bored of using `assert` multiple times to check types, intervals, etc. on data passed as input to your Python functions?
This generates a lot of boilerplate code.

__fluentcheck__ helps you reducing the lines of code providing a human-friendly and fluent way to make assertions.

Instead of:

```python
def my_function(n, obj):
    assert n is not None
    assert isinstance(n, float)
    assert 0. < n < 1.
    assert obj is not None
    assert isinstance(obj, MyCustomType)
```

you just streamline the assertions ("checks") you want to make, in a fluent way:

```python
from fluentcheck import Check

def my_function(n, obj):
    Check(n).is_not_None().is_float().is_between(0., 1.)
    Check(obj).is_not_None().is_subtype_of(MyCustomType)
```

You can even use the alternate `Is` syntax:

```python
from fluentcheck import Is

def my_function(n, obj):
    Is(n).not_none.float.between(0, 1)
    Is(obj).not_none.subtype_of(MyCustomType)
```

__Fluentcheck__ can also be used as an _assertion framework in tests_.


## Installation
```shell
pip install fluentcheck
```
or 

```shell
python setup.py install
```

Only _Python 3_ is supported (because you DID update your code to Python3, didn't you?)


## Usage

### Check API

Simply instantiate the `Check` wrapper around the Python value you want to
check out, then fluently append assertions like this:

```python
from fluentcheck import Check

Check(my_value).assertion1().assertion2().assertion3() # and so on
```

### Is API

Simply instantiate the `Is` wrapper around the Python value you want to
check out, then fluently append assertions like this:

```python
from fluentcheck import Is

Is(my_value).assertion1.assertion2_with_params(a, b).assertion3 # and so on
```

### When an assertion fails

What if an assertion fails? A `CheckError` is raised: just catch it!

Please notice: if the order of assertions _matters_ to your overall goal, _then take care of it_!


### Linters and Is API

You may run into warnings for code such as this when using the `Is` API:

```python
n = .4
Is(n).not_none.float.non_negative

# WARNING: Statement seems to have no effect ...
```

While not required for assertions to work, you can always "call" the last assertion to make linters happy: 


```python
n = .4
Is(n).not_none.float.non_negative()

# Happy, calling non_negative() has no effect but the linter warnings are gone.
```

## What can I actually check with it?
To date, here's a list of assertions you can make:

### Check API

```python
# Check(value).X where X is one of:

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
is_not_positive()
is_negative()
is_not_negative()
is_zero()
is_not_zero()
is_at_least(lower)
is_at_most(upper)
is_between(lower, upper)
is_not_between(lower, upper)

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

# Sets
is_set()
is_not_set()
is_subset_of(_set)
is_not_subset_of(_set)
is_superset_of(_set)
is_not_superset_of(_set)
intersects(_set)
not_intersects(_set)

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

# Geographic coords
is_latitude()
is_longitude()
is_azimuth()
is_geopoint()

# UUIDs
is_uuid1()
is_not_uuid1()
is_uuid4()
is_not_uuid4()

```

### Is API

```python
# Is(value).X where X is one of:

# Numbers
none
not_none
number
not_number
integer
not_integer
float
not_float
real
not_real
complex
not_complex
positive
not_positive
negative
not_negative
zero
not_zero
at_least(lower)
at_most(upper)
between(lower, upper)
not_between(lower, upper)

# Sequences
empty
not_empty
iterable
not_iterable
has_dimensionality(dimensionality)

# Tuples
tuple

# Lists
list

# Strings
string
not_string
contains_numbers
not_contains_numbers
only_numbers
contains_chars
not_contains_chars
only_chars
contains_spaces
not_contains_spaces
contains_char(_char)
not_contains_char(_char)
shorter_than(n_chars)
longer_than(n_chars)
length(n_chars)
not_length(n_chars)

json
not_json
matches(regex)
not_matches(regex)

# Booleans
boolean
not_boolean
true
not_true
truthy
not_truthy
false
not_false
falsy
not_falsy
has_same_truth_of(val)
has_opposite_truth_of(val)

# Dictionaries
dict
not_dict
has_keys(*args)
has_not_keys(*args)

# Sets
set
not_set
subset_of(_set)
not_subset_of(_set)
superset_of(_set)
not_superset_of(_set)
intersects(_set)
not_intersects(_set)

# Type hierarchy
subtype_of(_type)
not_subtype_of(_type)

# UUIDs
is_uuid1()
is_not_uuid1()
is_uuid4()
is_not_uuid4()

```


## Coming soon

The following checks will be added in the upcoming versions:

```python
# Dates
is_date()
is_not_date()
is_datetime()
is_not_datetime()
is_before(_datetime)
is_not_before(_datetime)
is_after(_datetime)
is_not_after(_datetime)
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

# Geographic coords
is_plus_code()  # https://plus.codes/
is_not_plus_code()

# Check against a custom rule (lambda)
conforms_to(func)
not_conforms_to(func)

# Sequences
is_sorted(rule=func)
is_not_sorted(rule=func)
is_subsequence_of(subseq)
is_not_subsequence_of(subseq)
has_duplicates()
has_not_duplicates()

# Objects
contains(element)
not_contains(element)
has_attribute(_attr)
has_not_attribute(_attr)


```

## License
MIT license
