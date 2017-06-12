# check
_Fluent assertions for Python values_

Bored of using `assert` multiple times to check types, intervals, etc. for the data fed to your Python functions?
This generates a lot of boilerplate code. __check__ helps you reducing the lines of code providing you a human-friendly and fluent way to make assertions.

Instead of:

```python
def my_function(value):
    assert value is not None
    assert instanceof(value, float)
    assert 0. < x < 1.
```

just:

```python
from check import Check

def my_function(value):
    Check(value).is_not_None().is_float().is_between(0., 1.)
```



## Installation
Just clone the repository and you're done!
