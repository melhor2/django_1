# Generated by Django 4.2.2 on 2023-06-13 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_remove_student_name_student_fname_student_lname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='document_type',
            field=models.CharField(choices=[('CC', 'Cedula de ciudadania'), ('PPT', 'permiso de protección temporal'), ('CE', 'Cedula de extranjería'), ('TI', 'Tarjeta de identidad')], default='CC', max_length=3),
        ),
    ]
