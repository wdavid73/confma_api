from django.db import models
from django.db.models import DateField
from django.urls import reverse

list_size = [
    ('XS', 'XS'),
    ('S', 'S'),
    ('M', 'M'),
    ('L', 'L'),
    ('XL', 'XL'),
    ('XXL', 'XXL'),
]


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
        return "{} {} , {}".format(self.name, self.last_name, self.cellphone)

    def get_absolute_url(self):
        return reverse("confma:client_detail", kwargs={'_id': self.id})

    class Meta:
        db_table="Client"


class Cloth(models.Model):
    name=models.CharField(max_length=100, null=False)
    color=models.CharField(max_length=100, null=False)
    size=models.CharField(max_length=10, null=False,
                          blank=False, choices=list_size, default=1)
    fashion=models.CharField(max_length=50, null=False)
    image=models.ImageField(upload_to='fashion/%Y/%m/%d/')
    state=models.SmallIntegerField(default=1, null=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} Talla : {}, Color : {}, Moda : {}".format(self.name, self.size, self.color, self.fashion)

    def get_absolute_url(self):
        return reverse("confma:cloth_detail", kwargs={'_id': self.id})

    class Meta:
        db_table="Cloth"


class Quotation(models.Model):
    value_cloth=models.DecimalField(
        max_digits=9, decimal_places=2, null=False, blank=False)
    value_work=models.DecimalField(
        max_digits=9, decimal_places=2, null=False, blank=False)
    value_threads=models.DecimalField(
        max_digits=8, decimal_places=2, null=False, blank=False)
    value_buttons=models.DecimalField(
        max_digits=8, decimal_places=2, null=False, blank=False)
    value_necks=models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=False)
    value_embroidery=models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=False)
    value_prints=models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=False)
    cloth=models.ForeignKey(
        Cloth, on_delete=models.CASCADE, blank=False, null=False)
    client=models.ManyToManyField(Client, through="QuotationClient")
    state=models.SmallIntegerField(default=1, null=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Value Cloth : {}, Value Work : {}, Value Threads : {}, Value Buttons : {}, Cloth : {}".format(self.value_cloth, self.value_work, self.value_threads, self.value_buttons, self.cloth)

    def get_absolute_url(self):
        return reverse("confma:quotation_detail", kwargs={'_id': self.id})

    class Meta:
        db_table="Quotation"


class QuotationClient(models.Model):
    quotation=models.ForeignKey(Quotation, on_delete=models.CASCADE)
    client=models.ForeignKey(
        Client, on_delete=models.CASCADE, blank=False, null=False)
    total=models.BigIntegerField()
    state=models.SmallIntegerField(default=1, null=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Quotation : {} , Client : {}, Total : ${}".format(self.quotation, self.client, self.total)

    def get_absolute_url(self):
        return reverse("confma:quotation_client_detail", kwargs={'_id': self.id})

    class Meta:
        db_table="Quotation_Client"


class Rental(models.Model):
    date_now: DateField=models.DateField(auto_now_add=True)  # [YYYY-MM-DD]
    date_return=models.DateField()  # [YYYY-MM-DD]
    price=models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=5000.00)
    cloth=models.ForeignKey(
        Cloth, on_delete=models.CASCADE, blank=False, null=False)
    client=models.ForeignKey(
        Client, on_delete=models.CASCADE, blank=False, null=False)
    ifrental=models.SmallIntegerField(default=1, null=False, blank=False)
    state=models.SmallIntegerField(default=1, null=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Date Now :{} , Date Return : {} , Price : {} , Client : {} , Cloth : {}" \
            .format(self.date_now, self.date_now, self.price, self.client, self.cloth)

    def get_absolute_url(self):
        return reverse("confma:rental_detail", kwargs={'_id': self.id})

    class Meta:
        db_table="Rental"
