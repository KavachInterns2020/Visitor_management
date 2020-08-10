# Generated by Django 3.0.8 on 2020-07-29 18:53

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
            name='Event',
            fields=[
                ('tag', models.CharField(blank=True, choices=[('Incomplete', 'Incomplete'), ('Complete', 'Complete')], default='blank', max_length=12, null=True)),
                ('event_id', models.AutoField(primary_key=True, serialize=False)),
                ('event_date_time', models.DateTimeField(default='', max_length=20, unique=True)),
                ('event_purpose', models.CharField(choices=[('Birthday', 'Birthday'), ('Meet Up', 'Meet Up'), ('Anniversary', 'Anniversary'), ('Festival', 'Festival'), ('General', 'General')], max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('visitor_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=200, unique=True)),
                ('Phone_no', models.CharField(default=' ', max_length=12)),
                ('email_id', models.EmailField(default='', max_length=200)),
                ('visitor_image', models.ImageField(default='', null=True, upload_to='')),
                ('id_proof', models.ImageField(default='', null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='VisitDetails',
            fields=[
                ('visit_id', models.AutoField(primary_key=True, serialize=False)),
                ('duration', models.CharField(choices=[('1 hours', '1 hours'), ('5 hours', '5 hours'), ('1 day', '1 day'), ('1 week', '1 week'), ('1 month', '1 month'), ('5 month', '5 month'), ('1 year', '1 year')], max_length=20)),
                ('purpose', models.CharField(choices=[('Guest', 'Guest'), ('Home_Service', 'Home_Service'), ('Clients', 'Clients'), ('Delivery_Service', 'Delivery_Service'), ('General_service', 'General_service'), ('Event', 'Event')], max_length=30)),
                ('visit_date', models.DateTimeField(auto_now_add=True)),
                ('flat_no', models.CharField(default=' ', max_length=300)),
                ('visit_detail', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='basic.Visitor')),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('host_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default=' ', max_length=200)),
                ('Phone_no', models.IntegerField(default=91)),
                ('email_id', models.EmailField(default='', max_length=200)),
                ('flat_no', models.IntegerField(default=0)),
                ('no_of_people', models.IntegerField(default=0)),
                ('host_image', models.ImageField(blank=True, default='download.jpeg', null=True, upload_to='')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EventVisitor',
            fields=[
                ('event_visitor_id', models.AutoField(primary_key=True, serialize=False)),
                ('visit_time', models.DateTimeField(auto_now_add=True)),
                ('event_info', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='basic.Event')),
                ('event_visitor_info', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='basic.Visitor')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='organizer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='basic.Host'),
        ),
    ]