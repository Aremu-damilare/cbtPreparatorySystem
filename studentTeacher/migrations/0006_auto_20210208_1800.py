# Generated by Django 3.0.4 on 2021-02-08 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studentTeacher', '0005_auto_20210208_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentanswer',
            name='answer',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='studentTeacher.Answer'),
        ),
    ]
