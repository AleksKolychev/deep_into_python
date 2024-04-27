"""В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку."""

from datetime import datetime as dt
from calendar import isleap
import argparse

def check_date(date: str):
    try:
        t = dt.strptime(date, '%d.%m.%Y')
        _isleap(t.year)
        return True
    except:
        return False

def _isleap(year: int):
    print("Leap" if isleap(year) else "Not leap")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Check if a given date is valid and if the year is a leap year.')
    parser.add_argument('date', help='Date in the format dd.mm.yyyy')
    args = parser.parse_args()
    
    if check_date(args.date):
        print(f"{args.date} is a valid date.")
    else:
        print(f"{args.date} is not a valid date.")
