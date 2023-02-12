from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Purchase(models.Model):
    customer = models.ForeignKey(User, related_name="user", on_delete=models.DO_NOTHING)
    created = models.DateTimeField("created", auto_now_add=True, auto_now=False)

    class Meta:
        ordering = ("-pk",)
        verbose_name = "purchase"
        verbose_name_plural = "purchases"

    def __str__(self):
        return self.customer
