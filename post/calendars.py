import calendar 
from datetime import date
from django.urls import reverse

class BlogCalendar(calendar.HTMLCalendar):
    def __init__(self, year, month):
        super().__init__(firstweekday=0)
        self.year = year
        self.month = month
        
    def formatday(self, day, month):
        if day == 0:
            return '<td class="noday">&nbsp;</td>'

        d = date(self.year, self.month, day)
        url = reverse("post:search") + f"?date{d:%Y-%m-%d}"
        return (
            f'<td class="day">'
            f'<a href="{url}"'
            f'>{day}</a>'
            f'</td>'
        )


def get_prev_next_month(year, month):
    if month == 1:
        prev_year, prev_month = year - 1, 12
        next_year, next_month = year, 2
    elif month == 12:
        prev_year, prev_month = year, 11
        next_year, next_month = year + 1, 1
    else:
        prev_year, prev_month = year, month - 1
        next_year, next_month = year, month + 1
    return prev_year, prev_month, next_year, next_month