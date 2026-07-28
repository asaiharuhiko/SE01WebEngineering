from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .forms import UserAccountCreateForm, UserAccountLoginForm


class AccountViewsTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester",
            password="secret12345",
        )

    def test_login_get_renders_login_form(self):
        response = self.client.get(reverse("account:login"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "account/login.html")
        self.assertIsInstance(response.context["form"], UserAccountLoginForm)

    def test_login_post_with_valid_credentials_redirects_and_logs_in(self):
        response = self.client.post(
            reverse("account:login"),
            {"username": "tester", "password": "secret12345"},
        )

        self.assertRedirects(response, reverse("post:index"))
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_login_post_with_invalid_credentials_returns_form_errors(self):
        response = self.client.post(
            reverse("account:login"),
            {"username": "tester", "password": "wrong-password"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "account/login.html")
        self.assertFalse(response.wsgi_request.user.is_authenticated)
        self.assertIn("__all__", response.context["form"].errors)

    def test_create_get_renders_create_form(self):
        response = self.client.get(reverse("account:create"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "account/create.html")
        self.assertIsInstance(response.context["form"], UserAccountCreateForm)

    def test_create_post_with_valid_data_creates_user_and_logs_in(self):
        response = self.client.post(
            reverse("account:create"),
            {
                "username": "newuser",
                "password1": "StrongPass123!",
                "password2": "StrongPass123!",
            },
        )

        self.assertRedirects(response, reverse("post:index"))
        self.assertTrue(get_user_model().objects.filter(username="newuser").exists())
        self.assertTrue(response.wsgi_request.user.is_authenticated)
        self.assertEqual(response.wsgi_request.user.username, "newuser")

    def test_logout_get_renders_logout_template(self):
        response = self.client.get(reverse("account:logout"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "account/logout.html")

    def test_logout_post_logs_user_out(self):
        self.client.login(username="tester", password="secret12345")

        response = self.client.post(reverse("account:logout"))

        self.assertRedirects(response, reverse("post:index"))
        self.assertFalse(response.wsgi_request.user.is_authenticated)

    def test_information_requires_login(self):
        response = self.client.get(reverse("account:information"))

        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse("account:login"), response.url)

    def test_information_displays_current_user(self):
        self.client.login(username="tester", password="secret12345")

        response = self.client.get(reverse("account:information"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "account/info.html")
        self.assertEqual(response.context["account"], self.user)
