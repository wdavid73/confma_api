from django.db import models
from django.urls import reverse
from ....General.Application.list_general import ListTypeUniform
from ..Shirts.Domain.ModelShirtsSports import ShirtsSports
from ..SweatShirt.Domain.ModelSweatShirt import SweatShirt
list_type_uniform = ListTypeUniform()


class UniformsSports(models.Model):
    name_college = models.CharField(max_length=100, null=False)
    type_uniform = models.CharField(
        max_length=10, null=False, blank=False, choices=list_type_uniform, default=1)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    shirt = models.ForeignKey(ShirtsSports, on_delete=models.CASCADE, blank=False, null=False)
    sweat_shirt = models.ForeignKey(SweatShirt, on_delete=models.CASCADE, blank=False, null=False)
    state = models.SmallIntegerField(default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return"Uniforme del Colegio : {}, Tipo : {}".format(self.name_college, self.type_uniform)

    def get_absolute_url(self):
        return reverse("confma:uniform_sports_detail", kwargs={'_id': self.id})

    class Meta:
        db_table = "UniformsSports"
