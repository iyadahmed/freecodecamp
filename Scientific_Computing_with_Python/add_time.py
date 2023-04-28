days = [
    "Saturday",
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
]


def add_time(start, duration, start_day: str | None = None):
    # Prase start time
    start_time_str, am_pm_str = start.split(" ")
    start_hours_str, start_minutes_str = start_time_str.split(":")
    start_hours_int = int(start_hours_str)
    start_minutes_int = int(start_minutes_str)

    # Convert start time to 24-hour time
    if am_pm_str == "PM":
        start_hours_int += 12

    # Convert start time to minutes
    start_total_minutes = start_hours_int * 60 + start_minutes_int

    # Parse duration
    duration_hours_str, duration_minutes_str = duration.split(":")
    duration_hours_int = int(duration_hours_str)
    duration_minutes_int = int(duration_minutes_str)

    # Convert duration to minutes
    duration_total_minutes = duration_hours_int * 60 + duration_minutes_int

    # Calculate total minutes (start time + duration)
    total_minutes = start_total_minutes + duration_total_minutes

    # Convert total minutes to days, hours, and minutes
    total_days = (total_minutes // 60) // 24
    result_hours = (total_minutes - total_days * 24 * 60) // 60
    result_minutes = total_minutes - total_days * 24 * 60 - result_hours * 60

    # Convert result hours to 12-hour format
    if result_hours > 12:
        result_am_pm = "PM"
        result_hours -= 12

    elif result_hours == 12 and result_minutes > 0:
        result_am_pm = "PM"

    elif result_hours == 0:
        result_am_pm = "AM"
        result_hours += 12

    else:
        result_am_pm = "AM"

    # Determine suffix based on number of passed days
    suffix = ""
    if total_days == 1:
        suffix = " (next day)"
    elif total_days > 1:
        suffix = f" ({total_days} days later)"

    # Determine end day based on start day and number of passed days
    end_day: str | None = None
    if start_day is not None:
        start_day = start_day.capitalize()
        if total_days == 0:
            end_day = start_day
        else:
            start_day_index = days.index(start_day)
            end_day = days[(start_day_index + total_days) % len(days)]

    result = f"{result_hours}:{result_minutes:02} {result_am_pm}"

    if end_day is not None:
        result += f", {end_day}"

    result += suffix

    return result


add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)
