from django.db import models


class Process(models.Model):
    topic = models.CharField('Why', max_length=125)
    basis = models.TextField('Description', max_length=10000)

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name = 'Name of process'
        verbose_name_plural = 'Process'
