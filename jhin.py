from damage import calculate_final_damage


class Jhin:
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

        if self.attack_count == 4:
            physical_damage = self.ad * 1.20
            self.attack_count = 0
            print("Jhin does BONUS DAMAGE!")
        else:
            print("Normal attack")

        total_damage = calculate_final_damage(
            physical_damage,
            magic_damage,
            enemy.ar,
            enemy.mr
        )

        enemy.hp = max(0, enemy.hp - total_damage)

        print(f"Jhin dealt {total_damage} damage!")
        print(f"Enemy HP: {enemy.hp}")

        if enemy.hp == 0:
            print("Killer Performance!")

        return total_damage

    

    
