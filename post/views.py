from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from .forms import BlogForm
from .selectors import (
    get_latest_posts,
    get_posts_by_query,
    get_posts_by_date,
    get_posts_by_author,
    get_post,
    get_calendar_context,
    get_authors_list,
)
from .services import create_post


class IndexView(View):
    def get(self, request):
        posts = get_latest_posts(request.GET.get("page", 1))

        if request.headers.get("HX-Request"):
            return render(
                request,
                "post/post_list.html",
                {"posts": posts, "base_url": reverse("post:index") + "?"},
            )

        return render(request, "post/index.html", {"posts": posts, "base_url": "/?"})


class SearchView(View):
    def get(self, request):
        page = request.GET.get("page", 1)
        words = request.GET.get("words")
        date_str = request.GET.get("date")
        author = request.GET.get("author")

        if words:
            posts = get_posts_by_query(words, page)
            header = f"search: {words}"
        elif date_str:
            posts = get_posts_by_date(date_str, page)
            header = f"search: {date_str}"
        elif author:
            posts = get_posts_by_author(author, page)
            header = f"search: {author}"
        else:
            return redirect("post:index")

        base_url = self._build_base_url(words, date_str, author)

        context = {"posts": posts, "search_header": header, "base_url": base_url}

        if request.headers.get("HX-Request"):
            return render(
                request, "post/post_list.html", {"posts": posts, "base_url": base_url}
            )

        return render(request, "post/search.html", context)

    def _build_base_url(self, words, date_str, author):
        if words:
            return f"/post/search/?words={words}"
        elif date_str:
            return f"/post/search/?date={date_str}"
        elif author:
            return f"/post/search/?author={author}"
        else:
            return ""


class CreatePostView(LoginRequiredMixin, View):
    login_url = "account:login"

    def get(self, request):
        form = BlogForm()
        return render(request, "post/create.html", {"form": form})

    def post(self, request):
        form = BlogForm(request.POST)
        if form.is_valid():
            create_post(form, request.user)
            return redirect("post:index")

        return render(request, "post/create.html", {"form": form})


class PostDetailView(View):
    def get(self, request, id):
        post = get_post(id)
        return render(request, "post/post_detail.html", {"post": post})


class CalendarView(View):
    def get(self, request, year, month):
        selected_day = request.GET.get("day")
        context = get_calendar_context(year, month, selected_day)
        return render(request, "components/calendar.html", context)


class AuthorsView(View):
    def get(self, request):
        page = request.GET.get("page", 1)
        authors = get_authors_list(page)

        if request.headers.get("HX-Request"):
            return render(request, "post/author_list.html", {"authors": authors})

        return render(request, "post/authors.html", {"authors": authors})


authors = AuthorsView.as_view()
search = SearchView.as_view()
index = IndexView.as_view()
create = CreatePostView.as_view()
detail = PostDetailView.as_view()
calendar = CalendarView.as_view()
