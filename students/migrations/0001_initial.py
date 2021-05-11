# Generated by Django 3.2 on 2021-05-10 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=256, verbose_name='Імʼя')),
                ('last_name', models.CharField(max_length=256, verbose_name='Прізвище')),
                ('middle_name', models.CharField(blank=True, default='', max_length=256, verbose_name='По-батькові')),
                ('birthday', models.DateField(null=True, verbose_name='Дата народження')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фото')),
                ('ticket', models.CharField(max_length=256, verbose_name='Білет')),
                ('notes', models.TextField(blank=True, verbose_name='Додаткові нотатки')),
            ],
        ),
    ]
