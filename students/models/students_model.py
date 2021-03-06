from django.db import models


class Student(models.Model):
    """Student Model"""
    first_name = models.CharField(
        max_length=256, blank=False, verbose_name="Імʼя"
    )
    last_name = models.CharField(
        max_length=256, blank=False, verbose_name="Прізвище"
    )
    middle_name = models.CharField(
        max_length=256, blank=True, verbose_name="По-батькові", default=''
    )
    birthday = models.DateField(
        blank=False, verbose_name="Дата народження", null=True
    )
    photo = models.ImageField(
        blank=True, verbose_name="Фото", null=True
    )
    ticket = models.CharField(
        max_length=256, blank=False, verbose_name="Білет"
    )
    student_group = models.ForeignKey(
        'Group', verbose_name="Група", blank=False, null=True, on_delete=models.PROTECT
    )
    notes = models.TextField(
        blank=True, verbose_name="Додаткові нотатки"
    )

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенти"

    def __str__(self):
        """Return first_name last_name"""
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.strip()