from django.db import models

class LunchMenu(models.Model):
    title = models.CharField(max_length=150, default='Lunch Menu')
    name = models.CharField(max_length=120, default='Add items here')
    description = models.TextField(default='Add items here')
    front_thumb_img_url = models.ImageField(default='Upload image', upload_to='images/')

    def __str__(self):
        return self.title

class BreakfastMenu(models.Model):
    title = models.CharField(max_length=150, default='Breakfast Menu')
    name = models.CharField(max_length=120, default='Add items here')
    description = models.TextField(default='Add items here')
    front_thumb_img_url = models.ImageField(default='Upload image', upload_to='images/')

    def __str__(self):
        return self.title

class SoupMenu(models.Model):
    title = models.CharField(max_length=150, default='Soup Menu')
    name = models.CharField(null=True, max_length=120, default='add soup name here')
    description = models.TextField(default='Describe soup here')
    front_thumb_img_url = models.ImageField(default='Upload image', upload_to='images/')
   
    def __str__(self):
        return self.title
