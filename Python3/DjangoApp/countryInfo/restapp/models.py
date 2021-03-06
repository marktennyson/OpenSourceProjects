from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=600, unique=True)
    def __str__(self): return self.name
    def toDict(self):
        return {
            'id' : self.pk,
            'name' : self.name
        }

class SubRegion(models.Model):
    name = models.CharField(max_length=600, unique=True)
    def __str__(self): return self.name
    def toDict(self):
        return {
            'id' : self.pk,
            'name' : self.name
        }

class CountryInfo(models.Model):
    name = models.CharField(max_length=600)
    capital = models.CharField(max_length=600, blank=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    subRegion = models.ForeignKey(SubRegion, on_delete=models.CASCADE)
    population = models.IntegerField()
    currency = models.CharField(max_length=600)
    languages = models.CharField(max_length=600)
    code = models.CharField(max_length=3, unique=True)
    neighbours = models.CharField(max_length=600, blank=True)
    flag = models.CharField(max_length=600, blank=True)
    area = models.IntegerField(null=True, blank=True)
    nativeName = models.CharField(max_length=600, blank=True)
    

    def __str__(self):
        return self.name

    def toDict(self):
        try: neighbours = self.neighbours.split("_")
        except: neighbours = ""
        return {
            'id' : self.pk,
            'name': self.name,
            'capital' : self.capital,
            'region' : self.region.name,
            'subRegion' : self.subRegion.name,
            'population' : self.population,
            'currency' : self.currency,
            'languages' : self.languages,
            'code' : self.code,
            'neighbours' : neighbours,
            'flag' : self.flag,
            'area' : self.area,
            'nativeName' : self.nativeName,
        }