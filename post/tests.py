from datetime import date

from django.contrib.auth import get_user_model
from django.http import Http404
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .calendars import BlogCalendar, get_prev_next_month
from .forms import BlogForm
from .models import BlogPost
from .selectors import (
    get_authors_list,
    get_calendar_context,
    get_latest_posts,
    get_post,
    get_posts_by_author,
    get_posts_by_date,
    get_posts_by_query,
)
from .services import create_post


class BlogPostModelTests(TestCase):
    def test_string_representation(self):
        post = BlogPost(title="Hello World")
        self.assertEqual(str(post), "Hello World")


class BlogFormTests(TestCase):
    def test_valid_form(self):
        form = BlogForm(
            data={
                "title": "Test Post",
                "content": "Some content",
                "creation_date": timezone.now(),
            }
        )
        self.assertTrue(form.is_valid())

    def test_form_fields(self):
        form = BlogForm()
        self.assertListEqual(
            list(form.fields.keys()), ["title", "content", "creation_date"]
        )

    def test_form_requires_title(self):
        form = BlogForm(data={"content": "no title", "creation_date": timezone.now()})
        self.assertFalse(form.is_valid())

    def test_form_requires_content(self):
        form = BlogForm(data={"title": "no content", "creation_date": timezone.now()})
        self.assertFalse(form.is_valid())


class SelectorsTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="author1")
        self.user2 = get_user_model().objects.create_user(username="author2")
        for i in range(12):
            BlogPost.objects.create(
                title=f"Post {i}",
                content=f"Content {i}",
                author=self.user if i % 2 == 0 else self.user2,
                creation_date=timezone.make_aware(timezone.datetime(2026, 7, 20 - i)),
            )

    def test_get_latest_posts_returns_most_recent_first(self):
        page = get_latest_posts(1, per_page=5)
        posts = list(page)
        self.assertEqual(len(posts), 5)
        self.assertEqual(posts[0].title, "Post 0")

    def test_get_latest_posts_pagination(self):
        page = get_latest_posts(2, per_page=5)
        posts = list(page)
        self.assertEqual(len(posts), 5)

    def test_get_latest_posts_last_page(self):
        page = get_latest_posts(3, per_page=5)
        posts = list(page)
        self.assertEqual(len(posts), 2)

    def test_get_latest_posts_empty(self):
        BlogPost.objects.all().delete()
        page = get_latest_posts(1, per_page=5)
        self.assertEqual(len(list(page)), 0)

    def test_get_posts_by_query_matches_title(self):
        page = get_posts_by_query("Post 1", 1, per_page=5)
        titles = [p.title for p in page]
        self.assertIn("Post 1", titles)
        self.assertNotIn("Post 2", titles)

    def test_get_posts_by_query_case_insensitive(self):
        page = get_posts_by_query("post", 1, per_page=20)
        self.assertEqual(len(list(page)), 12)

    def test_get_posts_by_query_no_match(self):
        page = get_posts_by_query("nonexistent", 1, per_page=5)
        self.assertEqual(len(list(page)), 0)

    def test_get_posts_by_date_matches(self):
        target_date = date(2026, 7, 20)
        page = get_posts_by_date(str(target_date), 1, per_page=5)
        titles = [p.title for p in page]
        self.assertIn("Post 0", titles)

    def test_get_posts_by_date_no_match(self):
        page = get_posts_by_date("2025-01-01", 1, per_page=5)
        self.assertEqual(len(list(page)), 0)

    def test_get_posts_by_author_matches(self):
        page = get_posts_by_author("author1", 1, per_page=10)
        titles = [p.title for p in page]
        for i in range(0, 12, 2):
            self.assertIn(f"Post {i}", titles)

    def test_get_posts_by_author_no_match(self):
        page = get_posts_by_author("nonexistent", 1, per_page=5)
        self.assertEqual(len(list(page)), 0)

    def test_get_post_returns_post(self):
        post = get_post(1)
        self.assertIsInstance(post, BlogPost)

    def test_get_post_raises_404(self):
        with self.assertRaises(Http404):
            get_post(9999)

    def test_get_authors_list_returns_usernames(self):
        page = get_authors_list(1, per_page=5)
        authors = list(page)
        self.assertIn("author1", authors)
        self.assertIn("author2", authors)

    def test_get_authors_list_pagination(self):
        page = get_authors_list(1, per_page=1)
        self.assertEqual(len(list(page)), 1)

    def test_get_calendar_context_keys(self):
        context = get_calendar_context(2026, 7, None)
        self.assertIn("calendar_html", context)
        self.assertIn("year", context)
        self.assertIn("month", context)
        self.assertIn("prev_year", context)
        self.assertIn("prev_month", context)
        self.assertIn("next_year", context)
        self.assertIn("next_month", context)
        self.assertIn("selected_day", context)

    def test_get_calendar_context_values(self):
        context = get_calendar_context(2026, 7, "15")
        self.assertEqual(context["year"], 2026)
        self.assertEqual(context["month"], 7)
        self.assertEqual(context["selected_day"], "15")


class ServicesTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="author1")

    def test_create_post_assigns_author(self):
        form = BlogForm(
            data={
                "title": "New Post",
                "content": "Content",
                "creation_date": timezone.now(),
            }
        )
        self.assertTrue(form.is_valid())
        post = create_post(form, self.user)
        self.assertEqual(post.author, self.user)
        self.assertEqual(BlogPost.objects.count(), 1)

    def test_create_post_returns_post(self):
        form = BlogForm(
            data={
                "title": "Another Post",
                "content": "Content",
                "creation_date": timezone.now(),
            }
        )
        self.assertTrue(form.is_valid())
        post = create_post(form, self.user)
        self.assertIsInstance(post, BlogPost)


class CalendarTests(TestCase):
    def test_formatday_with_day_returns_link(self):
        cal = BlogCalendar(2026, 7)
        result = cal.formatday(15, 7)
        self.assertIn('<td class="day">', result)
        self.assertIn('href="/post/search/?date=2026-07-15"', result)
        self.assertIn(">15<", result)

    def test_formatday_with_zero_returns_empty(self):
        cal = BlogCalendar(2026, 7)
        result = cal.formatday(0, 7)
        self.assertEqual(result, '<td class="noday">&nbsp;</td>')

    def test_get_prev_next_month_january(self):
        prev_year, prev_month, next_year, next_month = get_prev_next_month(2026, 1)
        self.assertEqual(prev_year, 2025)
        self.assertEqual(prev_month, 12)
        self.assertEqual(next_year, 2026)
        self.assertEqual(next_month, 2)

    def test_get_prev_next_month_december(self):
        prev_year, prev_month, next_year, next_month = get_prev_next_month(2026, 12)
        self.assertEqual(prev_year, 2026)
        self.assertEqual(prev_month, 11)
        self.assertEqual(next_year, 2027)
        self.assertEqual(next_month, 1)

    def test_get_prev_next_month_mid_year(self):
        prev_year, prev_month, next_year, next_month = get_prev_next_month(2026, 7)
        self.assertEqual(prev_year, 2026)
        self.assertEqual(prev_month, 6)
        self.assertEqual(next_year, 2026)
        self.assertEqual(next_month, 8)


class IndexViewTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="author1")
        BlogPost.objects.create(
            title="First Post",
            content="Content",
            author=self.user,
            creation_date=timezone.now(),
        )

    def test_index_get_returns_200(self):
        response = self.client.get(reverse("post:index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "post/index.html")

    def test_index_has_posts_in_context(self):
        response = self.client.get(reverse("post:index"))
        self.assertIn("posts", response.context)
        self.assertEqual(len(list(response.context["posts"])), 1)

    def test_index_has_base_url(self):
        response = self.client.get(reverse("post:index"))
        self.assertEqual(response.context["base_url"], "/?")

    def test_index_htmx_returns_partial(self):
        response = self.client.get(
            reverse("post:index"), headers={"HX-Request": "true"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "post/post_list.html")

    def test_index_htmx_has_correct_base_url(self):
        response = self.client.get(
            reverse("post:index"), headers={"HX-Request": "true"}
        )
        self.assertEqual(response.context["base_url"], reverse("post:index") + "?")

    def test_index_empty_posts(self):
        BlogPost.objects.all().delete()
        response = self.client.get(reverse("post:index"))
        self.assertEqual(len(list(response.context["posts"])), 0)


class SearchViewTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="author1")
        BlogPost.objects.create(
            title="Unique Title",
            content="Content",
            author=self.user,
            creation_date=timezone.now(),
        )

    def test_search_by_words_returns_results(self):
        response = self.client.get(reverse("post:search"), {"words": "Unique"})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "post/search.html")
        self.assertEqual(len(list(response.context["posts"])), 1)
        self.assertIn("search: Unique", response.context["search_header"])

    def test_search_by_date_returns_results(self):
        today = timezone.now().date()
        response = self.client.get(reverse("post:search"), {"date": str(today)})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(list(response.context["posts"])), 1)

    def test_search_by_author_returns_results(self):
        response = self.client.get(reverse("post:search"), {"author": "author1"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(list(response.context["posts"])), 1)
        self.assertIn("search: author1", response.context["search_header"])

    def test_search_empty_query_redirects(self):
        response = self.client.get(reverse("post:search"))
        self.assertRedirects(response, reverse("post:index"))

    def test_search_no_match_returns_empty(self):
        response = self.client.get(reverse("post:search"), {"words": "nonexistent"})
        self.assertEqual(len(list(response.context["posts"])), 0)

    def test_search_htmx_returns_partial(self):
        response = self.client.get(
            reverse("post:search"),
            {"words": "Unique"},
            headers={"HX-Request": "true"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "post/post_list.html")

    def test_search_builds_correct_base_url(self):
        response = self.client.get(reverse("post:search"), {"words": "Unique"})
        self.assertEqual(response.context["base_url"], "/post/search/?words=Unique")

    def test_search_date_builds_correct_base_url(self):
        response = self.client.get(reverse("post:search"), {"date": "2026-07-29"})
        self.assertEqual(response.context["base_url"], "/post/search/?date=2026-07-29")

    def test_search_author_builds_correct_base_url(self):
        response = self.client.get(reverse("post:search"), {"author": "author1"})
        self.assertEqual(response.context["base_url"], "/post/search/?author=author1")


class CreatePostViewTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester", password="secret12345"
        )

    def test_create_get_requires_login(self):
        response = self.client.get(reverse("post:create"))
        self.assertRedirects(
            response,
            reverse("account:login") + "?next=" + reverse("post:create"),
        )

    def test_create_get_renders_form(self):
        self.client.login(username="tester", password="secret12345")
        response = self.client.get(reverse("post:create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "post/create.html")
        self.assertIsInstance(response.context["form"], BlogForm)

    def test_create_post_valid_data_creates_post(self):
        self.client.login(username="tester", password="secret12345")
        response = self.client.post(
            reverse("post:create"),
            {
                "title": "My Post",
                "content": "My content",
                "creation_date": "2026-07-29 12:00:00",
            },
        )
        self.assertRedirects(response, reverse("post:index"))
        self.assertEqual(BlogPost.objects.count(), 1)
        post = BlogPost.objects.first()
        self.assertEqual(post.author, self.user)

    def test_create_post_invalid_data_returns_form(self):
        self.client.login(username="tester", password="secret12345")
        response = self.client.post(
            reverse("post:create"),
            {"title": "", "content": "", "creation_date": ""},
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "post/create.html")
        self.assertFalse(response.context["form"].is_valid())


class PostDetailViewTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="author1")
        self.post = BlogPost.objects.create(
            title="Detail Post",
            content="Detail content",
            author=self.user,
            creation_date=timezone.now(),
        )

    def test_detail_existing_post_returns_200(self):
        response = self.client.get(reverse("post:detail", args=[self.post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "post/post_detail.html")

    def test_detail_shows_post_in_context(self):
        response = self.client.get(reverse("post:detail", args=[self.post.id]))
        self.assertEqual(response.context["post"], self.post)

    def test_detail_nonexistent_post_returns_404(self):
        response = self.client.get(reverse("post:detail", args=[9999]))
        self.assertEqual(response.status_code, 404)


class CalendarViewTests(TestCase):
    def test_calendar_returns_200(self):
        response = self.client.get(reverse("post:calendar", args=[2026, 7]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "components/calendar.html")

    def test_calendar_has_context(self):
        response = self.client.get(reverse("post:calendar", args=[2026, 7]))
        self.assertIn("calendar_html", response.context)
        self.assertEqual(response.context["year"], 2026)
        self.assertEqual(response.context["month"], 7)

    def test_calendar_with_day_param(self):
        response = self.client.get(reverse("post:calendar", args=[2026, 7]) + "?day=15")
        self.assertEqual(response.context["selected_day"], "15")

    def test_calendar_january_boundary(self):
        response = self.client.get(reverse("post:calendar", args=[2026, 1]))
        self.assertEqual(response.context["prev_year"], 2025)
        self.assertEqual(response.context["prev_month"], 12)

    def test_calendar_december_boundary(self):
        response = self.client.get(reverse("post:calendar", args=[2026, 12]))
        self.assertEqual(response.context["next_year"], 2027)
        self.assertEqual(response.context["next_month"], 1)


class AuthorsViewTests(TestCase):
    def setUp(self):
        for i in range(3):
            get_user_model().objects.create_user(username=f"author{i}")

    def test_authors_returns_200(self):
        response = self.client.get(reverse("post:authors"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "post/authors.html")

    def test_authors_has_authors_in_context(self):
        response = self.client.get(reverse("post:authors"))
        self.assertIn("authors", response.context)
        authors = list(response.context["authors"])
        self.assertEqual(len(authors), 3)

    def test_authors_htmx_returns_partial(self):
        response = self.client.get(
            reverse("post:authors"), headers={"HX-Request": "true"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "post/author_list.html")

    def test_authors_empty_list(self):
        get_user_model().objects.exclude(username__startswith="nonexistent").delete()
        get_user_model().objects.all().delete()
        response = self.client.get(reverse("post:authors"))
        self.assertEqual(len(list(response.context["authors"])), 0)
