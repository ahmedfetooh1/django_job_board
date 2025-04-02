# Generated by Django 5.1.5 on 2025-02-07 23:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_job_slug_alter_job_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('website', models.URLField()),
                ('cv', models.FileField(upload_to='apply/')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('cover_letter', models.TextField(max_length=500)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apply_job', to='job.job')),
            ],
        ),
    ]
