# Generated by Django 4.0 on 2024-11-22 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kotlinApp', '0006_member'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('title', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
            ],
        ),
    ]