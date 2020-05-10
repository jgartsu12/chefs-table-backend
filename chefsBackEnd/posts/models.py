from django.db import models

class Posts(models.Model):
    phlog_title = models.CharField(default='Provide image a title', blank=True, max_length=150)
    phlog_description = models.TextField(blank=True, default='Write brief description here...')
    phlog_image_url = models.ImageField(upload_to='images/')
    position = models.CharField(default='provide position number', blank=True, max_length=150)

    DRAFT = 'Draft'
    PUBLISHED = 'Published'

    PHLOG_STATUS_CATEGORIES = [
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published')
    ]

    phlog_status = models.CharField (
        max_length=10,
        choices=PHLOG_STATUS_CATEGORIES,
        default=DRAFT
    )

    def __str__(self):
         return self.phlog_title
