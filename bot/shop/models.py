from django.db import models


class Clients(models.Model):
    client_id = models.CharField(max_length=100, primary_key=True)
    client_name = models.CharField(max_length=100, default="Human")
    client_number = models.CharField(max_length=100, default="+1234567890")
    client_address = models.CharField(max_length=100, default="Earth")

    def __str__(self):
        return self.client_name


class Products(models.Model):
    product_name = models.TextField(default="Default product")
    price = models.IntegerField(default=0.0)
    category = models.CharField(max_length=100, default="Others")


class Clientcarts(models.Model):
    product_id = models.CharField(max_length=100)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)


class Cartmeta(models.Model):
    client_id = models.CharField(max_length=100, primary_key=True)
    patient_name = models.CharField(max_length=100, default="Mr/Mrs")
    deadline = models.DateField(default="2022-09-23")
    term_time = models.TimeField(default="10:10:10")
    description = models.TextField(default="no description")
    priority = models.BooleanField(default=False)


class Orders(models.Model):
    order_id = models.BigAutoField(auto_created=True, primary_key=True)
    client_id = models.CharField(max_length=100)
    patient_name = models.CharField(max_length=100)
    deadline = models.DateField()
    term_time = models.TimeField()
    description = models.TextField()
    priority = models.BooleanField()


class OrderedGoods(models.Model):
    order_id = models.CharField(max_length=100)
    product_id = models.CharField(max_length=100)
    quantity = models.IntegerField()
