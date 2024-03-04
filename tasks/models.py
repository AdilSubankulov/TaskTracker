
from django.db import models

class Task(models.Model):
    LOW = 'Низкий'
    MEDIUM = 'Средний'
    HIGH = 'Высокий'
    PRIORITY_CHOICES = [
        (LOW, 'Низкий'),
        (MEDIUM, 'Средний'),
        (HIGH, 'Высокий'),
    ]

    DONE = 'Выполнено'
    CANCELED = 'Отменено'
    POSTPONED = 'Отложено'
    STATUS_CHOICES = [
        (DONE, 'Выполнено'),
        (CANCELED, 'Отменено'),
        (POSTPONED, 'Отложено'),
    ]

    Задача = models.CharField(max_length=100)
    Приоритет = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default=LOW)
    Статус = models.CharField(max_length=20, choices=STATUS_CHOICES, default=DONE)

    def __str__(self):
        return self.title
