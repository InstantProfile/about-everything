from django.db import models


class WorkEntry(models.Model):
    job_title = models.CharField(max_length=255, verbose_name="Название вида работы")
    hours_worked = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Количество отработанных часов")
    comment = models.TextField(blank=True, verbose_name="Комментарий")
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(verbose_name="Дата")

    def __str__(self):
        return f"{self.job_title} - {self.hours_worked} часов"

    class Meta:
        verbose_name = "Запись о работе"
        verbose_name_plural = "Записи о работе"
