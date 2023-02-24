from datetime import datetime

from django.utils import timezone
from django.test import TestCase

from jobs.models import Job


class JobTestCase(TestCase):
    """
    Тестирование функций работы.
    """

    def setUp(self) -> None:
        """
        Настройка перед тестированием.

        :return:
        """

        Job.objects.create(
            description="jobdescription",
            content="abdcefgh" * 100,
            image="Job №1 image path",
            publication_date=datetime(2023, 2, 24, tzinfo=timezone.utc),
        )

    def test_blog_messages_creation(self) -> None:
        """
        Тестирование моделей сообщений для работы.

        :return:
        """

        job = Job.objects.get(title="jobdescription")

        content = "abdcefgh" * 100
        self.assertEqual(job.summary(), content[:100] + "...")
        self.assertEqual(job.publication_date_format(), "Feb 24 2023")
        self.assertEqual(str(job), f'Объект "Выполненная работа" (id={job.pk})')