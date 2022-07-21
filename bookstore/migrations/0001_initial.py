# Generated by Django 4.0.6 on 2022-07-19 09:44

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
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('edition', models.PositiveIntegerField(blank=True, null=True)),
                ('author', models.CharField(max_length=200)),
                ('ISBN', models.PositiveIntegerField()),
                ('subject_area', models.CharField(max_length=50)),
                ('book_cover', models.ImageField(default='Book cover', upload_to='bookcovers')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=120)),
                ('last_name', models.CharField(max_length=120)),
                ('password', models.CharField(max_length=15)),
                ('course', models.CharField(max_length=50)),
                ('reg_no', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='Your sex', max_length=10)),
                ('username', models.ForeignKey(max_length=20, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IssuedBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issued_date', models.DateField(auto_now=True)),
                ('expiry_date', models.DateField(default=None)),
                ('fine', models.PositiveIntegerField(default=None)),
                ('ISBN', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bookstore.book')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bookstore.student')),
            ],
        ),
    ]