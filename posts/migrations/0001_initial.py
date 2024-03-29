# Generated by Django 4.1.6 on 2023-03-24 23:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='donateMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(allow_unicode=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('description', models.TextField()),
                ('current_amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('target_amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('donors', models.ManyToManyField(through='posts.donateMember', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
                'unique_together': {('user', 'title')},
            },
        ),
        migrations.AddField(
            model_name='donatemember',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='donorMember', to='posts.post'),
        ),
        migrations.AddField(
            model_name='donatemember',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_donors', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='donatemember',
            unique_together={('post', 'user')},
        ),
    ]
