from damage import calculate_final_damage


class Yone:
    def __init__(self, hp, ad, md, ar, mr):
        self.hp = hp
        self.ad = ad
        self.md = md
        self.ar = ar
        self.mr = mr
        self.attack_count = 0


    def auto_attack(self, enemy):
        self.attack_count += 1

        physical_damage = self.ad
        magic_damage = 0

        if self.attack_count == 2:
            physical_damage = self.ad / 2
            magic_damage = self.ad / 2
            self.attack_count = 0
            print("Yone's passive activates! He deals magic damage and attack damage!")
        else:
            print("Normal attack")

        total_damage = calculate_final_damage(
            physical_damage,
            magic_damage,
            enemy.ar,
            enemy.mr
        )

        enemy.hp = max(0, enemy.hp - total_damage)

        print(f"Yone dealt {total_damage} damage!")
        print(f"Enemy HP: {enemy.hp}")

        return total_damage