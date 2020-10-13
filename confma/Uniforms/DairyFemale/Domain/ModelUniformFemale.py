from django.db import models
from django.urls import reverse
from ...Shirts.Domain.ModelShirts import Shirts
from ...Dresses.Domain.ModelDresses import DressesUniform
from ...Pants.Domain.ModelPants import Pants
from ....Institution.Domain.Institution import Institution
from ....General.Application.list_general import ListSizeCloth

list_size = ListSizeCloth()


class UniformsFemale(models.Model):
    institution = models.ForeignKey(
        Institution, on_delete=models.CASCADE, blank=False, null=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    dress = models.ForeignKey(
        DressesUniform, on_delete=models.CASCADE, blank=True, null=True)
    shirt = models.ForeignKey(
        Shirts, on_delete=models.CASCADE, blank=True, null=True)
    #pants = models.ForeignKey(Pants, on_delete=models.CASCADE, blank=True, null=True)
    state = models.SmallIntegerField(default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "id {}, Precio : {}".format(self.id, self.price)

    def get_absolute_url(self):
        return reverse("confma:uniform_female_detail", kwargs={'_id': self.id})

    class Meta:
        db_table = "UniformsFemale"
