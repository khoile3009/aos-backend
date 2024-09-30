from rest_framework import serializers

from warscroll.models import (
    Ability,
    AbilityKeyword,
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


class AbilityKeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbilityKeyword
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
    keywords = AbilityKeywordSerializer(many=True)

    class Meta:
        model = Ability
        fields = [
            "phase",
            "side",
            "phaseText",
            "name",
            "declare",
            "effect",
            "lore",
            "cost",
            "keywords",
        ]


class WarscrollSerializer(serializers.ModelSerializer):
    weapons = WeaponSerializer(many=True)
    abilities = AbilitySerializer(many=True)
    keywords = KeywordSerializer(many=True)

    class Meta:
        model = Warscroll
        fields = [
            "id",
            "name",
            "wounds",
            "move",
            "control",
            "saves",
            "wards",
            "baseSize",
            "points",
            "numberOfModels",
            "description",
            "notes",
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
            ability_keywords = ability.pop("keywords")
            ability = Ability.objects.create(warscroll=warscroll, **ability)
            for ability_keyword in ability_keywords:
                AbilityKeyword.object.create(ability=ability, **ability_keyword)

        # Add keywords
        for keyword in keywords:
            Keyword.objects.create(warscroll=warscroll, **keyword)
        return warscroll
