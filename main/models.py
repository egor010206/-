from django.db import models

class Product(models.Model):
    title = models.CharField("Название", max_length=255)
    description = models.TextField("Описание")
    price = models.PositiveIntegerField("Цена")
    image = models.ImageField("Изображение", upload_to="products/")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title