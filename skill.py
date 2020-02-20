class Skill:
    def __init__(self):
        self.max_cooldown = 0
        self.cooldown = 0
        self.damage_multiplier = 0
        self.damage_cap = 0
        self.ally_buffs = []
        self.ally_debuffs = []
        self.foe_buffs = []
        self.foe_debuffs = []

    def use(self, attack):
        self.cooldown = self.max_cooldown

        #TODO: Apply damage cap lmao
        return self.damage_multiplier * attack