from django.db import models
from ckeditor.fields import RichTextField


class Human(models.Model):
    title = models.CharField(verbose_name='Название органа', max_length=255)
    slug = models.SlugField(verbose_name='Ключ органа', max_length=255)
    img = models.ImageField(verbose_name='Изображение', upload_to='main/images/', blank=True, null=True)
    description = RichTextField(verbose_name='Описание', )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Орган'
        verbose_name_plural = 'Органы'
