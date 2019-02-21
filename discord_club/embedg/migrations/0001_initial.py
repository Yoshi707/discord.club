# Generated by Django 2.1 on 2019-02-18 19:17

from django.db import migrations, models
import django.db.models.deletion
import embedg.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('oauth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Embed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=embedg.models._default_timestamp)),
                ('data', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oauth.OauthUser')),
            ],
        ),
    ]