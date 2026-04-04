champ = {
    "Nasus": 631,
    "Cho'Gath": 644,
    "Nautilus": 646,
    "Aatrox": 650
}

jhin_ad = 59
enemy_hp = 590

attack = {
    "A": 59,
    "a": 59
}

attack_count = 0

print("LoL Simulator v0.1.0 — Initial Release (Prototype): Jhin's Killer Performance")
user_input = input("\nWelcome to League of Legends Simulator! You are Jhin! Put on a killer performance! Press A to attack the enemy: ")

while enemy_hp > 0:
    damage = attack[user_input]

    attack_count += 1

    if attack_count == 4:
        damage = damage * 1.20
        print("Jhin does BONUS DAMAGE!")
        attack_count = 0
    else:
        print("Normal attack")

    enemy_hp = max(0, enemy_hp - damage)

    print("Enemy HP:", enemy_hp)

if enemy_hp == 0:
    print("Killer Performance!")