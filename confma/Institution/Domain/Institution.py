from django.db import models
from django.urls import reverse


class Institution(models.Model):
    name = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=200, null=False)
    state = models.SmallIntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - contact information {} - {}".format(self.name, self.phone, self.address)

    def get_absolute_url(self):
        return reverse('confma:institution_detail', kwargs={'_id': self.id})

    class Meta:
        db_table = 'Institution'
