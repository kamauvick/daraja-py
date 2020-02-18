""" Random helpful functions for the project. """

from datetime import datetime

#Generate a timestamp
def generate_timestamp():
    unformatted_time = datetime.now()
    formatted_time = unformatted_time.strftime('%Y%m%d%H%M%S')
    return formatted_time
