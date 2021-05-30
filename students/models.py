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


class Group(models.Model):
    """Group Model"""
    title = models.CharField(
        max_length=256, verbose_name="Назва"
    )
    leader = models.OneToOneField(
        'Student', verbose_name="Староста", blank=True, null=True, on_delete=models.SET_NULL
    )
    notes = models.TextField(
        blank=True, verbose_name="Додаткові нотатки"
    )

    class Meta:
        verbose_name = "Група"
        verbose_name_plural = "Групи"

    def __str__(self):
        if self.leader:
            return f"{self.title} ({self.leader.first_name}{self.leader.last_name})"
        else:
            return f"{self.title}"
