from base.models import TimeStampMixin
from django.db import models


class Author(TimeStampMixin):
    """
    Модель автора блога.
    """
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    github_link = models.URLField(blank=True)
    resume_link = models.URLField(blank=True)

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

    def __str__(self) -> str:
        return f'Объект "Автор" (id={self.pk})'

    def fullname(self) -> str:
        """
        Формирование строки "Имя Фамилия".

        :return:
        """
        return self.first_name + " " + self.last_name
