from django.db import models

class FoodMenus(models.Model):
    BREAKFAST_MENU = 'BREAKFAST MENU'
    LUNCH_MENU = 'LUNCH MENU'

    FOOD_MENU_TITLES = [
        (BREAKFAST_MENU, 'BREAKFAST MENU'),
        (LUNCH_MENU, 'LUNCH MENU'),
    ]

    title = models.CharField (
        max_length=150,
        choices=FOOD_MENU_TITLES,
        default=BREAKFAST_MENU
    )

    name = models.CharField(max_length=120, default='Add items here')
    description = models.TextField(default='Add items here')
    prices = models.DecimalField(null=True, blank=True, max_digits=4, decimal_places=2)

    def __str__(self):
        return self

class SoupMenu(models.Model):
    SMALL_SOUP = 'Small'
    MEDIUM_SOUP = 'Medium'
    LARGE_SOUP = 'Large'

    SOUP_SIZES = [
        (SMALL_SOUP, 'Small'),
        (MEDIUM_SOUP, 'Medium'),
        (LARGE_SOUP, 'Large')
    ]

    soup_sizes = models.CharField (
        default='Select soup size',
        max_length=6,
        choices=SOUP_SIZES
    )

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

    soup_name = models.CharField(null=True, max_length=120, default='add soup name here')

    def __str__(self):
        return(self)

