# Generated by Django 3.1.3 on 2021-02-22 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_step_sub_step'),
    ]

    operations = [
        migrations.RenameField(
            model_name='step',
            old_name='sub_step',
            new_name='parent',
        ),
    ]
