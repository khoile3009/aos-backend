from django.db import models

# Create your models here.


class Warscroll(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    prename = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=100)
    postname = models.CharField(max_length=100, null=True)
    wounds = models.IntegerField()
    move = models.IntegerField()
    control = models.IntegerField()
    saves = models.IntegerField()
    wards = models.IntegerField(null=True)
    baseSize = models.IntegerField()
    points = models.IntegerField()
    numberOfModels = models.IntegerField()
    description = models.TextField()


PHASE_CHOICES = [
    ("turnStart", "Turn Start"),
    ("hero", "Hero"),
    ("movement", "Movement"),
    ("shooting", "Shooting"),
    ("charge", "Charge"),
    ("combat", "Combat"),
    ("turnEnd", "Turn End"),
    ("passive", "Passive"),
    ("reaction", "Reaction"),
]

SIDE_CHOICES = [("your", "Your"), ("enemy", "Enemy"), ("any", "Any")]


class Ability(models.Model):
    warscroll = models.ForeignKey(
        Warscroll, related_name="abilities", on_delete=models.CASCADE
    )
    phase = models.CharField(choices=PHASE_CHOICES, max_length=10)
    side = models.CharField(choices=SIDE_CHOICES, max_length=5)
    phaseText = models.TextField()
    text = models.TextField()


class Weapon(models.Model):
    warscroll = models.ForeignKey(
        Warscroll, related_name="weapons", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=50)
    isRange = models.BooleanField(max_length=50)
    range = models.IntegerField(null=True)
    attack = models.CharField(max_length=5)
    hit = models.IntegerField()
    wound = models.IntegerField()
    rend = models.IntegerField()
    damage = models.CharField(max_length=3)


class Keyword(models.Model):
    warscroll = models.ForeignKey(
        Warscroll, related_name="keywords", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=30)


class WeaponAbility(models.Model):
    weapon = models.ForeignKey(
        Weapon, related_name="abilities", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=30)
