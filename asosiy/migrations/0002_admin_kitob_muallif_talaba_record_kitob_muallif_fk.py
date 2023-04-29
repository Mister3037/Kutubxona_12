# Generated by Django 4.2 on 2023-04-15 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=50)),
                ('ish_vaqti', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Kitob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('sahifa', models.CharField(max_length=34)),
                ('janr', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Muallif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=25)),
                ('kitob_soni', models.PositiveSmallIntegerField()),
                ('jins', models.CharField(choices=[('Erkak', 'Erkak'), ('Ayol', 'Ayol')], max_length=50)),
                ('tirik', models.CharField(choices=[('Tirik', 'Tirik'), ('Vafot etgan', 'Vafot etgan')], max_length=50)),
                ('tugilgan_yil', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Talaba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=50)),
                ('kitob_soni', models.PositiveIntegerField()),
                ('kurs', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('onlingan_sana', models.DateField()),
                ('qaytarish_sana', models.DateField()),
                ('qaytardi', models.BooleanField()),
                ('admin_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.admin')),
                ('kitob_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.kitob')),
                ('talaba_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.talaba')),
            ],
        ),
        migrations.AddField(
            model_name='kitob',
            name='muallif_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.muallif'),
        ),
    ]
