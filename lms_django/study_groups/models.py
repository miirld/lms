from django.db import models
from .validators import validate_year



class School(models.Model):
    full_name = models.CharField(
        max_length=255, verbose_name='Полное наименование')
    short_name = models.CharField(
        max_length=255, verbose_name='Короткое наименование')
    address = models.CharField(max_length=255, verbose_name='Адрес')

    def __str__(self):
        return self.short_name

    class Meta:
        verbose_name = 'Школа'
        verbose_name_plural = 'Школы'


class StudyGroup(models.Model):

    GRADE_CHOICES = (
        (10, 10),
        (11, 11)
    )

    LETTER_CHOICES = (
        ('А', 'А'), ('Б', 'Б'), ('В', 'В'), ('Г', 'Г'),
        ('Д', 'Д'), ('Е', 'Е'), ('Ё', 'Ё'), ('Ж', 'Ж'),
        ('З', 'З'), ('И', 'И'), ('Й', 'Й'), ('К', 'К'),
        ('Л', 'Л'), ('М', 'М'), ('Н', 'Н'), ('О', 'О'),
        ('П', 'П'), ('Р', 'Р'), ('С', 'С'), ('Т', 'Т'),
        ('У', 'У'), ('Ф', 'Ф'), ('Х', 'Х'), ('Ц', 'Ц'),
        ('Ч', 'Ч'), ('Ш', 'Ш'), ('Щ', 'Щ'), ('Ы', 'Ы'),
        ('Э', 'Э'), ('Ю', 'Ю'), ('Я', 'Я')
    )



    grade = models.IntegerField(choices=GRADE_CHOICES, verbose_name='Класс')
    letter = models.CharField(
        max_length=1, choices=LETTER_CHOICES, verbose_name='Литера')
    school = models.ForeignKey(
        School, related_name='study_groups', verbose_name='Школа', on_delete=models.CASCADE)
    entrance_year = models.IntegerField(
        verbose_name='Год поступления', validators=[validate_year])
    graduation_year = models.IntegerField(
        verbose_name='Год выпуска', validators=[validate_year])
    is_active = models.BooleanField(verbose_name='Активен', default=False)

    def __str__(self):
        return f"{self.grade}{self.letter} ({self.entrance_year}-{self.graduation_year}) {self.school.short_name}"

    class Meta:
        unique_together = ('grade', 'letter', 'school',
                           'entrance_year', 'graduation_year')
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'
