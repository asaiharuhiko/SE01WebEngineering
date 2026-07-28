from django import template
from datetime import date
from post.calendars import BlogCalendar

register = template.Library()


@register.inclusion_tag("components/calendar.html")
def calendar():
    today = date.today()
    year, month = today.year, today.month
    cal = BlogCalendar(year, month)
    calendar_html = cal.formatmonth(year, month)

    if month == 1:
        prev_year, prev_month = year - 1, 12
        next_year, next_month = year, 2
    elif month == 12:
        prev_year, prev_month = year, 11
        next_year, next_month = year + 1, 1
    else:
        prev_year, prev_month = year, month - 1
        next_year, next_month = year, month + 1

    return {
        "calendar_html": calendar_html,
        "year": year,
        "month": month,
        "prev_year": prev_year,
        "prev_month": prev_month,
        "next_year": next_year,
        "next_month": next_month,
    }
