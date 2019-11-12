import time

from django.utils import timezone


def mktime(date=None, ts=True):
    if not date:
        date = timezone.now()

    if not ts:
        return time.mktime(date.timetuple())  # 1533697871.0

    return int(time.mktime(date.timetuple()))  # 1533697871.0


def now():
    return timezone.now()
