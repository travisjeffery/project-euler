from datetime import date

def first_day_of_month_1901_to_2000():
    base = date(1901, 1, 1)
    yield base
    while base.year < 2001:
        if base.month == 12:
            base = base.replace(year=base.year+1)
            base = base.replace(month=1)
        else:
            base = base.replace(month=base.month+1)
        yield base

print len([base for base in first_day_of_month_1901_to_2000() \
           if base.weekday() == 6])
