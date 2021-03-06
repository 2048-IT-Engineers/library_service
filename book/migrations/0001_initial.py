# Generated by Django 3.1.1 on 2020-10-16 10:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('info', models.CharField(blank=True, max_length=500, null=True)),
                ('since_given', models.DateTimeField(default=django.utils.timezone.now)),
                ('since_back', models.DateTimeField(default=django.utils.timezone.now)),
                ('upload_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('when_should_be_back', models.DateTimeField(default=django.utils.timezone.now)),
                ('in_use_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='current_book_user', to=settings.AUTH_USER_MODEL)),
                ('read_history', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_giving_book', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_term', models.IntegerField(default=0)),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='given_book', to='book.book')),
                ('librarian', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='librarian_who_gave_the_book', to=settings.AUTH_USER_MODEL)),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_who_received_the_book', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
