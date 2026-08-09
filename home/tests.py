from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class LoginViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="stockmanager",
            password="safe-test-password",
        )

    def test_login_page_renders(self):
        response = self.client.get(reverse("home:login"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/login.html")
        self.assertContains(response, "Welcome back")

    def test_valid_login_redirects_to_dashboard(self):
        response = self.client.post(
            reverse("home:login"),
            {"username": "stockmanager", "password": "safe-test-password"},
        )

        self.assertRedirects(response, reverse("home:dashboard"))
        self.assertEqual(int(self.client.session["_auth_user_id"]), self.user.pk)

    def test_invalid_login_shows_an_error(self):
        response = self.client.post(
            reverse("home:login"),
            {"username": "stockmanager", "password": "incorrect"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Please enter a correct username and password")

    def test_external_next_url_is_not_followed(self):
        response = self.client.post(
            reverse("home:login"),
            {
                "username": "stockmanager",
                "password": "safe-test-password",
                "next": "https://example.com/phishing",
            },
        )

        self.assertRedirects(response, reverse("home:dashboard"))