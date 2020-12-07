# Generated by Django 3.1.3 on 2020-11-16 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='boardmodul',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boardmodul_title', models.CharField(max_length=200, verbose_name='modulname')),
                ('boardmodul_text', models.TextField(verbose_name='modulinfo')),
                ('pub_date', models.DateTimeField(verbose_name='publicdate')),
            ],
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=50, verbose_name='authorname')),
                ('comment_text', models.CharField(max_length=200, verbose_name='commenttext')),
                ('boardmodul', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boardmodul.boardmodul')),
            ],
        ),
    ]
