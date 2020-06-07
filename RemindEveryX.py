"""
RemindEveryX

Sends a text message on recurring events that occur on specific days of the
week (ex. The First Saturday of April, every Wednseday in February)

The script uses Gmail to send text messages as email, so it requires a Gmail
account and a mobile phone number with a wireless carrier designated in the
config.json file
"""

from calendar import TextCalendar
from datetime import datetime
from helper_functions import load_json, send_text

# If you want to hard-code a date (ex. for testing, use this instead)
# current_date = datetime(2020, 1, 4)
current_date = datetime.now()


def main():
    current_year = current_date.year
    current_month = current_date.month
    current_month_name = current_date.strftime("%B")
    current_weekday = current_date.weekday()
    current_weekday_name = current_date.strftime("%A")

    cal = TextCalendar().monthdatescalendar(current_year, current_month)

    events_dict = load_json("events.json")
    dates = []
    message = []

    for week in cal:
        for day in week:
            if day.month == current_month and day.weekday() == current_weekday:
                dates.append(day)

    if current_month_name in events_dict \
            and current_weekday_name in events_dict[current_month_name]:
        events = events_dict[current_month_name][current_weekday_name]

        if "First" in events and events["First"]:
            if current_date.date() == dates[0]:
                message.append(events["First"])

        if "Last" in events and events["Last"]:
            if current_date.date() == dates[-1]:
                message.append(events["Last"])

        if "Every" in events and events["Every"]:
            message.append(events["Every"])

    if message:
        send_text(', '.join(message))
    else:
        print("No notifications")


if __name__ == "__main__":
    main()
