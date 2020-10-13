from django.db import models
from django.urls import reverse
from ....General.Application.list_general import ListSizeCloth, ListTypesShirts
list_size = ListSizeCloth()
list_types_shirts = ListTypesShirts()


class Shirts(models.Model):
    ref = models.CharField(max_length=50, null=True,
                           blank=False, default="ref")
    size = models.CharField(max_length=10, null=False,
                            blank=False, choices=list_size, default=1)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    image = models.ImageField(
        upload_to='uniforms/shirts/%Y/%m/%d/', null=True)
    type = models.CharField(max_length=20, null=True,
                            blank=True, choices=list_types_shirts, default="")
    state = models.SmallIntegerField(default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Shirst Uniform {} id : {} Talla : {}, Precio : {}".format(
            self.type,
            self.id,
            self.size,
            self.price)

    def get_absolute_url(self):
        return reverse("confma:shirts_detail", kwargs={'_id': self.id})

    class Meta:
        db_table = "Shirts"
