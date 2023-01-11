#!/usr/bin/python3
"""contains a function that deserialize a JSON string"""

import json


def from_json_string(my_str):
    """returns an object represented by a JSON string

    Args:
        my_str: the JSON string
    """
    return json.loads(my_str)
