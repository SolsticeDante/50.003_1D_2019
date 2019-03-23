# Generated by Django 2.1.7 on 2019-02-26 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_id', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=60)),
                ('resolved', models.IntegerField(default=0)),
                ('read', models.IntegerField(default=0)),
                ('description', models.CharField(max_length=256)),
                ('user', models.CharField(max_length=60)),
            ],
        ),
    ]
