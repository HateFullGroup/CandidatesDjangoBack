from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
from datetime import datetime

from django.db.models import F, Q
from django.urls import reverse
Q

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
    # technologies = models.ManyToManyField('Technology', through='CandidateTechnology', related_name='list_technologies')

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

    def get_technologies(self):
        # candidate = Candidate.objects.filter(id=self.id)\
        #     .prefetch_related('candidatetechnology_set', 'technology_set').first()
        technologies = self.technology_set.all().prefetch_related('candidatetechnology_set')
        candidate_technologies = self.candidatetechnology_set.all()
        return {t.name: ct.knowledge_level for (t, ct) in zip(technologies, candidate_technologies)}

    # def get_technologies(self):
    #     return CandidateTechnology.objects.filter(pk=F('candidate_id'))

    # prefetch_related("technology")


class Technology(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя', null=False, unique=True)
    technologies = models.ManyToManyField('Candidate', through='CandidateTechnology')
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('technology', kwargs={"id": self.id})

    class Meta:
        ordering = ['name']
        verbose_name = 'Технология'
        verbose_name_plural = 'Технологии'


class CandidateTechnology(models.Model):
    candidate = models.ForeignKey('Candidate', on_delete=models.CASCADE, verbose_name='Кандидат', blank=True)
    technology = models.ForeignKey('Technology', on_delete=models.CASCADE, verbose_name='Технология')
    knowledge_level = models.IntegerField(default=1, validators=[MinValueValidator(1),
                                                                 MaxValueValidator(5)],
                                          verbose_name='Уровень знания', blank=False)

    class Meta:
        unique_together = [['candidate', 'technology']]
        verbose_name = 'Кандидат-технология'
        verbose_name_plural = 'Кандидаты-технологии'
        ordering = ['id']

