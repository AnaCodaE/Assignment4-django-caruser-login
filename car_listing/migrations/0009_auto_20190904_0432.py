# Generated by Django 2.2.4 on 2019-09-04 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_listing', '0008_auto_20190904_0429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='year_of_make',
            field=models.IntegerField(choices=[(2009, '2009'), (2010, '2010'), (2011, '2011'), (2012, '2012'), (2013, '2013'), (2014, '2014'), (2015, '2015'), (2016, '2016'), (2017, '2017'), (2018, '2018'), (2019, '2019')], default='2009'),
        ),
    ]
