# Generated by Django 5.1.2 on 2024-10-15 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Infirmier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('telephone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=100)),
                ('date_embauche', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
