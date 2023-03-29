# Generated by Django 4.1.7 on 2023-03-27 07:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0003_rename_nid_pass_professional_nid_passport'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='professional',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='professional',
            name='edu_type',
            field=models.CharField(choices=[('M.D.', 'M.D.'), ('Psy.D', 'Psy.D'), ('PhD', 'PhD'), ('MSc in Counseling Psychology', 'MSc in Counseling Psychology'), ('MSc in Clinical Social Work', 'MSc in Clinical Social Work')], max_length=30),
        ),
    ]