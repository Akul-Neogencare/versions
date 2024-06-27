import pytz

from datetime import datetime


def get_user_locale():

    local_time = datetime.now(pytz.timezone('UTC')).astimezone()
    print(local_time.tzinfo)
    print(datetime.now())
    try:
        start_time_str = "2024-06-27 09:11:38"
        start_time = datetime.strptime(start_time_str, '%Y-%m-%d %H:%M:%S')

        local_date_time = datetime.now()
        indian_tz = pytz.timezone('Asia/Kolkata')
        indian_date_time = local_date_time.astimezone(indian_tz)
        one = indian_date_time.replace(tzinfo=None)
        time_difference = one - start_time

        new = indian_date_time.strftime('%Y-%m-%d %H:%M:%S')
        print(time_difference)
        print(one)
    except Exception as E:
        print(E)


