from django.db import models
from django.urls import reverse
from ....General.Application.list_general import ListSizeCloth, ListTypeUniform

list_size = ListSizeCloth()
list_type_uniform = ListTypeUniform()


class UniformsSports(models.Model):
    name_college = models.CharField(max_length=100, null=False)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    type_uniform = models.CharField(
        max_length=10, null=False, blank=False, choices=list_type_uniform, default=1)
    state = models.SmallIntegerField(default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return"Uniforme del Colegio : {}, Talla : {}".format(self.name_college, self.size)

    def get_absolute_url(self):
        return reverse("confma:uniform_sports_detail", kwargs={'_id': self.id})

    class Meta:
        db_table = "UniformsSports"
