from datetime import datetime
from dateutil.parser import parse

def parsedate_mdy(date_str):
    """Parse a date string (MM/DD/YYYY) into a datetime object."""
    return parse(date_str)

def formatdate_ymd(date_obj):
    """Format a datetime object as YYYY-MM-DD."""
    return date_obj.strftime("%Y-%m-%d")