# Generated by Django 3.1.5 on 2021-01-05 00:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('commitment_date', models.DateField(auto_now_add=True)),
                ('committed_effort', models.CharField(max_length=100)),
                ('planned_completion_date', models.DateField()),
                ('actual_completion_date', models.DateField()),
                ('motivation', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('priority', models.CharField(choices=[('L', 'Low'), ('M', 'Medium'), ('H', 'High')], max_length=50)),
                ('level', models.CharField(choices=[('B', 'Beginner'), ('I', 'Intermediate'), ('A', 'Advanced')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('duration', models.IntegerField()),
                ('description', models.TextField()),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goals.goal')),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goals.resource')),
            ],
        ),
        migrations.CreateModel(
            name='Milestone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('planned_completion_date', models.DateField()),
                ('actual_completion_date', models.DateField()),
                ('reward', models.TextField()),
                ('proof', models.TextField()),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goals.goal')),
            ],
        ),
    ]