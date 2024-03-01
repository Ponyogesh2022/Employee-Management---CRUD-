# Generated by Django 5.0.2 on 2024-02-29 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employee_Id', models.IntegerField()),
                ('Employee_Name', models.CharField(max_length=30)),
                ('Employee_Email', models.CharField(max_length=30)),
                ('Employee_PhoneNumber', models.BigIntegerField()),
                ('Employee_DOB', models.DateField()),
                ('Last_Modified_Date', models.DateField()),
            ],
        ),
    ]