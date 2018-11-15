from enum import Enum
from dataclasses import dataclass


## Heroes names, types and factions
class Faction(Enum):
    EMPTY = 'EMPTY'
    ALLIANCE = 'ALLIANCE'
    HORDE = 'HORDE'
    ELF = 'ELF'
    UNDEAD = 'UNDEAD'
    HEAVEN = 'HEAVEN'
    HELL = 'HELL'


class HeroType(Enum):
    EMPTY = 'EMPTY'
    WARRIOR = 'WARRIOR'
    ASSASSIN = 'ASSASSIN'
    WANDERER = 'WANDERER'
    CLERIC = 'CLERIC'
    MAGE = 'MAGE'


class HeroName(Enum):
    EMPTY = 'Empty Hero'

    SIR_CONRAD = 'Sir Conrad'
    LONE_HERO = 'Lone Hero' 
    OLIVIA = 'Olivia'
    KING_LIONHEART = 'King Lionheart'
    TESLA = 'Tesla'
    MULAN = 'Mulan'
    SAW_MACHINE = 'Saw Machine'
    ULTIMA = 'Ultima'
    VIVIENNE = 'Vivienne'
    MARTIN = 'Martin'
    SAMURAI = 'Samurai'

    KHALIL = 'Khalil'
    RLYEH = 'Rlyeh'
    WOLF_RIDER = 'Wolf Rider'
    ABYSS_LORD = 'Abyss Lord'
    MEDUSA = 'Medusa'
    EAGLE_EYE_SHAMAN = 'Eagle-eye Shaman'
    SWORD_MASTER = 'Sword Master'
    SCARLET = 'Scarlet'
    MINOTAUR = 'Minotaur'
    BLOOD_TOOTH = 'Blood Tooth'
    LEXAR = 'Lexar'

    MEGAW = 'Megaw'
    WEREWORF = 'Werewolf'
    CENTAUR = 'Centaur'
    TIGER_KING = 'Tiger King'
    DEMON_FIGHTER = 'Demon Fighter'
    GRAND = 'Grand'
    FOREST_HEALER = 'Forest Healer'
    ORPHEE = 'Orphee'
    LUNA = 'Luna'
    VEGVISIR = 'Vegvisir'

    FORREN = 'Forren'
    PUPPET_MAID = 'Puppet Maid'
    EXDEATH = 'Exdeath'
    HESTER = 'Hester'
    DZIEWONA =  'Dziewona'
    WOLNIR = 'Wolnir'
    CURSED_ONE = 'Cursed One'
    GERALD = 'Gerald'
    REAPER = 'Reaper'
    RIPPER = 'Ripper'
    ADEN = 'Aden'
    SHUDDE_M_ELL = "Shudde M'ell"

    HEAVEN_JUDGE = 'Heaven Judge'
    NAMELESS_KING = 'Nameless King'
    VERTHANDI = 'Verthandi'
    MARS = 'Mars'

    DARK_JUDGE = 'Dark Judge'
    FREYA = 'Freya'
    MONKEY_KING = 'Monkey King'
    CHESSIA = 'Chessia'


## Equipment
class Equipment:
    def __init__(self, armor, helmet, weapon, pendant):
        self.hp = armor.hp + helmet.hp
        self.atk = weapon.atk + pendant.atk

        hp_bonus = 0
        atk_bonus = 0
        set_counts = {}
        for item in armor, helmet, weapon, pendant:
            if item.set in set_counts:
                set_counts[item.set] += 1
            else:
                set_counts[item.set] = 1
        for set in set_counts:
            if set_counts[set] >= 2:
                hp_bonus += set.hp_bonus_1
            if set_counts[set] >= 3:
                atk_bonus += set.atk_bonus
            if set_counts[set] == 4:
                hp_bonus += set.hp_bonus_2

        self.hp_bonus = hp_bonus
        self.atk_bonus = atk_bonus


@dataclass
class SetEmpty:
    hp_bonus_1 = 0
    atk_bonus = 0
    hp_bonus_2 = 0
@dataclass
class SetG1:
    hp_bonus_1 = 0
    atk_bonus = 0
    hp_bonus_2 = 0
@dataclass
class SetG2:
    hp_bonus_1 = 0
    atk_bonus = 0
    hp_bonus_2 = 0
@dataclass
class SetB1:
    hp_bonus_1 = 0
    atk_bonus = 0
    hp_bonus_2 = 0
@dataclass
class SetB2:
    hp_bonus_1 = 0
    atk_bonus = 0
    hp_bonus_2 = 0
@dataclass
class SetY1:
    hp_bonus_1 = 0
    atk_bonus = 0
    hp_bonus_2 = 0
@dataclass
class SetY2:
    hp_bonus_1 = 0
    atk_bonus = 0
    hp_bonus_2 = 0
@dataclass
class SetY3:
    hp_bonus_1 = 0.02
    atk_bonus = 0.03
    hp_bonus_2 = 0.01
@dataclass
class SetP1:
    hp_bonus_1 = 0.04
    atk_bonus = 0.05
    hp_bonus_2 = 0.02
@dataclass
class SetP2:
    hp_bonus_1 = 0.05
    atk_bonus = 0.07
    hp_bonus_2 = 0.04
@dataclass
class SetP3:
    hp_bonus_1 = 0.07
    atk_bonus = 0.09
    hp_bonus_2 = 0.04
@dataclass
class SetP4:
    hp_bonus_1 = 0.08
    atk_bonus = 0.11
    hp_bonus_2 = 0.05
@dataclass
class SetO1:
    hp_bonus_1 = 0.1
    atk_bonus = 0.13
    hp_bonus_2 = 0.05
@dataclass
class SetO2:
    hp_bonus_1 = 0.11
    atk_bonus = 0.15
    hp_bonus_2 = 0.06
@dataclass
class SetO3:
    hp_bonus_1 = 0.12
    atk_bonus = 0.17
    hp_bonus_2 = 0.07
@dataclass
class SetO4:
    hp_bonus_1 = 0.14
    atk_bonus = 0.19
    hp_bonus_2 = 0.07


@dataclass
class EmptyItem:
    hp = 0
    atk = 0
    set = SetEmpty


@dataclass
class ArmorG1:
    hp = 141
    set = SetG1
@dataclass
class ArmorG2:
    hp = 169
    set = SetG2
@dataclass
class ArmorB1:
    hp = 337
    set = SetB1
@dataclass
class ArmorB2:
    hp = 434
    set = SetB2
@dataclass
class ArmorY1:
    hp = 970
    set = SetY1
@dataclass
class ArmorY2:
    hp = 1255
    set = SetY2
@dataclass
class ArmorY3:
    hp = 1541
    set = SetY3
@dataclass
class ArmorP1:
    hp = 2645
    set = SetP1
@dataclass
class ArmorP2:
    hp = 3207
    set = SetP2
@dataclass
class ArmorP3:
    hp = 3770
    set = SetP3
@dataclass
class ArmorP4:
    hp = 4333
    set = SetP4
@dataclass
class ArmorO1:
    hp = 6401
    set = SetO1
@dataclass
class ArmorO2:
    hp = 7811
    set = SetO2
@dataclass
class ArmorO3:
    hp = 9222
    set = SetO3
@dataclass
class ArmorO4:
    hp = 10632
    set = SetO4


@dataclass
class HelmetG1:
    hp = 94
    set = SetG1
@dataclass
class HelmetG2:
    hp = 113
    set = SetG2
@dataclass
class HelmetB1:
    hp = 223
    set = SetB1
@dataclass
class HelmetB2:
    hp = 289
    set = SetB2
@dataclass
class HelmetY1:
    hp = 647
    set = SetY1
@dataclass
class HelmetY2:
    hp = 837
    set = SetY2
@dataclass
class HelmetY3:
    hp = 1027
    set = SetY3
@dataclass
class HelmetP1:
    hp = 1763
    set = SetP1
@dataclass
class HelmetP2:
    hp = 2183
    set = SetP2
@dataclass
class HelmetP3:
    hp = 2513
    set = SetP3
@dataclass
class HelmetP4:
    hp = 2889
    set = SetP4
@dataclass
class HelmetO1:
    hp = 4267
    set = SetO1
@dataclass
class HelmetO2:
    hp = 5207
    set = SetO2
@dataclass
class HelmetO3:
    hp = 6148
    set = SetO3
@dataclass
class HelmetO4:
    hp = 7088
    set = SetO4


@dataclass
class WeaponG1:
    atk = 32
    set = SetG1
@dataclass
class WeaponG2:
    atk = 38
    set = SetG2
@dataclass
class WeaponB1:
    atk = 66
    set = SetB1
@dataclass
class WeaponB2:
    atk = 85
    set = SetB2
@dataclass
class WeaponY1:
    atk = 168
    set = SetY1
@dataclass
class WeaponY2:
    atk = 218
    set = SetY2
@dataclass
class WeaponY3:
    atk = 256
    set = SetY3
@dataclass
class WeaponP1:
    atk = 414
    set = SetP1
@dataclass
class WeaponP2:
    atk = 502
    set = SetP2
@dataclass
class WeaponP3:
    atk = 590
    set = SetP3
@dataclass
class WeaponP4:
    atk = 678
    set = SetP4
@dataclass
class WeaponO1:
    atk = 914
    set = SetO1
@dataclass
class WeaponO2:
    atk = 1116
    set = SetO2
@dataclass
class WeaponO3:
    atk = 1317
    set = SetO3
@dataclass
class WeaponO4:
    atk = 1519
    set = SetO4


@dataclass
class PendantG1:
    atk = 21
    set = SetG1
@dataclass
class PendantG2:
    atk = 25
    set = SetG2
@dataclass
class PendantB1:
    atk = 44
    set = SetB1
@dataclass
class PendantB2:
    atk = 57
    set = SetB2
@dataclass
class PendantY1:
    atk = 112
    set = SetY1
@dataclass
class PendantY2:
    atk = 145
    set = SetY2
@dataclass
class PendantY3:
    atk = 178
    set = SetY3
@dataclass
class PendantP1:
    atk = 276
    set = SetP1
@dataclass
class PendantP2:
    atk = 335
    set = SetP2
@dataclass
class PendantP3:
    atk = 393
    set = SetP3
@dataclass
class PendantP4:
    atk = 452
    set = SetP4
@dataclass
class PendantO1:
    atk = 610
    set = SetO1
@dataclass
class PendantO2:
    atk = 744
    set = SetO2
@dataclass
class PendantO3:
    atk = 878
    set = SetO3
@dataclass
class PendantO4:
    atk = 1013
    set = SetO4


@dataclass
class Armor:
    empty = EmptyItem
    G1 = ArmorG1
    G2 = ArmorG2
    B1 = ArmorB1
    B2 = ArmorB2
    Y1 = ArmorY1
    Y2 = ArmorY2
    Y3 = ArmorY3
    P1 = ArmorP1
    P2 = ArmorP2
    P3 = ArmorP3
    P4 = ArmorP4
    O1 = ArmorO1
    O2 = ArmorO2
    O3 = ArmorO3
    O4 = ArmorO4


@dataclass
class Helmet:
    empty = EmptyItem
    G1 = HelmetG1
    G2 = HelmetG2
    B1 = HelmetB1
    B2 = HelmetB2
    Y1 = HelmetY1
    Y2 = HelmetY2
    Y3 = HelmetY3
    P1 = HelmetP1
    P2 = HelmetP2
    P3 = HelmetP3
    P4 = HelmetP4
    O1 = HelmetO1
    O2 = HelmetO2
    O3 = HelmetO3
    O4 = HelmetO4


@dataclass
class Weapon:
    empty = EmptyItem
    G1 = WeaponG1
    G2 = WeaponG2
    B1 = WeaponB1
    B2 = WeaponB2
    Y1 = WeaponY1
    Y2 = WeaponY2
    Y3 = WeaponY3
    P1 = WeaponP1
    P2 = WeaponP2
    P3 = WeaponP3
    P4 = WeaponP4
    O1 = WeaponO1
    O2 = WeaponO2
    O3 = WeaponO3
    O4 = WeaponO4


@dataclass
class Pendant:
    empty = EmptyItem
    G1 = PendantG1
    G2 = PendantG2
    B1 = PendantB1
    B2 = PendantB2
    Y1 = PendantY1
    Y2 = PendantY2
    Y3 = PendantY3
    P1 = PendantP1
    P2 = PendantP2
    P3 = PendantP3
    P4 = PendantP4
    O1 = PendantO1
    O2 = PendantO2
    O3 = PendantO3
    O4 = PendantO4


## Rune
class BaseRune:
    atk = 0
    hp = 0
    atk_bonus = 0
    hp_bonus = 0
    armor_break = 0
    skill_damage = 0
    hit_rate = 0
    dodge = 0
    crit_rate = 0
    crit_damage = 0


class EmptyRune(BaseRune):
    pass


class AccuracyRuneB1(BaseRune):
    atk = 0
    atk_bonus = 0
    hit_rate = 0
class AccuracyRuneB2(BaseRune):
    atk = 0
    atk_bonus = 0
    hit_rate = 0
class AccuracyRuneG1(BaseRune):
    atk = 50
    atk_bonus = 0
    hit_rate = 0.02
class AccuracyRuneG2(BaseRune):
    atk = 70
    atk_bonus = 0
    hit_rate = 0.03
class AccuracyRuneY1(BaseRune):
    atk = 125
    atk_bonus = 0
    hit_rate = 0.05
class AccuracyRuneY2(BaseRune):
    atk = 155
    atk_bonus = 0
    hit_rate = 0.06
class AccuracyRuneY3(BaseRune):
    atk = 185
    atk_bonus = 0
    hit_rate = 0.07
class AccuracyRuneP1(BaseRune):
    atk = 0
    atk_bonus = 0
    hit_rate = 0
class AccuracyRuneP2(BaseRune):
    atk = 0
    atk_bonus = 0
    hit_rate = 0
class AccuracyRuneP3(BaseRune):
    atk = 0
    atk_bonus = 0
    hit_rate = 0
class AccuracyRuneO1(BaseRune):
    atk = 0
    atk_bonus = 0
    hit_rate = 0
class AccuracyRuneO2(BaseRune):
    atk = 0
    atk_bonus = 0
    hit_rate = 0
class AccuracyRuneO3(BaseRune):
    atk = 0
    atk_bonus = 0
    hit_rate = 0
class AccuracyRuneO4(BaseRune):
    atk = 0
    atk_bonus = 0
    hit_rate = 0
class AccuracyRuneR1(BaseRune):
    atk = 0
    atk_bonus = 0
    hit_rate = 0
class AccuracyRuneR2(BaseRune):
    atk = 620
    atk_bonus = 0.09
    hit_rate = 0.19


class CritRateRuneB1(BaseRune):
    hp = 0
    hp_bonus = 0
    crit_rate = 0
class CritRateRuneB2(BaseRune):
    hp = 0
    hp_bonus = 0
    crit_rate = 0
class CritRateRuneG1(BaseRune):
    hp = 300
    hp_bonus = 0
    crit_rate = 0.02
class CritRateRuneG2(BaseRune):
    hp = 600
    hp_bonus = 0
    crit_rate = 0.03
class CritRateRuneY1(BaseRune):
    hp = 920
    hp_bonus = 0
    crit_rate = 0.05
class CritRateRuneY2(BaseRune):
    hp = 1200
    hp_bonus = 0
    crit_rate = 0.06
class CritRateRuneY3(BaseRune):
    hp = 1480
    hp_bonus = 0
    crit_rate = 0.07
class CritRateRuneP1(BaseRune):
    hp = 0
    hp_bonus = 0
    crit_rate = 0
class CritRateRuneP2(BaseRune):
    hp = 0
    hp_bonus = 0
    crit_rate = 0
class CritRateRuneP3(BaseRune):
    hp = 2280
    hp_bonus = 0
    crit_rate = 0.11
class CritRateRuneO1(BaseRune):
    hp = 0
    hp_bonus = 0
    crit_rate = 0
class CritRateRuneO2(BaseRune):
    hp = 3460
    hp_bonus = 0
    crit_rate = 0.14
class CritRateRuneO3(BaseRune):
    hp = 0
    hp_bonus = 0
    crit_rate = 0
class CritRateRuneO4(BaseRune):
    hp = 0
    hp_bonus = 0
    crit_rate = 0
class CritRateRuneR1(BaseRune):
    hp = 0
    hp_bonus = 0
    crit_rate = 0
class CritRateRuneR2(BaseRune):
    hp = 0
    hp_bonus = 0.13
    crit_rate = 0.19


class AttackRuneB1(BaseRune):
    atk = 55
    atk_bonus = 0
class AttackRuneB2(BaseRune):
    atk = 72
    atk_bonus = 0
class AttackRuneG1(BaseRune):
    atk = 110
    atk_bonus = 0
class AttackRuneG2(BaseRune):
    atk = 150
    atk_bonus = 0
class AttackRuneY1(BaseRune):
    atk = 210
    atk_bonus = 0.04
class AttackRuneY2(BaseRune):
    atk = 270
    atk_bonus = 0.05
class AttackRuneY3(BaseRune):
    atk = 330
    atk_bonus = 0.06
class AttackRuneP1(BaseRune):
    atk = 0
    atk_bonus = 0
class AttackRuneP2(BaseRune):
    atk = 0
    atk_bonus = 0
class AttackRuneP3(BaseRune):
    atk = 0
    atk_bonus = 0
class AttackRuneO1(BaseRune):
    atk = 1000
    atk_bonus = 0.15
class AttackRuneO2(BaseRune):
    atk = 0
    atk_bonus = 0
class AttackRuneO3(BaseRune):
    atk = 0
    atk_bonus = 0
class AttackRuneO4(BaseRune):
    atk = 0
    atk_bonus = 0
class AttackRuneR1(BaseRune):
    atk = 0
    atk_bonus = 0
class AttackRuneR2(BaseRune):
    atk = 1200
    atk_bonus = 0.22


class EvasionRuneB1(BaseRune):
    hp = 0
    hp_bonus = 0
    dodge = 0
class EvasionRuneB2(BaseRune):
    hp = 0
    hp_bonus = 0
    dodge = 0
class EvasionRuneG1(BaseRune):
    hp = 0
    hp_bonus = 0
    dodge = 0
class EvasionRuneG2(BaseRune):
    hp = 0
    hp_bonus = 0
    dodge = 0
class EvasionRuneY1(BaseRune):
    hp = 920
    hp_bonus = 0
    dodge = 0.035
class EvasionRuneY2(BaseRune):
    hp = 1200
    hp_bonus = 0
    dodge = 0.045
class EvasionRuneY3(BaseRune):
    hp = 0
    hp_bonus = 0
    dodge = 0
class EvasionRuneP1(BaseRune):
    hp = 0
    hp_bonus = 0
    dodge = 0
class EvasionRuneP2(BaseRune):
    hp = 0
    hp_bonus = 0
    dodge = 0
class EvasionRuneP3(BaseRune):
    hp = 0
    hp_bonus = 0
    dodge = 0
class EvasionRuneO1(BaseRune):
    hp = 0
    hp_bonus = 0
    dodge = 0
class EvasionRuneO2(BaseRune):
    hp = 0
    hp_bonus = 0
    dodge = 0
class EvasionRuneO3(BaseRune):
    hp = 0
    hp_bonus = 0
    dodge = 0
class EvasionRuneO4(BaseRune):
    hp = 0
    hp_bonus = 0
    dodge = 0
class EvasionRuneR1(BaseRune):
    hp = 0
    hp_bonus = 0
    dodge = 0
class EvasionRuneR2(BaseRune):
    hp = 0
    hp_bonus = 0.12
    dodge = 0.16


class ArmorBreakRuneB1(BaseRune):
    atk = 0
    atk_bonus = 0
    armor_break = 0
class ArmorBreakRuneB2(BaseRune):
    atk = 0
    atk_bonus = 0
    armor_break = 0
class ArmorBreakRuneG1(BaseRune):
    atk = 0
    atk_bonus = 0
    armor_break = 0
class ArmorBreakRuneG2(BaseRune):
    atk = 0
    atk_bonus = 0
    armor_break = 0
class ArmorBreakRuneY1(BaseRune):
    atk = 125
    atk_bonus = 0
    armor_break = 2
class ArmorBreakRuneY2(BaseRune):
    atk = 155
    atk_bonus = 0
    armor_break = 3
class ArmorBreakRuneY3(BaseRune):
    atk = 185
    atk_bonus = 0
    armor_break = 4
class ArmorBreakRuneP1(BaseRune):
    atk = 0
    atk_bonus = 0
    armor_break = 0
class ArmorBreakRuneP2(BaseRune):
    atk = 0
    atk_bonus = 0
    armor_break = 0
class ArmorBreakRuneP3(BaseRune):
    atk = 0
    atk_bonus = 0
    armor_break = 0
class ArmorBreakRuneO1(BaseRune):
    atk = 0
    atk_bonus = 0
    armor_break = 0
class ArmorBreakRuneO2(BaseRune):
    atk = 0
    atk_bonus = 0
    armor_break = 0
class ArmorBreakRuneO3(BaseRune):
    atk = 0
    atk_bonus = 0
    armor_break = 0
class ArmorBreakRuneO4(BaseRune):
    atk = 0
    atk_bonus = 0
    armor_break = 0
class ArmorBreakRuneR1(BaseRune):
    atk = 0
    atk_bonus = 0
    armor_break = 0
class ArmorBreakRuneR2(BaseRune):
    atk = 620
    atk_bonus = 0.09
    armor_break = 13


class SkillDamageRuneB1(BaseRune):
    skill_damage = 0
    hit_rate = 0
class SkillDamageRuneB2(BaseRune):
    skill_damage = 0
    hit_rate = 0
class SkillDamageRuneG1(BaseRune):
    skill_damage = 0
    hit_rate = 0
class SkillDamageRuneG2(BaseRune):
    skill_damage = 0
    hit_rate = 0
class SkillDamageRuneY1(BaseRune):
    skill_damage = 0
    hit_rate = 0
class SkillDamageRuneY2(BaseRune):
    skill_damage = 0
    hit_rate = 0
class SkillDamageRuneY3(BaseRune):
    skill_damage = 0
    hit_rate = 0
class SkillDamageRuneP1(BaseRune):
    skill_damage = 0
    hit_rate = 0
class SkillDamageRuneP2(BaseRune):
    skill_damage = 0
    hit_rate = 0
class SkillDamageRuneP3(BaseRune):
    skill_damage = 0.14
    hit_rate = 0.05
class SkillDamageRuneO1(BaseRune):
    skill_damage = 0
    hit_rate = 0
class SkillDamageRuneO2(BaseRune):
    skill_damage = 0
    hit_rate = 0
class SkillDamageRuneO3(BaseRune):
    skill_damage = 0
    hit_rate = 0
class SkillDamageRuneO4(BaseRune):
    skill_damage = 0
    hit_rate = 0
class SkillDamageRuneR1(BaseRune):
    skill_damage = 0
    hit_rate = 0
class SkillDamageRuneR2(BaseRune):
    skill_damage = 0.26
    hit_rate = 0.13


class CritDamageRuneB1(BaseRune):
    crit_rate = 0
    crit_damage = 0
class CritDamageRuneB2(BaseRune):
    crit_rate = 0
    crit_damage = 0
class CritDamageRuneG1(BaseRune):
    crit_rate = 0
    crit_damage = 0
class CritDamageRuneG2(BaseRune):
    crit_rate = 0
    crit_damage = 0
class CritDamageRuneY1(BaseRune):
    crit_rate = 0
    crit_damage = 0
class CritDamageRuneY2(BaseRune):
    crit_rate = 0
    crit_damage = 0
class CritDamageRuneY3(BaseRune):
    crit_rate = 0
    crit_damage = 0
class CritDamageRuneP1(BaseRune):
    crit_rate = 0
    crit_damage = 0
class CritDamageRuneP2(BaseRune):
    crit_rate = 0
    crit_damage = 0
class CritDamageRuneP3(BaseRune):
    crit_rate = 0
    crit_damage = 0
class CritDamageRuneO1(BaseRune):
    crit_rate = 0.07
    crit_damage = 0.24
class CritDamageRuneO2(BaseRune):
    crit_rate = 0
    crit_damage = 0
class CritDamageRuneO3(BaseRune):
    crit_rate = 0
    crit_damage = 0
class CritDamageRuneO4(BaseRune):
    crit_rate = 0
    crit_damage = 0
class CritDamageRuneR1(BaseRune):
    crit_rate = 0
    crit_damage = 0
class CritDamageRuneR2(BaseRune):
    crit_rate = 0.13
    crit_damage = 0.44


class HpRuneB1(BaseRune):
    hp = 450
    atk_bonus = 0
    hp_bonus = 0
class HpRuneB2(BaseRune):
    hp = 582
    atk_bonus = 0
    hp_bonus = 0
class HpRuneG1(BaseRune):
    hp = 880
    atk_bonus = 0
    hp_bonus = 0
class HpRuneG2(BaseRune):
    hp = 1120
    atk_bonus = 0
    hp_bonus = 0
class HpRuneY1(BaseRune):
    hp = 1480
    atk_bonus = 0
    hp_bonus = 0.07
class HpRuneY2(BaseRune):
    hp = 1960
    atk_bonus = 0
    hp_bonus = 0.08
class HpRuneY3(BaseRune):
    hp = 2440
    atk_bonus = 0
    hp_bonus = 0.09
class HpRuneP1(BaseRune):
    hp = 0
    atk_bonus = 0
    hp_bonus = 0
class HpRuneP2(BaseRune):
    hp = 0
    atk_bonus = 0
    hp_bonus = 0
class HpRuneP3(BaseRune):
    hp = 4120
    atk_bonus = 0
    hp_bonus = 0.15
class HpRuneO1(BaseRune):
    hp = 0
    atk_bonus = 0
    hp_bonus = 0
class HpRuneO2(BaseRune):
    hp = 0
    atk_bonus = 0
    hp_bonus = 0
class HpRuneO3(BaseRune):
    hp = 6120
    atk_bonus = 0
    hp_bonus = 0.22
class HpRuneO4(BaseRune):
    hp = 0
    atk_bonus = 0
    hp_bonus = 0
class HpRuneR1(BaseRune):
    hp = 0
    atk_bonus = 0
    hp_bonus = 0
class HpRuneR2(BaseRune):
    hp = 8960
    atk_bonus = 0.06
    hp_bonus = 0.25


@dataclass
class AccuracyRune:
    B1 = AccuracyRuneB1()
    B2 = AccuracyRuneB2()
    G1 = AccuracyRuneG1()
    G2 = AccuracyRuneG2()
    Y1 = AccuracyRuneY1()
    Y2 = AccuracyRuneY2()
    Y3 = AccuracyRuneY3()
    P1 = AccuracyRuneP1()
    P2 = AccuracyRuneP2()
    P3 = AccuracyRuneP3()
    O1 = AccuracyRuneO1()
    O2 = AccuracyRuneO2()
    O3 = AccuracyRuneO3()
    O4 = AccuracyRuneO4()
    R1 = AccuracyRuneR1()
    R2 = AccuracyRuneR2()


@dataclass
class CritRateRune:
    B1 = CritRateRuneB1()
    B2 = CritRateRuneB2()
    G1 = CritRateRuneG1()
    G2 = CritRateRuneG2()
    Y1 = CritRateRuneY1()
    Y2 = CritRateRuneY2()
    Y3 = CritRateRuneY3()
    P1 = CritRateRuneP1()
    P2 = CritRateRuneP2()
    P3 = CritRateRuneP3()
    O1 = CritRateRuneO1()
    O2 = CritRateRuneO2()
    O3 = CritRateRuneO3()
    O4 = CritRateRuneO4()
    R1 = CritRateRuneR1()
    R2 = CritRateRuneR2()


@dataclass
class AttackRune:
    B1 = AttackRuneB1()
    B2 = AttackRuneB2()
    G1 = AttackRuneG1()
    G2 = AttackRuneG2()
    Y1 = AttackRuneY1()
    Y2 = AttackRuneY2()
    Y3 = AttackRuneY3()
    P1 = AttackRuneP1()
    P2 = AttackRuneP2()
    P3 = AttackRuneP3()
    O1 = AttackRuneO1()
    O2 = AttackRuneO2()
    O3 = AttackRuneO3()
    O4 = AttackRuneO4()
    R1 = AttackRuneR1()
    R2 = AttackRuneR2()


@dataclass
class EvasionRune:
    B1 = EvasionRuneB1()
    B2 = EvasionRuneB2()
    G1 = EvasionRuneG1()
    G2 = EvasionRuneG2()
    Y1 = EvasionRuneY1()
    Y2 = EvasionRuneY2()
    Y3 = EvasionRuneY3()
    P1 = EvasionRuneP1()
    P2 = EvasionRuneP2()
    P3 = EvasionRuneP3()
    O1 = EvasionRuneO1()
    O2 = EvasionRuneO2()
    O3 = EvasionRuneO3()
    O4 = EvasionRuneO4()
    R1 = EvasionRuneR1()
    R2 = EvasionRuneR2()


@dataclass
class ArmorBreakRune:
    B1 = ArmorBreakRuneB1()
    B2 = ArmorBreakRuneB2()
    G1 = ArmorBreakRuneG1()
    G2 = ArmorBreakRuneG2()
    Y1 = ArmorBreakRuneY1()
    Y2 = ArmorBreakRuneY2()
    Y3 = ArmorBreakRuneY3()
    P1 = ArmorBreakRuneP1()
    P2 = ArmorBreakRuneP2()
    P3 = ArmorBreakRuneP3()
    O1 = ArmorBreakRuneO1()
    O2 = ArmorBreakRuneO2()
    O3 = ArmorBreakRuneO3()
    O4 = ArmorBreakRuneO4()
    R1 = ArmorBreakRuneR1()
    R2 = ArmorBreakRuneR2()


@dataclass
class SkillDamageRune:
    B1 = SkillDamageRuneB1()
    B2 = SkillDamageRuneB2()
    G1 = SkillDamageRuneG1()
    G2 = SkillDamageRuneG2()
    Y1 = SkillDamageRuneY1()
    Y2 = SkillDamageRuneY2()
    Y3 = SkillDamageRuneY3()
    P1 = SkillDamageRuneP1()
    P2 = SkillDamageRuneP2()
    P3 = SkillDamageRuneP3()
    O1 = SkillDamageRuneO1()
    O2 = SkillDamageRuneO2()
    O3 = SkillDamageRuneO3()
    O4 = SkillDamageRuneO4()
    R1 = SkillDamageRuneR1()
    R2 = SkillDamageRuneR2()


@dataclass
class CritDamageRune:
    B1 = CritDamageRuneB1()
    B2 = CritDamageRuneB2()
    G1 = CritDamageRuneG1()
    G2 = CritDamageRuneG2()
    Y1 = CritDamageRuneY1()
    Y2 = CritDamageRuneY2()
    Y3 = CritDamageRuneY3()
    P1 = CritDamageRuneP1()
    P2 = CritDamageRuneP2()
    P3 = CritDamageRuneP3()
    O1 = CritDamageRuneO1()
    O2 = CritDamageRuneO2()
    O3 = CritDamageRuneO3()
    O4 = CritDamageRuneO4()
    R1 = CritDamageRuneR1()
    R2 = CritDamageRuneR2()


@dataclass
class HpRune:
    B1 = HpRuneB1()
    B2 = HpRuneB2()
    G1 = HpRuneG1()
    G2 = HpRuneG2()
    Y1 = HpRuneY1()
    Y2 = HpRuneY2()
    Y3 = HpRuneY3()
    P1 = HpRuneP1()
    P2 = HpRuneP2()
    P3 = HpRuneP3()
    O1 = HpRuneO1()
    O2 = HpRuneO2()
    O3 = HpRuneO3()
    O4 = HpRuneO4()
    R1 = HpRuneR1()
    R2 = HpRuneR2()


@dataclass
class Rune:
    empty = EmptyRune()
    accuracy = AccuracyRune
    crit_rate = CritRateRune
    attack = AttackRune
    evasion = EvasionRune
    armor_break = ArmorBreakRune
    skill_damage = SkillDamageRune
    crit_damage = CritDamageRune
    hp = HpRune


## Artifact
class BaseArtifact:
    energy = 0
    atk = 0
    hp = 0
    speed = 0
    atk_bonus = 0
    hp_bonus = 0
    hit_rate = 0
    true_damage = 0
    damage_reduction = 0
    damage_to_warriors = 0
    damage_to_assassins = 0
    damage_to_wanderers = 0
    damage_to_clerics = 0
    damage_to_mages = 0
    skill_damage_if_alliance = 0
    skill_damage_if_undead = 0
    skill_damage_if_hell = 0
    crit_rate_if_horde = 0
    crit_rate_if_elf = 0
    true_damage_if_heaven = 0


class EmptyArtifact(BaseArtifact):
    pass


class WarriorArtifactG1(BaseArtifact):
    atk = 0
    damage_to_warriors = 0
class WarriorArtifactG2(BaseArtifact):
    atk = 0
    damage_to_warriors = 0
class WarriorArtifactB1(BaseArtifact):
    atk = 0
    damage_to_warriors = 0
class WarriorArtifactB2(BaseArtifact):
    atk = 0
    damage_to_warriors = 0
class WarriorArtifactY1(BaseArtifact):
    atk = 0
    damage_to_warriors = 0
class WarriorArtifactY2(BaseArtifact):
    atk = 0
    damage_to_warriors = 0
class WarriorArtifactY3(BaseArtifact):
    atk = 0
    damage_to_warriors = 0
class WarriorArtifactP1(BaseArtifact):
    atk = 0
    damage_to_warriors = 0
class WarriorArtifactP2(BaseArtifact):
    atk = 0
    damage_to_warriors = 0
class WarriorArtifactP3(BaseArtifact):
    atk = 0
    damage_to_warriors = 0
class WarriorArtifactP4(BaseArtifact):
    atk = 0
    damage_to_warriors = 0
class WarriorArtifactO1(BaseArtifact):
    atk = 0
    damage_to_warriors = 0
class WarriorArtifactO2(BaseArtifact):
    atk = 0
    damage_to_warriors = 0
class WarriorArtifactO3(BaseArtifact):
    atk = 0
    damage_to_warriors = 0
class WarriorArtifactO4(BaseArtifact):
    atk = 0
    damage_to_warriors = 0
class WarriorArtifactO5(BaseArtifact):
    atk = 1280
    damage_to_warriors = 0.42


class AssassinArtifactG1(BaseArtifact):
    atk = 0
    damage_to_assassins = 0
class AssassinArtifactG2(BaseArtifact):
    atk = 0
    damage_to_assassins = 0
class AssassinArtifactB1(BaseArtifact):
    atk = 0
    damage_to_assassins = 0
class AssassinArtifactB2(BaseArtifact):
    atk = 0
    damage_to_assassins = 0
class AssassinArtifactY1(BaseArtifact):
    atk = 0
    damage_to_assassins = 0
class AssassinArtifactY2(BaseArtifact):
    atk = 0
    damage_to_assassins = 0
class AssassinArtifactY3(BaseArtifact):
    atk = 0
    damage_to_assassins = 0
class AssassinArtifactP1(BaseArtifact):
    atk = 0
    damage_to_assassins = 0
class AssassinArtifactP2(BaseArtifact):
    atk = 0
    damage_to_assassins = 0
class AssassinArtifactP3(BaseArtifact):
    atk = 0
    damage_to_assassins = 0
class AssassinArtifactP4(BaseArtifact):
    atk = 0
    damage_to_assassins = 0
class AssassinArtifactO1(BaseArtifact):
    atk = 0
    damage_to_assassins = 0
class AssassinArtifactO2(BaseArtifact):
    atk = 0
    damage_to_assassins = 0
class AssassinArtifactO3(BaseArtifact):
    atk = 0
    damage_to_assassins = 0
class AssassinArtifactO4(BaseArtifact):
    atk = 0
    damage_to_assassins = 0
class AssassinArtifactO5(BaseArtifact):
    atk = 1280
    damage_to_assassins = 0.42


class WandererArtifactG1(BaseArtifact):
    atk = 0
    damage_to_wanderers = 0
class WandererArtifactG2(BaseArtifact):
    atk = 0
    damage_to_wanderers = 0
class WandererArtifactB1(BaseArtifact):
    atk = 0
    damage_to_wanderers = 0
class WandererArtifactB2(BaseArtifact):
    atk = 0
    damage_to_wanderers = 0
class WandererArtifactY1(BaseArtifact):
    atk = 0
    damage_to_wanderers = 0
class WandererArtifactY2(BaseArtifact):
    atk = 0
    damage_to_wanderers = 0
class WandererArtifactY3(BaseArtifact):
    atk = 0
    damage_to_wanderers = 0
class WandererArtifactP1(BaseArtifact):
    atk = 0
    damage_to_wanderers = 0
class WandererArtifactP2(BaseArtifact):
    atk = 0
    damage_to_wanderers = 0
class WandererArtifactP3(BaseArtifact):
    atk = 0
    damage_to_wanderers = 0
class WandererArtifactP4(BaseArtifact):
    atk = 0
    damage_to_wanderers = 0
class WandererArtifactO1(BaseArtifact):
    atk = 0
    damage_to_wanderers = 0
class WandererArtifactO2(BaseArtifact):
    atk = 0
    damage_to_wanderers = 0
class WandererArtifactO3(BaseArtifact):
    atk = 0
    damage_to_wanderers = 0
class WandererArtifactO4(BaseArtifact):
    atk = 0
    damage_to_wanderers = 0
class WandererArtifactO5(BaseArtifact):
    atk = 1280
    damage_to_wanderers = 0.42


class ClericArtifactG1(BaseArtifact):
    atk = 0
    damage_to_clerics = 0
class ClericArtifactG2(BaseArtifact):
    atk = 0
    damage_to_clerics = 0
class ClericArtifactB1(BaseArtifact):
    atk = 0
    damage_to_clerics = 0
class ClericArtifactB2(BaseArtifact):
    atk = 0
    damage_to_clerics = 0
class ClericArtifactY1(BaseArtifact):
    atk = 0
    damage_to_clerics = 0
class ClericArtifactY2(BaseArtifact):
    atk = 0
    damage_to_clerics = 0
class ClericArtifactY3(BaseArtifact):
    atk = 0
    damage_to_clerics = 0
class ClericArtifactP1(BaseArtifact):
    atk = 0
    damage_to_clerics = 0
class ClericArtifactP2(BaseArtifact):
    atk = 0
    damage_to_clerics = 0
class ClericArtifactP3(BaseArtifact):
    atk = 0
    damage_to_clerics = 0
class ClericArtifactP4(BaseArtifact):
    atk = 0
    damage_to_clerics = 0
class ClericArtifactO1(BaseArtifact):
    atk = 0
    damage_to_clerics = 0
class ClericArtifactO2(BaseArtifact):
    atk = 0
    damage_to_clerics = 0
class ClericArtifactO3(BaseArtifact):
    atk = 0
    damage_to_clerics = 0
class ClericArtifactO4(BaseArtifact):
    atk = 0
    damage_to_clerics = 0
class ClericArtifactO5(BaseArtifact):
    atk = 1280
    damage_to_clerics = 0.42


class MageArtifactG1(BaseArtifact):
    atk = 0
    damage_to_mages = 0
class MageArtifactG2(BaseArtifact):
    atk = 0
    damage_to_mages = 0
class MageArtifactB1(BaseArtifact):
    atk = 0
    damage_to_mages = 0
class MageArtifactB2(BaseArtifact):
    atk = 0
    damage_to_mages = 0
class MageArtifactY1(BaseArtifact):
    atk = 0
    damage_to_mages = 0
class MageArtifactY2(BaseArtifact):
    atk = 0
    damage_to_mages = 0
class MageArtifactY3(BaseArtifact):
    atk = 0
    damage_to_mages = 0
class MageArtifactP1(BaseArtifact):
    atk = 0
    damage_to_mages = 0
class MageArtifactP2(BaseArtifact):
    atk = 0
    damage_to_mages = 0
class MageArtifactP3(BaseArtifact):
    atk = 0
    damage_to_mages = 0
class MageArtifactP4(BaseArtifact):
    atk = 0
    damage_to_mages = 0
class MageArtifactO1(BaseArtifact):
    atk = 0
    damage_to_mages = 0
class MageArtifactO2(BaseArtifact):
    atk = 0
    damage_to_mages = 0
class MageArtifactO3(BaseArtifact):
    atk = 0
    damage_to_mages = 0
class MageArtifactO4(BaseArtifact):
    atk = 0
    damage_to_mages = 0
class MageArtifactO5(BaseArtifact):
    atk = 1280
    damage_to_mages = 0.42


class EyeOfHeavenO1(BaseArtifact):
    atk_bonus = 0
    hit_rate = 0
class EyeOfHeavenO2(BaseArtifact):
    atk_bonus = 0
    hit_rate = 0
class EyeOfHeavenO3(BaseArtifact):
    atk_bonus = 0
    hit_rate = 0
class EyeOfHeavenO4(BaseArtifact):
    atk_bonus = 0
    hit_rate = 0
class EyeOfHeavenO5(BaseArtifact):
    atk_bonus = 0.12
    hit_rate = 0.08


class WindWalkerO1(BaseArtifact):
    speed = 0
    hp_bonus = 0
class WindWalkerO2(BaseArtifact):
    speed = 0
    hp_bonus = 0
class WindWalkerO3(BaseArtifact):
    speed = 0
    hp_bonus = 0
class WindWalkerO4(BaseArtifact):
    speed = 0
    hp_bonus = 0
class WindWalkerO5(BaseArtifact):
    speed = 42
    hp_bonus = 0.1


class ScorchingSunO1(BaseArtifact):
    hp_bonus = 0
    damage_reduction = 0
class ScorchingSunO2(BaseArtifact):
    hp_bonus = 0
    damage_reduction = 0
class ScorchingSunO3(BaseArtifact):
    hp_bonus = 0
    damage_reduction = 0
class ScorchingSunO4(BaseArtifact):
    hp_bonus = 0
    damage_reduction = 0
class ScorchingSunO5(BaseArtifact):
    hp_bonus = 0.08
    damage_reduction = 0.12


class DragonbloodO1(BaseArtifact):
    atk_bonus = 0
    true_damage = 0
class DragonbloodO2(BaseArtifact):
    atk_bonus = 0
    true_damage = 0
class DragonbloodO3(BaseArtifact):
    atk_bonus = 0
    true_damage = 0
class DragonbloodO4(BaseArtifact):
    atk_bonus = 0
    true_damage = 0
class DragonbloodO5(BaseArtifact):
    atk_bonus = 0.08
    true_damage = 0.12


class SoundStepO1(BaseArtifact):
    energy = 0
    atk = 0
class SoundStepO2(BaseArtifact):
    energy = 0
    atk = 0
class SoundStepO3(BaseArtifact):
    energy = 0
    atk = 0
class SoundStepO4(BaseArtifact):
    energy = 0
    atk = 0
class SoundStepO5(BaseArtifact):
    energy = 240
    atk = 240


class KnightsVowO1(BaseArtifact):
    atk = 0
    damage_to_clerics = 0
    skill_damage_if_alliance = 0
class KnightsVowO2(BaseArtifact):
    atk = 0
    damage_to_clerics = 0
    skill_damage_if_alliance = 0
class KnightsVowO3(BaseArtifact):
    atk = 0
    damage_to_clerics = 0
    skill_damage_if_alliance = 0
class KnightsVowO4(BaseArtifact):
    atk = 0
    damage_to_clerics = 0
    skill_damage_if_alliance = 0
class KnightsVowO5(BaseArtifact):
    atk = 1280
    damage_to_clerics = 0.42
    skill_damage_if_alliance = 0.25


class PrimevalSoulO1(BaseArtifact):
    atk = 0
    damage_to_wanderers = 0
    crit_rate_if_horde = 0
class PrimevalSoulO2(BaseArtifact):
    atk = 0
    damage_to_wanderers = 0
    crit_rate_if_horde = 0
class PrimevalSoulO3(BaseArtifact):
    atk = 0
    damage_to_wanderers = 0
    crit_rate_if_horde = 0
class PrimevalSoulO4(BaseArtifact):
    atk = 0
    damage_to_wanderers = 0
    crit_rate_if_horde = 0
class PrimevalSoulO5(BaseArtifact):
    atk = 1280
    damage_to_wanderers = 0.42
    crit_rate_if_horde = 0.09


class QueensCrownO1(BaseArtifact):
    speed = 0
    hp_bonus = 0
    crit_rate_if_elf = 0
class QueensCrownO2(BaseArtifact):
    speed = 0
    hp_bonus = 0
    crit_rate_if_elf = 0
class QueensCrownO3(BaseArtifact):
    speed = 0
    hp_bonus = 0
    crit_rate_if_elf = 0
class QueensCrownO4(BaseArtifact):
    speed = 0
    hp_bonus = 0
    crit_rate_if_elf = 0
class QueensCrownO5(BaseArtifact):
    speed = 42
    hp_bonus = 0.1
    crit_rate_if_elf = 0.09


class SoulTorrentO1(BaseArtifact):
    atk_bonus = 0
    hit_rate = 0
    skill_damage_if_undead = 0
class SoulTorrentO2(BaseArtifact):
    atk_bonus = 0
    hit_rate = 0
    skill_damage_if_undead = 0
class SoulTorrentO3(BaseArtifact):
    atk_bonus = 0
    hit_rate = 0
    skill_damage_if_undead = 0
class SoulTorrentO4(BaseArtifact):
    atk_bonus = 0
    hit_rate = 0
    skill_damage_if_undead = 0
class SoulTorrentO5(BaseArtifact):
    atk_bonus = 0.12
    hit_rate = 0.08
    skill_damage_if_undead = 0.25


class GiftOfCreationO1(BaseArtifact):
    hp_bonus = 0
    damage_reduction = 0
    true_damage_if_heaven = 0
class GiftOfCreationO2(BaseArtifact):
    hp_bonus = 0
    damage_reduction = 0
    true_damage_if_heaven = 0
class GiftOfCreationO3(BaseArtifact):
    hp_bonus = 0
    damage_reduction = 0
    true_damage_if_heaven = 0
class GiftOfCreationO4(BaseArtifact):
    hp_bonus = 0
    damage_reduction = 0
    true_damage_if_heaven = 0
class GiftOfCreationO5(BaseArtifact):
    hp_bonus = 0.1
    damage_reduction = 0.15
    true_damage_if_heaven = 0.12


class EternalCurseO1(BaseArtifact):
    atk_bonus = 0
    hit_rate = 0
    skill_damage_if_hell = 0
class EternalCurseO2(BaseArtifact):
    atk_bonus = 0
    hit_rate = 0
    skill_damage_if_hell = 0
class EternalCurseO3(BaseArtifact):
    atk_bonus = 0
    hit_rate = 0
    skill_damage_if_hell = 0
class EternalCurseO4(BaseArtifact):
    atk_bonus = 0
    hit_rate = 0
    skill_damage_if_hell = 0
class EternalCurseO5(BaseArtifact):
    atk_bonus = 0.12
    hit_rate = 0.08
    skill_damage_if_hell = 0.25


@dataclass
class WarriorArtifact:
    G1 = WarriorArtifactG1()
    G2 = WarriorArtifactG2()
    B1 = WarriorArtifactB1()
    B2 = WarriorArtifactB2()
    Y1 = WarriorArtifactY1()
    Y2 = WarriorArtifactY2()
    Y3 = WarriorArtifactY3()
    P1 = WarriorArtifactP1()
    P2 = WarriorArtifactP2()
    P3 = WarriorArtifactP3()
    P4 = WarriorArtifactP4()
    O1 = WarriorArtifactO1()
    O2 = WarriorArtifactO2()
    O3 = WarriorArtifactO3()
    O4 = WarriorArtifactO4()
    O5 = WarriorArtifactO5()


@dataclass
class AssassinArtifact:
    G1 = AssassinArtifactG1()
    G2 = AssassinArtifactG2()
    B1 = AssassinArtifactB1()
    B2 = AssassinArtifactB2()
    Y1 = AssassinArtifactY1()
    Y2 = AssassinArtifactY2()
    Y3 = AssassinArtifactY3()
    P1 = AssassinArtifactP1()
    P2 = AssassinArtifactP2()
    P3 = AssassinArtifactP3()
    P4 = AssassinArtifactP4()
    O1 = AssassinArtifactO1()
    O2 = AssassinArtifactO2()
    O3 = AssassinArtifactO3()
    O4 = AssassinArtifactO4()
    O5 = AssassinArtifactO5()


@dataclass
class WandererArtifact:
    G1 = WandererArtifactG1()
    G2 = WandererArtifactG2()
    B1 = WandererArtifactB1()
    B2 = WandererArtifactB2()
    Y1 = WandererArtifactY1()
    Y2 = WandererArtifactY2()
    Y3 = WandererArtifactY3()
    P1 = WandererArtifactP1()
    P2 = WandererArtifactP2()
    P3 = WandererArtifactP3()
    P4 = WandererArtifactP4()
    O1 = WandererArtifactO1()
    O2 = WandererArtifactO2()
    O3 = WandererArtifactO3()
    O4 = WandererArtifactO4()
    O5 = WandererArtifactO5()


@dataclass
class ClericArtifact:
    G1 = ClericArtifactG1()
    G2 = ClericArtifactG2()
    B1 = ClericArtifactB1()
    B2 = ClericArtifactB2()
    Y1 = ClericArtifactY1()
    Y2 = ClericArtifactY2()
    Y3 = ClericArtifactY3()
    P1 = ClericArtifactP1()
    P2 = ClericArtifactP2()
    P3 = ClericArtifactP3()
    P4 = ClericArtifactP4()
    O1 = ClericArtifactO1()
    O2 = ClericArtifactO2()
    O3 = ClericArtifactO3()
    O4 = ClericArtifactO4()
    O5 = ClericArtifactO5()


@dataclass
class MageArtifact:
    G1 = MageArtifactG1()
    G2 = MageArtifactG2()
    B1 = MageArtifactB1()
    B2 = MageArtifactB2()
    Y1 = MageArtifactY1()
    Y2 = MageArtifactY2()
    Y3 = MageArtifactY3()
    P1 = MageArtifactP1()
    P2 = MageArtifactP2()
    P3 = MageArtifactP3()
    P4 = MageArtifactP4()
    O1 = MageArtifactO1()
    O2 = MageArtifactO2()
    O3 = MageArtifactO3()
    O4 = MageArtifactO4()
    O5 = MageArtifactO5()


@dataclass
class EyeOfHeaven:
    O1 = EyeOfHeavenO1()
    O2 = EyeOfHeavenO2()
    O3 = EyeOfHeavenO3()
    O4 = EyeOfHeavenO4()
    O5 = EyeOfHeavenO5()


@dataclass
class WindWalker:
    O1 = WindWalkerO1()
    O2 = WindWalkerO2()
    O3 = WindWalkerO3()
    O4 = WindWalkerO4()
    O5 = WindWalkerO5()


@dataclass
class ScorchingSun:
    O1 = ScorchingSunO1()
    O2 = ScorchingSunO2()
    O3 = ScorchingSunO3()
    O4 = ScorchingSunO4()
    O5 = ScorchingSunO5()


@dataclass
class Dragonblood:
    O1 = DragonbloodO1()
    O2 = DragonbloodO2()
    O3 = DragonbloodO3()
    O4 = DragonbloodO4()
    O5 = DragonbloodO5()


@dataclass
class SoundStep:
    O1 = SoundStepO1()
    O2 = SoundStepO2()
    O3 = SoundStepO3()
    O4 = SoundStepO4()
    O5 = SoundStepO5()


@dataclass
class KnightsVow:
    O1 = KnightsVowO1()
    O2 = KnightsVowO2()
    O3 = KnightsVowO3()
    O4 = KnightsVowO4()
    O5 = KnightsVowO5()


@dataclass
class PrimevalSoul:
    O1 = PrimevalSoulO1()
    O2 = PrimevalSoulO2()
    O3 = PrimevalSoulO3()
    O4 = PrimevalSoulO4()
    O5 = PrimevalSoulO5()


@dataclass
class QueensCrown:
    O1 = QueensCrownO1()
    O2 = QueensCrownO2()
    O3 = QueensCrownO3()
    O4 = QueensCrownO4()
    O5 = QueensCrownO5()


@dataclass
class SoulTorrent:
    O1 = SoulTorrentO1()
    O2 = SoulTorrentO2()
    O3 = SoulTorrentO3()
    O4 = SoulTorrentO4()
    O5 = SoulTorrentO5()


@dataclass
class GiftOfCreation:
    O1 = GiftOfCreationO1()
    O2 = GiftOfCreationO2()
    O3 = GiftOfCreationO3()
    O4 = GiftOfCreationO4()
    O5 = GiftOfCreationO5()


@dataclass
class EternalCurse:
    O1 = EternalCurseO1()
    O2 = EternalCurseO2()
    O3 = EternalCurseO3()
    O4 = EternalCurseO4()
    O5 = EternalCurseO5()


@dataclass
class Artifact:
    empty = EmptyArtifact()
    warrior = WarriorArtifact
    assassin = AssassinArtifact
    wanderer = WandererArtifact
    cleric = ClericArtifact
    mage = MageArtifact
    eye_of_heaven = EyeOfHeaven
    wind_walker = WindWalker
    scorching_sun = ScorchingSun
    dragonblood = Dragonblood
    sound_step = SoundStep
    knights_vow = KnightsVow
    primeval_soul = PrimevalSoul
    queens_crown = QueensCrown
    soul_torrent = SoulTorrent
    gift_of_creation = GiftOfCreation
    eternal_curse = EternalCurse


## Aura
class Aura:
    def __init__(self, heroes):
        alliance_count = len([h for h in heroes if h.faction == Faction.ALLIANCE])
        horde_count = len([h for h in heroes if h.faction == Faction.HORDE])
        elf_count = len([h for h in heroes if h.faction == Faction.ELF])
        undead_count = len([h for h in heroes if h.faction == Faction.UNDEAD])
        heaven_count = len([h for h in heroes if h.faction == Faction.HEAVEN])
        hell_count = len([h for h in heroes if h.faction == Faction.HELL])

        self.atk_bonus = 0
        self.hp_bonus = 0
        self.dodge = 0
        self.crit_rate = 0
        self.armor_break_bonus = 0
        self.control_immune = 0

        if alliance_count == 6:
            self.dodge = 0.05
            self.hp_bonus = 0.2
        elif horde_count == 6:
            self.atk_bonus = 0.15
            self.hp_bonus = 0.2
        elif elf_count == 6:
            self.crit_rate = 0.05
            self.hp_bonus = 0.2
        elif undead_count == 6:
            self.armor_break_bonus = 0.2
            self.hp_bonus = 0.2
        elif heaven_count == 6:
            self.control_immune = 0.3
            self.hp_bonus = 0.2
        elif hell_count == 6:
            self.control_immune = 0.3
            self.hp_bonus = 0.2
        elif min([alliance_count, horde_count, elf_count, undead_count, heaven_count, hell_count]) == 1:
            self.atk_bonus = 0.1
            self.hp_bonus = 0.1
        elif min([heaven_count, hell_count]) == 3:
            self.atk_bonus = 0.135
            self.hp_bonus = 0.16
        elif min([alliance_count, elf_count]) == 3:
            self.atk_bonus = 0.1
            self.hp_bonus = 0.08
        elif min([horde_count, undead_count]) == 3:
            self.atk_bonus = 0.08
            self.hp_bonus = 0.1
        elif min([alliance_count, elf_count, heaven_count]) == 2:
            self.atk_bonus = 0.11
            self.hp_bonus = 0.13
        elif min([horde_count, undead_count, hell_count]) == 2:
            self.atk_bonus = 0.13
            self.hp_bonus = 0.11


## Effects
class BaseEffect:
    def kill(self):
        self.holder.effects = [e for e in self.holder.effects if e.turns > 0]


class Poison(BaseEffect):
    def __init__(self, source, holder, power, turns, skill=False, name=''):
        self.source = source
        self.holder = holder
        self.power = power
        self.turns = turns
        self.skill = skill
        self.name = name

    def tick(self):
        if self.turns == 0:
            self.kill()
        elif not self.holder.is_dead:
            damage_components = self.source.compute_damage \
                        (self.holder, self.power, skill=self.skill) # check if armor applies to poison
            dmg = damage_components['Total damage']
            crit = True if damage_components['Crit damage'] > 0 else False
            crit_str = ', crit' if crit else ''

            self.holder.hp -= dmg
            self.turns -= 1
            log_text = '\n{} takes {} damage (poison from {} ({}{}), {} turns left)' \
                        .format(self.holder.str_id, round(dmg), self.source.str_id, self.name, crit_str, self.turns)
            self.source.game.log += log_text
            self.holder.has_taken_damage(self.source)


@dataclass
class Effect:
    poison = Poison
