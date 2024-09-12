from django.db import models


class VideoRequest(models.Model):

    text = models.CharField(max_length=255, verbose_name='текст')
    video_file = models.FileField(upload_to='videos/', verbose_name='файл')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='создан')

    def __str__(self):
        return f"Video for: {self.text[:50]} (Created: {self.created_at})"

    class Meta:
        verbose_name = 'Запрос'
        verbose_name_plural = 'Запросы'
