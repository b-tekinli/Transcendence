# Generated by Django 4.2.7 on 2023-12-19 13:43

from django.db import migrations, models
import django.utils.timezone
import trascendence.api.models.SerializableModel
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, max_length=36, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('intraId', models.IntegerField()),
                ('username', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('avatarURI', models.CharField(max_length=200)),
            ],
            bases=(models.Model, trascendence.api.models.SerializableModel.SerializableModel),
        ),
    ]
