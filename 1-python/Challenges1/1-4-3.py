## Challenge 1-4-1
#use the `datetime` module to:
#parse a string like this "Month/Day/Year" 1/15/2025 into a datetime
#then print it like this: YYYY-MM-DD
#For example in the current date is January 15, 2025 the output should be 2025-01-15
#You will need to read through the module with `dir()` and `help()` or read the python docs to determine which functions to use.


#Let's make the code in 1-4-1 more resusable 
#re-write the date parse into a function `parsedate_mdy(text: str) -> datetime:`   
#re-write the date format into a function `formatdate_ymd(date: datetime) -> str:`  
#re-write the main program to use both functions. input -> parsedate -> formatdate -> output

#Let's make the code in 1-4-2 more resusable!!! 
#move your functions into a module names `dateutils.py`
#import your functions from `dateutils.py` into `1-4-3.py`
#from datetime import datetime
#from dateutil.parser import parse
from dateutils import parsedate_mdy, formatdate_ymd

dates = ["02/03/2026", "12/25/2025", "07/04/2023"]

for date_str in dates:
    date_obj = parsedate_mdy(date_str)
    formatted = formatdate_ymd(date_obj)
    print(f"Original: {date_str} -> Formatted: {formatted}")