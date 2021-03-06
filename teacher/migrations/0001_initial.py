# Generated by Django 3.2.4 on 2021-07-02 03:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('teacher_bio', models.TextField(max_length=5000)),
                ('depertment', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='department.department')),
            ],
        ),
    ]
