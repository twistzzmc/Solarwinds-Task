from datetime import datetime, timedelta


class Day:
    def __init__(self, entries):
        self.date = None
        self.work = None

        self.weekend = False
        self.overtime = False
        self.undertime = False
        self.inconclusive = False

        self.__handle_entries(entries)

    def __handle_entries(self, entries):
        self.date = datetime.strptime(entries[0][0].split(' ')[0], '%Y-%m-%d').date()

        first_work_time = datetime.strptime(entries[0][0].split(' ')[1], '%H:%M:%S')
        last_work_time = datetime.strptime(entries[len(entries) - 1][0].split(' ')[1], '%H:%M:%S')

        self.work = last_work_time - first_work_time

        if self.date in {'5', '6'}:
            self.weekend = True

        if self.work > timedelta(hours=9):
            self.overtime = True
        elif self.work < timedelta(hours=6):
            self.undertime = True

        if entries[len(entries) - 1][1] == 'Reader entry':
            self.inconclusive = True

    def __repr__(self):
        return f'Day {self.date} Work {self.work}' + \
               (' w' if self.weekend else '') + \
               (' ot' if self.overtime else '') + \
               (' ut' if self.undertime else '') + \
               (' i' if self.inconclusive else '')
