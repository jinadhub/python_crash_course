#!/usr/bin/python3

def calculate_total_days(years, month, days):
    days_in_year = years * 365
    days_in_month = month * 30
    days_in_day = days * 1
    return (days_in_year + days_in_month + days_in_day)


print (calculate_total_days(2,4,30))


