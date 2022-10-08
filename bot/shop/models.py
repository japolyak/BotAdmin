from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Clients(models.Model):
    client_id = models.CharField(max_length=100, primary_key=True, verbose_name="TG identifikator")
    client_name = models.CharField(max_length=100, default="Human")
    client_number = models.CharField(max_length=100, default="+1234567890")
    client_address = models.CharField(max_length=100, default="Earth")

    def __str__(self):
        return self.client_name

    def get_absolute_url(self):
        return reverse('shop:show_id', kwargs={'client_id': self.client_id})

    class Meta:
        verbose_name = "Shop clients"
        verbose_name_plural = "Shop clients"
        ordering = ["client_name", ]


class Categories(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = "Shop category"
        verbose_name_plural = "Shop categories"


class Products(models.Model):
    product_name = models.TextField(default="Default product")
    price = models.IntegerField(default=0.0)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, db_column='category')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, null=True)

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse('shop:product_name', kwargs={'product_slug': self.slug})

    class Meta:
        verbose_name = "Shop product"
        verbose_name_plural = "Shop products"
        ordering = ["id", ]


class Clientcarts(models.Model):
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE, db_column='product_id')
    client_id = models.ForeignKey(Clients, on_delete=models.CASCADE, db_column='client_id')


class Cartmeta(models.Model):
    client_id = models.OneToOneField(Clients, on_delete=models.CASCADE, primary_key=True, db_column='client_id')
    patient_name = models.CharField(max_length=100, default="Mr/Mrs")
    deadline = models.DateField(default="2022-09-23")
    term_time = models.TimeField(default="10:10:10")
    description = models.TextField(default="no description")
    priority = models.BooleanField(default=False)


class Orders(models.Model):
    order_id = models.BigAutoField(auto_created=True, primary_key=True)
    client_id = models.ForeignKey(Clients, on_delete=models.CASCADE, db_column='client_id')
    patient_name = models.CharField(max_length=100)
    deadline = models.DateField()
    term_time = models.TimeField()
    description = models.TextField()
    priority = models.BooleanField()


class OrderedGoods(models.Model):
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE, db_column='order_id')
    product_id = models.OneToOneField(Products, on_delete=models.CASCADE, db_column='product_id')
    quantity = models.IntegerField()


class ShopUsers(models.Model):
    username = models.OneToOneField(User, to_field='username', on_delete=models.CASCADE, db_column='username')
    client_id = models.OneToOneField(Clients, on_delete=models.CASCADE, db_column='client_id')
