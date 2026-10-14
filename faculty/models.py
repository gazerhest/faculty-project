from django.db import models
from django.utils import timezone

class FacultyInfo(models.Model):
    title = models.CharField(
        max_length=199,
        default="Факультет Гуманітарних Наук",
    )
    description = models.TextField()
    dean = models.CharField(max_length=147)
    vice_dean = models.CharField(max_length=154)
    address = models.CharField(max_length=213)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=156)
    office_hours = models.CharField(max_length=99)

    def __str__(self):
        return self.title


class Department(models.Model):
    name = models.CharField(max_length=200)
    boss = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Program(models.Model):
    name = models.CharField(max_length=147)
    code = models.CharField(max_length=20)
    description = models.TextField()
    coordinator_name = models.CharField(max_length=153)
    coordinator_contact = models.CharField(max_length=100)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="programs"
    )
    disciplines = models.TextField(
        help_text="Введіть перелік дисциплін (через кому)"
    )

    def __str__(self):
        return f"{self.code}: {self.name}"

    def short_description(self):
        words = self.description.split()
        if len(words) > 50:
            return " ".join(words[:50]) + '...'
        return self.description


class Teacher(models.Model):
    name = models.CharField(max_length=150)
    position = models.CharField(max_length=150)
    degree = models.CharField(max_length=150)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="teachers"
    )

    def __str__(self):
        return f"{self.name} ({self.position})"

class ExchangeProgram(models.Model):
    university_name = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    languages = models.CharField(max_length=255)
    slots = models.PositiveIntegerField()
    deadline = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"{self.university_name} ({self.country})"

    @property
    def is_open(self):
        return timezone.localdate() <= self.deadline
