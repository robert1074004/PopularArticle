import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PopularArticles.settings")
django.setup()

from django.contrib.auth.hashers import make_password

password = "your_password"

hashed_password = make_password(password)
print(hashed_password)
