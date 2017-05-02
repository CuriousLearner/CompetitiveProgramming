from datetime import timedelta

def add_gigasecond(moment):
    return moment + timedelta(seconds=10**9)
