from django.db import models

class News(models.Model):
	title = models.CharField(max_length=150, verbose_name='Заголовок')
	content = models.TextField(blank=True, verbose_name='Текст')
	created_at = models.DateTimeField(auto_now_add=True, verbose_name='Вреемя создания')
	updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
	photo = models.ImageField(upload_to='media/%y/%m/%d', verbose_name='Фото')
	is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

	class Meta:
		verbose_name='Новость'
		verbose_name_plural='Новости'
		ordering = ['-created_at']