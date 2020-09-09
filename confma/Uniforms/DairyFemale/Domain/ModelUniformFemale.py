from django.db import models
from django.urls import reverse
from ....General.Application.list_general import ListSizeCloth, ListTypeUniform

list_size = ListSizeCloth()
list_type_uniform = ListTypeUniform()


class UniformsFemale(models.Model):
    name_college = models.CharField(max_length=100, null=False)
    models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=10000.00)
    state = models.SmallIntegerField(default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return"Uniforme del Colegio : {}, Precio : {}".format(self.name_college.self.price)

    def get_absolute_url(self):
        return reverse("confma:uniform_female_detail", kwargs={'_id': self.id})

    class Meta:
        db_table = "UniformsFemale"
