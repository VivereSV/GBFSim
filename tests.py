import utils
import character

print(utils.apply_auto_damage_cap(500000, 0))
andira = character.Character()
andira.double_attack = 1
andira.triple_attack = 0.35
andira.auto_cap = 0.1
for i in range(10):
    print(andira.attack_foe(50, 1.33))
print(andira.total_damage)