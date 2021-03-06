# Generated by Django 3.1.3 on 2021-01-30 22:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-project_created']},
        ),
        migrations.AlterModelOptions(
            name='step',
            options={'ordering': ['-step_created']},
        ),
        migrations.RemoveField(
            model_name='project',
            name='steps',
        ),
        migrations.AddField(
            model_name='project',
            name='user',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='account.customuser'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='step',
            name='project',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='projects.project'),
            preserve_default=False,
        ),
    ]
