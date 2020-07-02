from django.db import models
from django.urls import reverse

list_size = [
    ('XS', 'XS'),
    ('S', 'S'),
    ('M', 'M'),
    ('L', 'L'),
    ('XL', 'XL'),
    ('XXL', 'XXL'),
]


class Cloth(models.Model):
    name = models.CharField(max_length=100, null=False)
    color = models.CharField(max_length=100, null=False)
    size = models.CharField(max_length=10, null=False,
                            blank=False, choices=list_size, default=1)
    fashion = models.CharField(max_length=50, null=False)
    image = models.ImageField(upload_to='fashion/%Y/%m/%d/')
    state = models.SmallIntegerField(default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} Talla : {}, Color : {}, Moda : {} ,".format(self.name,
                                                             self.size,
                                                             self.color,
                                                             self.fashion)

    def get_absolute_url(self):
        return reverse("confma:cloth_detail", kwargs={'_id': self.id})

    class Meta:
        db_table = "Cloth"
