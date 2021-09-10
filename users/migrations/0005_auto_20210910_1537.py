# Generated by Django 3.2.7 on 2021-09-10 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_message'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['-created']},
        ),
        migrations.RemoveField(
            model_name='message',
            name='name',
        ),
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profile'),
        ),
    ]