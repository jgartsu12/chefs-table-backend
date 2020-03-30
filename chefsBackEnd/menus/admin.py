from django.contrib import admin

from .models import FoodMenus
from .models import SoupMenu

admin.site.register(FoodMenus)
admin.site.register(SoupMenu)