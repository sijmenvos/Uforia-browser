#!/usr/bin/env python

import datetime

def getType(value=None):
    """
    
    elasticsearch has the following coretypes:
    string, integer/long, float/double, boolean, and null

    python floats are almost always c doubles, so there is no check for double.
    we default to string for convenience sake.
    
    """

    if value == "bigint":
        return str("long")
    
    elif value == "bit":
        return str("boolean")
    
    elif value == "int":
        return str("integer")
    
    elif value == "float":
        return str("float")

    elif value == "date":
        return str("date")

    elif value == "text":
        return str("string")

    elif value == "time":
        return str("time")

    elif value == "double":
        return str("float")

    else:
        return str("string")
#    if isinstance(value, int):
#        return str("integer")
#    elif isinstance(value, long):
#        return str("long")
#    elif isinstance(value, str):
#        return str("string")
#    elif isinstance(value, float):
#        return str("float")
#    elif isinstance(value, bool):
#        return str("boolean")
#    elif isinstance(value, datetime.date):
#        return str("date")
#    elif isinstance(value, datetime.datetime):
#        return str("date")
#    else:
#        return str("string")


