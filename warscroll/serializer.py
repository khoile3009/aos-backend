from rest_framework import serializers

from warscroll.models import (
    Ability,
    Keyword,
    Warscroll,
    Weapon,
    WeaponAbility,
)


class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = ["name"]


class WeaponAbilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = WeaponAbility
        fields = ["name"]


class WeaponSerializer(serializers.ModelSerializer):
    abilities = WeaponAbilitySerializer(many=True)

    class Meta:
        model = Weapon
        fields = [
            "name",
            "isRange",
            "range",
            "attack",
            "hit",
            "wound",
            "rend",
            "damage",
            "abilities",
        ]


class AbilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ability
        fields = ["phase", "side", "phaseText", "text"]


class WarscrollSerializer(serializers.ModelSerializer):
    weapons = WeaponSerializer(many=True)
    abilities = AbilitySerializer(many=True)
    keywords = KeywordSerializer(many=True)

    class Meta:
        model = Warscroll
        fields = [
            "id",
            "prename",
            "name",
            "postname",
            "wounds",
            "move",
            "control",
            "saves",
            "wards",
            "baseSize",
            "points",
            "numberOfModels",
            "description",
            "weapons",
            "abilities",
            "keywords",
        ]

    def create(self, validated_data):
        weapons = validated_data.pop("weapons")
        abilities = validated_data.pop("abilities")
        keywords = validated_data.pop("keywords")
        warscroll = Warscroll.objects.create(**validated_data)

        # Add Weapons
        for weapon in weapons:
            weapon_abilities_data = weapon.pop("abilities")
            weapon = Weapon.objects.create(warscroll=warscroll, **weapon)
            for weapon_ability_data in weapon_abilities_data:
                WeaponAbility.objects.create(weapon=weapon, **weapon_ability_data)

        # Add abilities
        for ability in abilities:
            Ability.objects.create(warscroll=warscroll, **ability)

        # Add keywords
        for keyword in keywords:
            Keyword.objects.create(warscroll=warscroll, **keyword)
        return warscroll
