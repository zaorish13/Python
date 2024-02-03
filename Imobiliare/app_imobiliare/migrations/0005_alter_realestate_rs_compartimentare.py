# Generated by Django 5.0.1 on 2024-02-02 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_imobiliare', '0004_remove_realestate_rs_compartimerntare_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realestate',
            name='RS_compartimentare',
            field=models.CharField(choices=[('open space', 'Open Space'), ('semidecomandat', 'Semidecomandat'), ('decomandat', 'Decomandat'), ('circular', 'Circular'), ('nedecomandat', 'Nedecomandat')], default='Decomandat', max_length=255),
        ),
    ]