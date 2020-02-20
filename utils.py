AUTO_THRESHOLDS = [0, 300000, 400000, 500000, 600000, 10000000]
AUTO_REDUCTIONS = [0, 0.2, 0.4, 0.95, 0.99, 1]

def apply_auto_damage_cap(damage, cap_up):
    thresholds = [threshold * (1 + cap_up) for threshold in AUTO_THRESHOLDS]
    capped_damage = 0
    for i in range(1, len(thresholds)):
        threshold = thresholds[i]
        if damage > threshold:
            reduced_damage = (threshold - thresholds[i - 1]) * (1 - AUTO_REDUCTIONS[i - 1])
            capped_damage += reduced_damage
        else:
            reduced_damage = (damage - thresholds[i - 1]) * (1 - AUTO_REDUCTIONS[i - 1])
            capped_damage += reduced_damage
            break
    return capped_damage
