from django.db import models


class Link(models.Model):
    url = models.URLField(verbose_name='Ссылка')
    code = models.CharField(max_length=8, verbose_name='Код ссылки', unique=True)

    def __str__(self):
        return f'{self.url} - {self.code}'
