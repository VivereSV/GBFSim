class Character:
    def __init__(self):
        self.attack = 10000
        self.hp = 2000
        self.defense = 1
        self.double_attack = 0
        self.triple_attack = 0
        self.max_bar = 100
        self.current_bar = 30
        self.buffs = []
        self.debuffs = []
        self.skill_one = None
        self.skill_two = None
        self.skill_three = None
        self.skill_four = None

    def attack(self):
