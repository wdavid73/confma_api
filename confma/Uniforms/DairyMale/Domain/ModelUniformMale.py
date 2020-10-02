from django.db import models
from django.urls import reverse
from ..Pants.Domain.ModelPantsMale import PantsMale
from ..Shirts.Domain.ModelShirtsMale import ShirtsMale



class UniformsMale(models.Model):
    name_college = models.CharField(max_length=100, null=False)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, null=False,blank=True, default=0)
    pants = models.ForeignKey(PantsMale,on_delete=models.CASCADE,blank=False,null=False)
    shirt = models.ForeignKey(ShirtsMale, on_delete=models.CASCADE, blank=False, null=False)
    state = models.SmallIntegerField(default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return"Uniforme del Colegio : {}, Precio : {}".format(self.name_college,self.price)

    def get_absolute_url(self):
        return reverse("confma:uniform_male_detail", kwargs={'_id': self.id})

    class Meta:
        db_table = "UniformsMale"
