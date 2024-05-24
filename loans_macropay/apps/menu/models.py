from django.db import models

# Create your models here.
class Menu(models.Model):
    external_id = models.IntegerField()
    icon =  models.CharField(max_length=100, null=True, blank=True)
    key_menu = models.CharField(max_length=100)
    link =  models.CharField(max_length=100, null=True, blank=True)
    order_menu = models.IntegerField(null=True, blank=True)
    parent_id = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=100)
    type_menu = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menu"