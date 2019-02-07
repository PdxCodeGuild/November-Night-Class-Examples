import string
import random

from django.db import models

class ShortURL(models.Model):
    code = models.CharField(max_length=7, primary_key=True, editable=False)
    url = models.URLField(max_length=2048)

    def generate_code(self):
        self.code = ''.join(
            [
                random.choice(string.ascii_letters + string.digits)
                for _ in range(7)
            ]
        )