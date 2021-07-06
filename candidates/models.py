from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
from datetime import datetime

from django.urls import reverse


class Candidate(models.Model):
    # auto_now_add=True, ?
    phone_number = models.CharField(max_length=255, verbose_name='Телефон')
    f_i_o = models.CharField(max_length=255, verbose_name='ФИО', null=False)
    birth_date = models.DateTimeField(verbose_name='Дата рождения', null=False)
    added_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    description = models.CharField(max_length=255, verbose_name='Описание', null=False)
    feedback = models.CharField(max_length=255, verbose_name='Отзыв', null=False)
    place_of_employment = models.CharField(max_length=255, verbose_name='Место работы', null=False)
    salary = models.IntegerField(default=0)
    job_position = models.CharField(max_length=255, verbose_name='Должность', null=False)
    technologies = models.ManyToManyField('Technology', through='CandidateTechnology')
    # candidate_technologies = models.ForeignKey('CandidateTechnology', on_delete=models.PROTECT(), related_name='candidate_technology')
    # technology = models.ManyToManyField('Technology')

    class Meta:
        ordering = ['f_i_o']
        verbose_name = 'Кандидат'
        verbose_name_plural = 'Кандидаты'

    def __str__(self):
        return self.f_i_o

    def get_absolute_url(self):
        return reverse('candidate', kwargs={"id": self.id})


class Technology(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя', null=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('technology', kwargs={"id": self.id})

    class Meta:
        ordering = ['name']
        verbose_name = 'Технология'
        verbose_name_plural = 'Технологии'


class CandidateTechnology(models.Model):
    candidate = models.ForeignKey('Candidate', on_delete=models.PROTECT, verbose_name='Кандидат')
    technology = models.ForeignKey('Technology', on_delete=models.PROTECT, verbose_name='Технология')
    knowledge_level = models.IntegerField(default=1, validators=[MinValueValidator(1),
                                                                 MaxValueValidator(5)],
                                          verbose_name='Уровень знания')
    class Meta:
        unique_together = [['candidate', 'technology']]
        verbose_name = 'Кандидат-технология'
        verbose_name_plural = 'Кандидаты-технологии'

