from django.db import models
from django.urls import reverse
from .....General.Application.list_general import ListSizeCloth, ListTypeUniform

list_size = ListSizeCloth()
list_type = ListTypeUniform()


class SweatShirt(models.Model):
    size = models.CharField(max_length=10, null=False,
                            blank=False, choices=list_size, default=1)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    image = models.ImageField(upload_to='uniforms/sports/sweatshirt/%Y/%m/%d/',null=True)
    state = models.SmallIntegerField(default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Shirst Uniform Male id : {} Talla : {},".format(
            self.id,
            self.size, )

    def get_absolute_url(self):
        return reverse("confma:sweatshirst_sport_detail", kwargs={'_id': self.id})

    class Meta:
        db_table = "SweatShirtsUniformSports"
