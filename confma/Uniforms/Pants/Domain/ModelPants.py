from django.db import models
from django.urls import reverse
from ....General.Application.list_general import ListSizeCloth, ListTypesPants
list_size = ListSizeCloth()
list_types_pants = ListTypesPants()


class Pants(models.Model):
    ref = models.CharField(max_length=10, null=True,
                           blank=False, default="ref")
    size = models.CharField(max_length=10, null=False,
                            blank=False, choices=list_size, default=1)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    image = models.ImageField(
        upload_to='uniforms/Male/pants/%Y/%m/%d/', null=True)
    type = models.CharField(max_length=10, null=True,
                            blank=True, choices=list_types_pants,default=1)
    state = models.SmallIntegerField(default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Pants Uniform {} id : {} Talla : {}, Precio : {}".format(
            self.type,
            self.id,
            self.size,
            self.price,)

    def get_absolute_url(self):
        return reverse("confma:pants_male_detail", kwargs={'_id': self.id})

    class Meta:
        db_table = "Pants"
