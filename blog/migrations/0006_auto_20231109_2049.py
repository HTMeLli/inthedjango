# Generated by Django 3.2.23 on 2023-11-09 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_supplement_daily_dose'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppingitem',
            name='price',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.price'),
        ),
        migrations.AlterField(
            model_name='shoppingitem',
            name='supplement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shoppingitems', to='blog.supplement'),
        ),
    ]