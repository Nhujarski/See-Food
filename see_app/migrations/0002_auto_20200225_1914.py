# Generated by Django 2.2 on 2020-02-25 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('see_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('serving', models.CharField(max_length=50)),
                ('cals', models.IntegerField()),
                ('total_carbs', models.IntegerField()),
                ('fiber', models.IntegerField()),
                ('protein', models.IntegerField()),
                ('fats', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='user',
            name='updated_at',
        ),
        migrations.CreateModel(
            name='Mesurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.IntegerField()),
                ('current_weight', models.IntegerField()),
                ('goal_weight', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_measurement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='measurments', to='see_app.User')),
            ],
        ),
    ]
