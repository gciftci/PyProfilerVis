# package\utils\utils.py
from package.utils.regex_parser import parse_text
from typing import List, Tuple, Union


def process_data(input_str: str,
                 regex: str,
                 header: Union[bool, str] = False) -> Tuple[List[str], List[Tuple[str]]]:

    # Parse data
    headers, data = parse_text(input_str, regex, header)

    # Calculate the total timeline
    progress_total_time = round(float(data[0][3]) * 1000)

    # Add the Duration column to the headers
    headers = list(headers) + [f"Duration (Total: {progress_total_time}ms)"]

    # Calculate Duration of each Call and add to data
    for i in range(len(data)):
        if i < len(data) - 1:  # If we are not at the last row
            length = round((float(data[i][3]) - float(data[i+1][3])) * 1000)  # Calculate the difference and *1000
        else:
            length = round(float(data[i][3]) * 1000)  # If we are at the last row, just multiply the value by 1000

        data[i] = data[i] + (length,)  # Add the calculated value to the current row
    return headers, data, progress_total_time
