"""Student registered under the CCA"""

from datetime import date
from django.db import models


class Student(models.Model):
    """Student registered under the CCA"""
    name = models.CharField(
        max_length=100,
        default='',
    )

    email = models.CharField(
        max_length=100,
        blank=True,
        default='',
    )

    major = models.CharField(
        max_length=100,
        blank=True,
        default='',
    )

    registration_date = models.DateField(
        blank=True,
        default=date.today,
    )

    school = models.ForeignKey(
        'School',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    def __str__(self):
        # pylint: disable=no-member
        #
        # Referencing Django Foreign Key models via string breaks pylint
        # no-member checking
        #
        # https://github.com/PyCQA/pylint-django/issues/142
        # https://github.com/PyCQA/pylint-django/issues/106

        if self.school_id is not None:
            return f'[{self.school.school_abbr}] {self.name}'

        return self.name
