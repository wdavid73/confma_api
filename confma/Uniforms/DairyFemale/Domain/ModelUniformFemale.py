from django.db import models
from django.urls import reverse
from ..Dresses.Domain.ModelDresses import DressesUniform
from ..Shirts.Domain.ModelShirtsFemale import ShirtsFemale

from ....General.Application.list_general import ListSizeCloth, ListTypeUniform


list_size = ListSizeCloth()
list_type_uniform = ListTypeUniform()


class UniformsFemale(models.Model):
    name_college = models.CharField(max_length=100, null=False)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    dress = models.ForeignKey(DressesUniform, on_delete=models.CASCADE, blank=False, null=False)
    shirt = models.ForeignKey(ShirtsFemale, on_delete=models.CASCADE, blank=False, null=False)
    state = models.SmallIntegerField(default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return"Uniforme del Colegio : {}, Precio : {}".format(self.name_college.self.price)

    def get_absolute_url(self):
        return reverse("confma:uniform_female_detail", kwargs={'_id': self.id})

    class Meta:
        db_table = "UniformsFemale"
