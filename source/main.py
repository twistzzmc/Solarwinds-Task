import csv
from datetime import datetime
from source.Day import Day
from source.Week import Week


def validate_row(i, row, prev_date):
    if row[1] not in {'Reader entry', 'Reader exit'}:
        raise ValueError(
            f'ERROR: [line {i + 1}] Events must be either \'Reader entry\' or \'Reader exit\', not: [{row[1]}]')

    try:
        previous_date = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S ')
    except ValueError:
        raise ValueError(f'ERROR [line {i + 1}] Bad date format: {row[0]}')

    if i > 1 and \
            datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S ') < prev_date:
        raise ValueError(f'ERROR: [lines {i + 1}, {i}] Dates must in ascending order!')

    return previous_date


def get_days(file):
    days = []
    day_entries = []

    previous_date = None

    for i, row in enumerate(file):
        if i == 0:
            if len(row) != 3:
                raise ValueError(f'ERROR [line {i+1}] Wrong number of columns, must be 3 not {len(row)}!')

            if row[0] != 'Date' or row[1] != 'Event' or row[2] != 'Gate':
                raise ValueError(f'ERROR: [line {i+1}] Bad columns, should be \'Date;Event;Gate\'')

            continue

        previous_date = validate_row(i, row, previous_date)

        if len(day_entries) == 0 or row[0].split(' ')[0] == day_entries[len(day_entries) - 1][0].split(' ')[0]:
            day_entries.append(row)
        else:
            days.append(Day(day_entries))
            day_entries = [row]

    days.append(Day(day_entries))

    return days


def get_weeks(days):
    weeks = []
    week_days = []

    for day in days:
        if len(week_days) == 0 or \
                day.date.weekday() > week_days[len(week_days) - 1].date.weekday() or \
                (week_days[len(week_days) - 1].date - day.date).days >= 7:
            week_days.append(day)
        else:
            weeks.append(Week(week_days))
            week_days = [day]

    weeks.append(Week(week_days))

    return weeks


def main(file):
    with open(file, 'r', encoding='utf-8') as f:
        csv_file = csv.reader(f, delimiter=';')

        days = get_days(csv_file)
        weeks = get_weeks(days)

        with open('result', 'w', encoding='utf-8') as result:
            for week in weeks:
                result.write(str(week) + '\n')
