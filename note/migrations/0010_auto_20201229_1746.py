# Generated by Django 3.1.3 on 2020-12-29 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0009_auto_20201229_1746'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notecategory',
            options={'ordering': ['-created']},
        ),
    ]