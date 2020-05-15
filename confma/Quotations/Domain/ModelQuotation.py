from django.db import models
from django.urls import reverse
from ...Clients.Domain.ModelClient import Client
from ...Cloths.Domain.ModelCloth import Cloth


class Quotation(models.Model):
    value_cloth = models.DecimalField(
        max_digits=9, decimal_places=2, null=False, blank=False)
    value_work = models.DecimalField(
        max_digits=9, decimal_places=2, null=False, blank=False)
    value_threads = models.DecimalField(
        max_digits=8, decimal_places=2, null=False, blank=False)
    value_buttons = models.DecimalField(
        max_digits=8, decimal_places=2, null=False, blank=False)
    value_necks = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=False, default=0)
    value_embroidery = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=False, default=0)
    value_prints = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=False, default=0)
    total = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True, default=0)
    cloth = models.ForeignKey(
        Cloth, on_delete=models.CASCADE, blank=False, null=False)
    client = models.ManyToManyField(Client, through="QuotationClient")
    state = models.SmallIntegerField(default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Value Cloth : {}, Value Work : {}, Value Threads : {}, Value Buttons : {}, Cloth : {}".format(
            self.value_cloth, self.value_work, self.value_threads, self.value_buttons, self.cloth)

    def get_absolute_url(self):
        return reverse("confma:quotation_detail", kwargs={'_id': self.id})

    class Meta:
        db_table = "Quotation"


class QuotationClient(models.Model):
    quotation = models.ForeignKey(Quotation, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE,
                               blank=False, null=False)
    state = models.SmallIntegerField(default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Quotation : {} , Client : {}".format(self.quotation,
                                                     self.client)

    def get_absolute_url(self):
        return reverse("confma:quotation_client_detail",
                       kwargs={'_id': self.id})

    class Meta:
        db_table = "Quotation_Client"

