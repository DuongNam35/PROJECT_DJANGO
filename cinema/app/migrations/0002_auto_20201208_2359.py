# Generated by Django 3.1.1 on 2020-12-08 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('bookingDate', models.DateTimeField()),
                ('showDate', models.DateTimeField()),
                ('status', models.IntegerField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.movie')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=30, unique=True, verbose_name='Mã')),
                ('numberOfRow', models.IntegerField(verbose_name='Số dãy ghế')),
                ('numberOfCols', models.IntegerField(verbose_name='số ghế trong một dãy')),
            ],
        ),
        migrations.CreateModel(
            name='BookingTicket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seatRow', models.IntegerField()),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.booking')),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.room'),
        ),
        migrations.AlterField(
            model_name='movieshow',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.room', verbose_name='Phòng chiếu'),
        ),
    ]