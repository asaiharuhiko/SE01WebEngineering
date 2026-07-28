import calendar 
from datetime import date

class BlogCalendar(calendar.HTMLCalendar):
    def __init__(self, year, month):
        super().__init__(firstweekday=0)
        self.year = year
        self.month = month
        
    def formatday(self, day, month):
        if day == 0:
            return '<td class="noday">&nbsp;</td>'

        d = date(self.year, self.month, day)
        url = f'/post/search/?date={d:%Y-%m-%d}'
        return (
            f'<td class="day">'
            f'<a href="{url}"'
            f'>{day}</a>'
            f'</td>'
        )