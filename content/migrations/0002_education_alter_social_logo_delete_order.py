# Generated by Django 4.2.4 on 2024-05-30 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='images/')),
                ('name', models.CharField(max_length=300)),
                ('desc', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AlterField(
            model_name='social',
            name='logo',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.DeleteModel(
            name='order',
        ),
    ]
