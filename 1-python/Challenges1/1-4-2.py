#Let's make the code in 1-4-1 more resusable 

#re-write the date parse into a function `parsedate_mdy(text: str) -> datetime:`   
#re-write the date format into a function `formatdate_ymd(date: datetime) -> str:`  
#re-write the main program to use both functions. input -> parsedate -> formatdate -> output



from datetime import datetime

# parse date from MM/DD/YYYY to datetime object
def parsedate_mdy(text: str) -> datetime:
    return datetime.strptime(text, "%m/%d/%Y")

# format datetime object to YYYY-MM-DD
def formatdate_ymd(date: datetime) -> str:
    return date.strftime("%Y-%m-%d")


if __name__ == "__main__":
    # main program
    date = '12/30/2000'
    date_dt = parsedate_mdy(date)
    date_str = formatdate_ymd(date_dt)
    print(date_str)  # Output: 2000-12-30

    # simple test without pytest
    date_dt_expected = datetime(2000, 12, 30)
    date_actual = parsedate_mdy(date)
    assert date_dt_expected == date_actual

    # test formatdate_ymd
    date_str_expected = '2000-12-30'
    date_str_actual = formatdate_ymd(date_dt)
    assert date_str_expected == date_str_actual