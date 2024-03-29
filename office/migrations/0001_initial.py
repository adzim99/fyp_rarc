# Generated by Django 4.0 on 2022-01-14 02:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('functions', '0003_delete_office'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_no', models.IntegerField(null=True)),
                ('staff_name', models.CharField(max_length=200, null=True)),
                ('designation', models.CharField(max_length=100, null=True)),
                ('tel_no', models.IntegerField(null=True)),
                ('booking', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='functions.booking')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
