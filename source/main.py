import csv
from source.Day import Day
from source.Week import Week


def get_days(file):
    days = []
    day_entries = []

    for i, row in enumerate(file):
        if i == 0:
            continue

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
