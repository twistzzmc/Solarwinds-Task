from datetime import timedelta


class Week:
    def __init__(self, days):
        self.days = days
        self.total_work = timedelta()
        self.unusual_work_time = None
        self.overtime = None

        self.__handle_days()

    def __handle_days(self):
        for day in self.days:
            self.total_work += day.work

        usual_work_time = timedelta(hours=8 * len(self.days))

        self.unusual_work_time = abs(self.total_work - usual_work_time)

        if usual_work_time.days > self.total_work.days or \
           usual_work_time.seconds > self.total_work.seconds:
            self.overtime = True
        else:
            self.overtime = False

    def __repr__(self):
        days_string = ''
        for day in self.days[:len(self.days) - 1]:
            days_string += str(day) + '\n'
        days_string += str(self.days[len(self.days) - 1])

        return days_string + ' ' + \
            Week.__get_timedelta_without_days(self.total_work) + \
            (' -' if self.overtime else ' ') + \
            Week.__get_timedelta_without_days(self.unusual_work_time)

    @staticmethod
    def __get_timedelta_without_days(time):
        hours = int(time.seconds / 3600) + time.days * 24
        minutes = int((time.seconds % 3600) / 60)
        seconds = time.seconds % 3600 % 60
        return str(hours) + ':' + \
            ('0' if len(str(minutes)) == 1 else '') + str(minutes) + ':' + \
            ('0' if len(str(seconds)) == 1 else '') + str(seconds)
