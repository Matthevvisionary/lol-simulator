def calculate_final_damage(physical_damage, magic_damage, armor, magic_resist):
    final_physical_damage = max(0, physical_damage - armor)
    final_magic_damage = max(0, magic_damage - magic_resist)

    total_damage = final_physical_damage + final_magic_damage

    return total_damage
