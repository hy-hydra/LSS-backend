# Generated by Django 4.2.5 on 2023-11-12 14:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0027_rename_last_login_device_user_last_signin_device_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inquiry',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='inquiry', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('persona_inquiry_id', models.CharField(max_length=255)),
                ('status', models.CharField(default='created')),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('modified_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
