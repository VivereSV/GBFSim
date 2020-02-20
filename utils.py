AUTO_THRESHOLDS = [0, 300000, 400000, 500000, 600000]
AUTO_REDUCTIONS = [0, 0.2, 0.4, 0.95, 0.99, 1]
OUGI_THRESHOLDS = [0, 1500000, 1700000, 1800000, 2500000]
OUGI_REDUCTIONS = [0, 0.4, 0.7, 0.95, 0.99, 1]

def apply_auto_damage_cap(damage, cap_up, damage_type='auto'):
    if damage_type == 'auto':
        thresholds = [threshold * (1 + cap_up) for threshold in AUTO_THRESHOLDS]
        reductions = AUTO_REDUCTIONS
    elif damage_type == 'ougi':
        thresholds = [threshold * (1 + cap_up) for threshold in OUGI_THRESHOLDS]
        reductions = OUGI_REDUCTIONS
    else:
        return -1
    thresholds.append(10000000)

    capped_damage = 0
    for i in range(1, len(thresholds)):
        threshold = thresholds[i]
        if damage > threshold:
            reduced_damage = (threshold - thresholds[i - 1]) * (1 - reductions[i - 1])
            capped_damage += reduced_damage
        else:
            reduced_damage = (damage - thresholds[i - 1]) * (1 - reductions[i - 1])
            capped_damage += reduced_damage
            break
    return capped_damage
