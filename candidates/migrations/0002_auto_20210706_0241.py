# Generated by Django 3.2.5 on 2021-07-05 23:41

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='technology',
        ),
        migrations.CreateModel(
            name='CanditateTechnologies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('knowledge_level', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Уровень знания)')),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='candidates.candidate', verbose_name='Кандидат')),
                ('technology', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='candidates.technology', verbose_name='Технология')),
            ],
        ),
        migrations.AddField(
            model_name='candidate',
            name='technologies',
            field=models.ManyToManyField(through='candidates.CanditateTechnologies', to='candidates.Technology'),
        ),
    ]
