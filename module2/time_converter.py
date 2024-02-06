#!/usr/bin/python3

def timeConverter(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds


hours, minutes, seconds = timeConverter(10000)
print(hours, minutes, seconds)


