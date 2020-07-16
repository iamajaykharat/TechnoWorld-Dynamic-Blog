# Generated by Django 3.0.8 on 2020-07-16 18:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_blogpost_content1'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogComment',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.TextField(verbose_name='Comment on Article')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date-Time')),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.BlogComment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.BlogPost')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
