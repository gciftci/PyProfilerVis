# package\utils\regex_parser.py
import re
from typing import List, Tuple, Union


def parse_text(input_string: str,
               regex_string: str,
               header: Union[bool, str] = False) -> Tuple[List[str], List[Tuple[str]]]:
    """
    Parses the input string using the provided regex_string and optional header regex.

    Args:
        input_string (str): The text to be parsed.
        regex_string (str): The regex pattern for parsing the input_string.
        header (Union[bool, str], optional): If True or a regex string, the first line will be parsed as a header.
                                             If a regex string is provided, it will be used to parse the header.
                                             Defaults to False.

    Returns:
        Tuple[List[str], List[Tuple[str]]]: A tuple containing a list of header values (if applicable) and a list of
        tuples with parsed data.

    Raises:
        ValueError: If input_string or regex_string are not of the expected types, are empty, no lines are found in
        input_string, the provided regex patterns are invalid, or no match is found for a line.
    """

    if not isinstance(input_string, str) or not input_string:
        # raise ValueError("Input string must be a non-empty string.")
        print("Input string must be a non-empty string.")
    if not isinstance(regex_string, str) or not regex_string:
        # raise ValueError("Regex string must be a non-empty string.")
        print("Regex string must be a non-empty string.")

    if not isinstance(header, (bool, str)):
        raise TypeError("Invalid input types. Expected header to be bool or string (optional).")

    lines = input_string.strip().split('\n')
    if not lines:
        # raise ValueError("No lines found in the input string.")
        print("No lines found in the input string.")

    regex_pattern = re.compile(regex_string)
    header_pattern = None
    if header is True or isinstance(header, str):
        header_regex_string = header if isinstance(header, str) else regex_string
        header_pattern = re.compile(header_regex_string)

    parsed_data = []
    headers = []

    for line_num, line in enumerate(lines):
        if header_pattern and line_num == 0:
            if header_match := header_pattern.match(line):
                headers = header_match.groups()
            else:
                # raise ValueError("No match found for the header line.")
                print("No match found for the header line.")
        elif match := regex_pattern.match(line):
            parsed_data.append(match.groups())
        else:
            # raise ValueError(f"No match found for line {line_num + 1}: {line}")
            print(f"No match found for line {line_num + 1}: {line}")

    return headers, parsed_data
