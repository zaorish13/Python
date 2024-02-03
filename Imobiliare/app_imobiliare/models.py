from django.db import models


class RealEstate(models.Model):
    RS_id_estate = models.IntegerField()
    RS_titlu = models.CharField(max_length=255)
    RS_zona = models.CharField(max_length=255)
    RS_compartimentare_alege = [
        ('open space', 'Open Space'),
        ('semidecomandat', 'Semidecomandat'),
        ('decomandat', 'Decomandat'),
        ('circular', 'Circular'),
        ('nedecomandat', 'Nedecomandat'),
    ]
    RS_compartimentare = models.CharField(
        max_length=255,
        choices=RS_compartimentare_alege,
        default='Decomandat',
    )
    RS_total_mp = models.IntegerField()
    RS_etaj = models.IntegerField()
    RS_an_finalizare_constructie = models.IntegerField()
    RS_stare_proprietate = models.CharField(max_length=255)
    RS_pret = models.DecimalField(max_digits=10, decimal_places=2)
    RS_camere = models.IntegerField()
    RS_bai = models.IntegerField()
    RS_descriere = models.TextField()



class Agent(models.Model):
    id_agent = models.IntegerField()
    name = models.CharField(max_length=255)
    email = models.EmailField()
