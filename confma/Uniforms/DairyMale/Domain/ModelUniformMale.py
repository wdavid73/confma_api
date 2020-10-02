from django.db import models
from django.urls import reverse
from ...Pants.Domain.ModelPants import Pants
from ...Shirts.Domain.ModelShirts import Shirts
from ....Institution.Domain.Institution import Institution



class UniformsMale(models.Model):
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, blank=False, null=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, null=False,blank=True, default=0)
    pants = models.ForeignKey(Pants,on_delete=models.CASCADE,blank=False,null=False)
    shirt = models.ForeignKey(Shirts, on_delete=models.CASCADE, blank=False, null=False)
    state = models.SmallIntegerField(default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return"id {} , Precio : {}".format(self.id ,self.price)

    def get_absolute_url(self):
        return reverse("confma:uniform_male_detail", kwargs={'_id': self.id})

    class Meta:
        db_table = "UniformsMale"
