# Generated by Django 5.0.1 on 2024-09-30 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_rename_roll_no_student_reg_no'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='branch',
            new_name='department',
        ),
    ]
