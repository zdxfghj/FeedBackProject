# Generated by Django 5.0.6 on 2024-05-15 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='email',
            field=models.EmailField(default=1, max_length=254, verbose_name='E-mail'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='feedback',
            name='contact_info',
            field=models.TextField(default=1, verbose_name='Контактные данные для связи'),
            preserve_default=False,
        ),
    ]
