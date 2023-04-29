from django.db import models

class Yonalish(models.Model):
    nom = models.CharField(max_length=50)
    aktiv = models.BooleanField()
    def __str__(self):
        return self.nom

class Fan(models.Model):
    fan = models.CharField(max_length=50)
    asosiy = models.BooleanField()
    yonalish_fk = models.ForeignKey(Yonalish, on_delete=models.CASCADE)
    def __str__(self):
        return self.fan

class Ustoz(models.Model):
    tanlov = [
        ("Erkak", "Erkak"),
        ("Ayol", "Ayol")
    ]
    tanlov_2 = [
        ("Magistr", "Magistr"),
        ("Bakalavr", "Bakalavr")
    ]
    ism = models.CharField(max_length=35)
    jins = models.CharField(max_length=50, choices=tanlov)
    yosh = models.PositiveIntegerField()
    daraja = models.CharField(max_length=50 ,choices=tanlov_2)
    fan_fk = models.ForeignKey(Fan, on_delete=models.CASCADE)
    def __str__(self):
        return self.ism

class Talaba(models.Model):
    ism = models.CharField(max_length=50)
    kitob_soni = models.PositiveIntegerField()
    kurs = models.CharField(max_length=30)
    def __str__(self):
        return self.ism

class Muallif(models.Model):
    jins_tanlov = [
        ("Erkak", "Erkak"),
        ("Ayol", "Ayol")
    ]
    tirik_tanlov = [
        ("Tirik", "Tirik"),
        ("Vafot etgan", "Vafot etgan")
    ]
    ism = models.CharField(max_length=50)
    kitob_soni = models.PositiveSmallIntegerField()
    jins = models.CharField(max_length=50, choices=jins_tanlov)
    tirik = models.CharField(max_length=50, choices=tirik_tanlov)
    tugilgan_yil = models.DateField()
    def __str__(self):
        return self.ism

class Kitob(models.Model):
    nom = models.CharField(max_length=50)
    muallif_fk = models.ForeignKey(Muallif, on_delete=models.CASCADE)
    sahifa = models.CharField(max_length=34)
    janr = models.CharField(max_length=50)


    def __str__(self):
        return str(self.nom)

class Admin(models.Model):
    ism = models.CharField(max_length=50)
    ish_vaqti = models.CharField(max_length=100)
    def __str__(self):
        return self.ism

class Record(models.Model):
    talaba_fk = models.ForeignKey(Talaba, on_delete=models.CASCADE)
    kitob_fk = models.ForeignKey(Kitob, on_delete=models.CASCADE)
    admin_fk = models.ForeignKey(Admin, on_delete=models.CASCADE)
    onlingan_sana = models.DateField()
    qaytarish_sana = models.DateField()
    qaytardi = models.BooleanField()
    def __str__(self):
        return str(self.talaba_fk)
