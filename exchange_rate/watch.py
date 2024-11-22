import time
from datetime import datetime as dt


def get_current_time():
    return dt.now().strftime('%d-%m-%Y %H:%M:%S')
