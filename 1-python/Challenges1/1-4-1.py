#use the `datetime` module to:

#parse a string like this "Month/Day/Year" 1/15/2025 into a datetime
#then print it like this: YYYY-MM-DD

#For example in the current date is January 15, 2025 the output should be 2025-01-15

#You will need to read through the module with `dir()` and `help()` or read the python docs to determine which functions to use.





import datetime
from datetime import datetime

# Get today's date
today = datetime.now()
print("Today's day:", today.day)

# Format today's date as YYYY-MM-DD
formatted_date = today.strftime("%Y-%m-%d")
print("Today's date (YYYY-MM-DD):", formatted_date)

# Parse a birthday string into a datetime object
birthday = "1/15/2025"
birthday_dt = datetime.strptime(birthday, "%m/%d/%Y")
print("Birthday formatted (YYYY-MM-DD):", birthday_dt.strftime("%Y-%m-%d"))

# Format birthday as "Monday January 15, 2025"
birthday_str = birthday_dt.strftime("%A %B %d, %Y")
print("Birthday formatted nicely:", birthday_str)