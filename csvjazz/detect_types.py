import csv
from dateutil import 

def get_type(s):
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


