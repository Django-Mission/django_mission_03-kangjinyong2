# Generated by Django 4.0.4 on 2022-04-17 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0007_answer_updated_at_faq_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='updated_at',
        ),
    ]
