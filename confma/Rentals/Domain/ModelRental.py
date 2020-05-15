from django.db import models
from django.db.models import DateField
from django.urls import reverse
from ...Clients.Domain.ModelClient import Client
from ...Cloths.Domain.ModelCloth import Cloth


class Rental(models.Model):
    date_now: DateField = models.DateField(
        auto_now_add=True)  # [YYYY-MM-DD]
    date_return = models.DateField()  # [YYYY-MM-DD]
    price = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=5000.00)
    cloth = models.ForeignKey(
        Cloth, on_delete=models.CASCADE, blank=False, null=False)
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, blank=False, null=False)
    ifrental = models.SmallIntegerField(default=1, null=False,
                                        blank=False)
    state = models.SmallIntegerField(default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Date Now :{} , Date Return : {} , Price : {} , Client : {} , Cloth : {}" \
            .format(self.date_now, self.date_now, self.price,
                    self.client, self.cloth)

    def get_absolute_url(self):
        return reverse("confma:rental_detail", kwargs={'_id': self.id})

    class Meta:
        db_table = "Rental"
