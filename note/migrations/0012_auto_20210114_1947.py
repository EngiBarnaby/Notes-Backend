# Generated by Django 3.1.3 on 2021-01-14 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0011_auto_20210114_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='note.notecategory'),
        ),
    ]