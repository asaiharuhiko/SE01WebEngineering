from django import template
from datetime import date
from post.calendars import BlogCalendar, get_prev_next_month

register = template.Library()


@register.inclusion_tag("components/calendar.html")
def calendar():
    today = date.today()
    year, month = today.year, today.month
    cal = BlogCalendar(year, month)
    calendar_html = cal.formatmonth(year, month)

    prev_year, prev_month, next_year, next_month = get_prev_next_month(year, month)

    return {
        "calendar_html": calendar_html,
        "year": year,
        "month": month,
        "prev_year": prev_year,
        "prev_month": prev_month,
        "next_year": next_year,
        "next_month": next_month,
    }
