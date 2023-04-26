# PyRegexParse
`PyRegexParse` is a Python function that can be used to parse a string of text using a regular expression pattern.


# Installation
You can install requirements using pip:
```
$ pip install -r requirements.txt
```

## Usage
To use PyRegexParser, import the `parse_text` function and provide it with an input string to be parsed and a regular expression pattern:

```
from parse_text import parse_text
# input string to be parsed
input_str = "Some text to be parsed"

# regex pattern for parsing the input string
regex = r"Some regex pattern"

# parse the input string using the regex pattern
parsed_data = parse_text(input_str, regex)
```

## Example <a name = "example"></a>
**Input:**
```python
input_str = """
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    1    0.000    0.000    0.007    0.007 timeit.py:164(timeit)
    1    0.000    0.000    0.007    0.007 <timeit-src>:2(inner)
    1    0.000    0.000    0.007    0.007 benchmark.py:92(<lambda>)
    1    0.004    0.004    0.007    0.007 clip_method.py:51(process)
    1    0.000    0.000    0.003    0.003 <__array_function__ internals>:177(clip)
"""

regex = r'^.*?(\S+?)\s+?(\S+?)\s+?(\S+?)\s+?(\S+?)\s+?(\S+?)\s+?(\S.*?)$'
header = True

headers, data = parse_text(input_string=input_str, regex_string=regex, header=header)
```

**Returns:**
```python
    tuple headers = [
                ('ncalls', 'tottime', 'percall', 'cumtime', 'percall', 'filename:lineno(function)')
        ]

    list data = [
                ('1', '0.000', '0.000', '0.007', '0.007', 'timeit.py:164(timeit)')
                ('1', '0.000', '0.000', '0.007', '0.007', '<timeit-src>:2(inner)')
                [...]
        ]
```
```python
    headers[5] => 'filename:lineno(function)'
    data[1][5] => '<timeit-src>:2(inner)'
```

# API
**Args:**

* `input_string` (str): The text to be parsed.
* `regex_string` (str): The regex pattern for parsing the input_string.
* `header` (Union[bool, str], optional): If True or a regex string, the first line will be parsed as a header. If a regex string is provided, it will be used to parse the header. Defaults to False.

**Returns:**

* `Tuple[List[str], List[Tuple[str]]]`: A tuple containing a list of header values (if applicable) and a list of tuples with parsed data.

The `headers` list contains the column names for each value in the `data` tuples. The length of each tuple in `data` depends on the number of capturing groups in the regular expression pattern.

**Raises:**

`ValueError`: If input_string or regex_string are not of the expected types, are empty, no lines are found in input_string, the provided regex patterns are invalid, or no match is found for a line.

# Contributing
Contributions are welcome! If you'd like to contribute to PyRegexParser, please submit a pull request or open an issue.

# License
Released under the [MIT-License](./LICENSE)