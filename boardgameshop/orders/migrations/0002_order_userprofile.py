# Generated by Django 4.1.2 on 2022-11-13 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myauth', '0001_initial'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='userprofile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='userprofile_orders', to='myauth.userprofile'),
        ),
    ]
