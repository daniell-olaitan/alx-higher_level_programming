#!/usr/bin/python3
"""contains function that returns the JSON representation
   of an object (string)
"""

import json


def to_json_string(my_obj):
    """return the JSON representation of an object

    Args:
        my_obj: the given object
    """
    return json.dumps(my_obj)
