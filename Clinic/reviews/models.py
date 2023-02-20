from django.db import models


class Reviews(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    review = models.TextField(verbose_name='Отзыв')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Отзывы'
        verbose_name = 'Отзыв'
        ordering = ['-created_on']
