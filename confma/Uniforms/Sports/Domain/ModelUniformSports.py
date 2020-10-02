from django.db import models
from django.urls import reverse
from ...Shirts.Domain.ModelShirts import Shirts
from ...Pants.Domain.ModelPants import Pants
from ....General.Application.list_general import ListTypeUniform
from ....Institution.Domain.Institution import Institution
list_type_uniform = ListTypeUniform()

class UniformsSports(models.Model):
    institution = models.ForeignKey(Institution,on_delete=models.CASCADE,blank=False,null=True)
    type_uniform = models.CharField(
        max_length=10, null=False, blank=False, choices=list_type_uniform, default=1)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    shirt = models.ForeignKey(
        Shirts, on_delete=models.CASCADE, blank=False, null=False)
    pants = models.ForeignKey(
        Pants, on_delete=models.CASCADE, blank=False, null=True)
    state = models.SmallIntegerField(default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return"id : {}, Tipo : {}".format(self.id, self.type_uniform)

    def get_absolute_url(self):
        return reverse("confma:uniform_sports_detail", kwargs={'_id': self.id})

    class Meta:
        db_table = "UniformsSports"
