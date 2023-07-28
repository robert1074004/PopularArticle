from django.contrib.auth.models import User


def run():
    User.objects.create_user(username="admin1", password="your_password")
