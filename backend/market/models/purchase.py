from django.db import models


class Purchase(models.Model):
    customer = models.CharField("customer", max_length=100)
    created = models.DateTimeField("created", auto_now_add=True, auto_now=False)

    class Meta:
        ordering = ("-pk",)
        verbose_name = "purchase"
        verbose_name_plural = "purchases"

    def __str__(self):
        return self.customer
