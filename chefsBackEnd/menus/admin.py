from django.contrib import admin

from .models import LunchMenu
from .models import BreakfastMenu
from .models import SoupMenu

admin.site.register(LunchMenu)
admin.site.register(BreakfastMenu)
admin.site.register(SoupMenu)