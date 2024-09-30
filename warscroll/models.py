from django.db import models

# Create your models here.


class Warscroll(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    wounds = models.IntegerField()
    move = models.IntegerField()
    control = models.IntegerField()
    saves = models.IntegerField()
    wards = models.IntegerField(null=True)
    baseSize = models.IntegerField()
    points = models.IntegerField()
    numberOfModels = models.IntegerField()
    description = models.TextField(null=True)
    notes = models.TextField(null=True)


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
    name = models.CharField(max_length=100)
    declare = models.TextField(null=True)
    effect = models.TextField()
    lore = models.TextField(null=True)
    cost = models.IntegerField(null=True)


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


class AbilityKeyword(models.Model):
    ability = models.ForeignKey(
        Ability, related_name="keywords", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=30)
