# Generated by Django 2.1.2 on 2019-01-16 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20190116_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice_question',
            name='show_time',
            field=models.DateField(verbose_name='题目出现时间(月-日的形式：如12-18)'),
        ),
        migrations.AlterField(
            model_name='outside_reading',
            name='show_time',
            field=models.DateField(verbose_name='题目出现时间(12-18)'),
        ),
    ]
