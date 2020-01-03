"""School registered under the CCA"""

from datetime import date
from django.core.validators import RegexValidator
from django.db import models
from ..constants import Region, Province
from .student import Student


class School(models.Model):
    """School registered under the CCA"""
    founding_date = models.DateField(
        blank=True,
        default=date.today,
    )

    school_name = models.CharField(
        max_length=100,
    )

    school_abbr = models.CharField(
        max_length=8,
    )

    region = models.CharField(
        max_length=10,
        choices=Region.choices,
    )

    province = models.CharField(
        max_length=100,
        choices=Province.choices,
    )

    color_primary = models.CharField(
        max_length=7,
        null=True,
        blank=True,
        validators=[
            RegexValidator(
                regex='^#[0-9A-F]{6}$',
                message='Invalid HEX color code',
            ),
        ],
    )

    color_secondary = models.CharField(
        max_length=7,
        null=True,
        blank=True,
        validators=[
            RegexValidator(
                regex='^#[0-9A-F]{6}$',
                message='Invalid HEX color code',
            ),
        ],
    )

    color_primary_alternate = models.CharField(
        max_length=7,
        null=True,
        blank=True,
        validators=[
            RegexValidator(
                regex='^#[0-9A-F]{6}$',
                message='Invalid HEX color code',
            ),
        ],
    )

    color_secondary_alternate = models.CharField(
        max_length=7,
        null=True,
        blank=True,
        validators=[
            RegexValidator(
                regex='^#[0-9A-F]{6}$',
                message='Invalid HEX color code',
            ),
        ],
    )

    president = models.ForeignKey(
        Student,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    def __str__(self):
        return self.school_name
