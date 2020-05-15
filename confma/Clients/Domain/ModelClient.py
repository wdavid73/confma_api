from django.db import models
from django.db.models import DateField
from django.urls import reverse


class Client(models.Model):
    name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=200, null=False)
    address = models.CharField(max_length=100, null=True)
    phone = models.IntegerField(null=True)
    cellphone = models.BigIntegerField(null=False)
    state = models.SmallIntegerField(default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "id: {}, {} {} , {}".format(self.id, self.name,
                                           self.last_name,
                                           self.cellphone)

    def get_absolute_url(self):
        return reverse("confma:client_detail", kwargs={'_id': self.id})

    class Meta:
        db_table = "Client"
