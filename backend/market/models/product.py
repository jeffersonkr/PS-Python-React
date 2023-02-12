from django.db import models


class Product(models.Model):
    name = models.CharField("name", max_length=100, unique=True)
    price = models.DecimalField("price", max_digits=6, decimal_places=2)
    score = models.IntegerField("score", default=0)
    image = models.CharField("image", max_length=255, default="")

    class Meta:
        ordering = ("name",)
        verbose_name = "product"
        verbose_name_plural = "products"

    def __str__(self):
        return self.name

    def to_dict(self):
        return {"value": self.pk, "text": self.name, "price": self.price}
