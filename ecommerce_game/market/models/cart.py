from django.db import models
from market.models.product import Product
from market.models.purchase import Purchase


class Cart(models.Model):
    purchase = models.ForeignKey(Purchase, related_name="purchases", on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name="products", on_delete=models.SET_NULL, null=True, blank=True
    )
    quantity = models.PositiveIntegerField("quantity")
    price = models.DecimalField("price", max_digits=6, decimal_places=2)

    class Meta:
        ordering = ("-pk",)
        verbose_name = "cart"
        verbose_name_plural = "carts"

    def __str__(self):
        if self.purchase:
            return f"{self.purchase.pk}-{self.pk}-{self.product}"
        return str(self.pk)

    def get_subtotal(self):
        return self.price * (self.quantity or 0)
