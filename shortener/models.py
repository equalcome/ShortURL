from django.conf import settings
from django.db import models
import string
import secrets


def _gen_code(length=6):
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))


class ShortURL(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, related_name='short_urls')
    original_url = models.URLField()
    short_code = models.CharField(
        max_length=10, unique=True, db_index=True, blank=True)
    click_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # 若沒指定 short_code，幫忙產生且保證唯一
        if not self.short_code:
            code = _gen_code(6)
            while ShortURL.objects.filter(short_code=code).exists():
                code = _gen_code(6)
            self.short_code = code
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.short_code} -> {self.original_url}"

    def get_absolute_url(self):
        # 之後在 template 用它來組短網址
        return f"/{self.short_code}/"


class ClickRecord(models.Model):
    short_url = models.ForeignKey(
        ShortURL, on_delete=models.CASCADE, related_name='clicks')
    ip_address = models.GenericIPAddressField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ip_address} @ {self.created_at}"
