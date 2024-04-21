from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re


def validate_year(year):
    if year<2000 or year>2050:
        raise ValidationError(
            ("%(year)s - неправильный год"),
            params={"year": year},
        )