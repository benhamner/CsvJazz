import csv
from dateutil.parser import parse

def detect_type(s):
    try:
        int(s)
        return "int"
    except ValueError:
        pass

    try:
        float(s)
        return "float"
    except ValueError:
        pass

    try:
        parse(s)
        return "datetime"
    except ValueError:
        pass

    return "str"

def greater_type(type1, type2):
    if (type1 == "str") or (type2 == "str"): return "str"
    if (type1 == "datetime") or (type2 == "datetime"): return "datetime"
    if (type1 == "float") or (type2 == "float"): return "float"
    return type1