from django.db import models

class Menus(models.Model):
    def __init__(self, titles):
        self.titles = titles

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