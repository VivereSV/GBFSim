import random
import utils


class Character:
    def __init__(self):
        self.attack = 10000
        self.hp = 2000
        self.defense = 1
        self.double_attack = 0.0
        self.triple_attack = 0.0
        self.max_bar = 100
        self.current_bar = 30
        self.buffs = []
        self.debuffs = []
        self.skill_one = None
        self.skill_two = None
        self.skill_three = None
        self.skill_four = None
        self.total_damage = 0
        self.auto_cap = 0
        self.ougi_cap = 0
        self.skill_cap = 0

    #Damage multiplier should include grid, buffs, debuffs, and enemy defense
    #Return a list of damage instances
    def attack_foe(self, damage_multiplier, seraphic):
        num_attacks = 1
        triple_attack_roll = random.uniform(0, 1)
        double_attack_roll = random.uniform(0, 1)
        if triple_attack_roll < self.triple_attack:
            num_attacks = 3
        elif double_attack_roll < self.double_attack:
            num_attacks = 2
        damage = []
        for i in range(num_attacks):
            variance = random.uniform(0.95, 1.05)
            damage.append(utils.apply_auto_damage_cap(variance * damage_multiplier * self.attack, self.auto_cap) * seraphic)
        self.total_damage += sum(damage)
        return damage