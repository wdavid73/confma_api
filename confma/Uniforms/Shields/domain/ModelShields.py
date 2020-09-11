from django.db import models
from django.urls import reverse


class Shields(models.Model):
    name_college = models.CharField(max_length=100, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    image = models.ImageField(upload_to='uniforms/shields/%Y/%m/%d/',null=True)
    state = models.SmallIntegerField(default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Escudo del Colegio : {}, Precio : {}".format(self.name_college,self.price)

    def get_absolute_url(self):
        return reverse("confma:shields_detail", kwargs={'_id': self.id})

    class Meta:
        db_table = "Shields"
