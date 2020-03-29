from django.db import models

class Menus(models.Model):
    BREAKFAST_MENU = 'BREAKFAST MENU'
    LUNCH_MENU = 'LUNCH MENU'
    SOUP_MENU = 'SOUP MENU'

    MENU_TITLES = [
        (BREAKFAST_MENU, 'BREAKFAST MENU'),
        (LUNCH_MENU, 'LUNCH MENU'),
        (SOUP_MENU, 'SOUP MENU')
    ]

    titles = models.CharField (
        max_length=150,
        choices=MENU_TITLES,
        default=SOUP_MENU
    )

    menu_items = models.CharField(max_length=120, default='added food or soup item here')
    menu_items_description = models.TextField(default='describe food or soup item here')

    SMALL_SOUP_PRICE = '$4.00'
    MEDIUM_SOUP_PRICE = '6.80'
    LARGE_SOUP_PRICE = '$12.06'

    SOUP_SIZE_PRICES = [
        (SMALL_SOUP_PRICE, '$4.00'),
        (MEDIUM_SOUP_PRICE, '$6.80'),
        (LARGE_SOUP_PRICE, '$12.06')
    ]

    soup_prices = models.CharField (
        null= True,
        blank=True,
        max_length=150,
        choices=SOUP_SIZE_PRICES,
        default=MEDIUM_SOUP_PRICE
    )

    all_food_but_soups_prices = models.DecimalField(null=True, blank=True, max_digits=4, decimal_places=2)


