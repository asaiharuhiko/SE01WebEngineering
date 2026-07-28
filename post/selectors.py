from django.core.paginator import Paginator
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from .models import BlogPost
from .calendars import BlogCalendar

def get_latest_posts(page, per_page=5):
    
    queryset = BlogPost.objects.order_by("-creation_date")
    paginator = Paginator(queryset,per_page)
    return paginator.get_page(page)

def get_posts_by_query(query, page, per_page=5):
    queryset = BlogPost.objects.filter(
        title__icontains=query
    ).order_by("-creation_date")
    paginator = Paginator(queryset,per_page)
    return paginator.get_page(page)

def get_posts_by_date(date_str, page, per_page=5):
    queryset = BlogPost.objects.filter(
        creation_date__date=date_str
    ).order_by("-creation_date")
    paginator = Paginator(queryset,per_page)
    return paginator.get_page(page)

def get_posts_by_author(author, page, per_page=5):
    queryset = BlogPost.objects.filter(
        author__username=author
    ).order_by("-creation_date")
    paginator = Paginator(queryset, per_page)
    return paginator.get_page(page)

def get_post(id):
    return get_object_or_404(BlogPost,id=id)

def get_authors_list(page, per_page=5):
    User = get_user_model()
    queryset = User.objects.values_list("username", flat=True).order_by("username")
    paginator = Paginator(queryset, per_page)
    return paginator.get_page(page)


def get_calendar_context(year, month, selected_day):
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
            "selected_day": selected_day,
        }