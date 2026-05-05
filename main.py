champ = {
    "Nasus": 631,
    "Cho'Gath": 644,
    "Nautilus": 646,
    "Aatrox": 650
}

from jhin import Jhin
from yone import Yone
from zed import Zed
from minions import caster_minion, melee_minion, cannon_minion


champion_pool = {
    "jhin": {
        "class": Jhin,
        "name": "Jhin",
        "stats": {"hp": 700, "ad": 80, "md": 0, "ar": 30, "mr": 30}
    },
    "yone": {
        "class": Yone,
        "name": "Yone",
        "stats": {"hp": 800, "ad": 75, "md": 0, "ar": 35, "mr": 30}
    },
    "zed": {
        "class": Zed,
        "name": "Zed",
        "stats": {"hp": 750, "ad": 85, "md": 0, "ar": 32, "mr": 30}
    }
}

print("LoL Simulator v0.2.0") 

def choose_champion(choice):
    champion_data = champion_pool.get(choice)

    if champion_data is None:
        print("Champion not found.")
        return None

    champion_class = champion_data["class"]
    champion_stats = champion_data["stats"]

    return champion_class(**champion_stats)


player_choice = input("Welcome to League of Legends Simulator! Choose your champion: ").lower()
champion_data = champion_pool.get(player_choice)

player = choose_champion(player_choice)

enemy = caster_minion

if player:
    print(f"You chose {champion_data['name']}!")
    print(f"Enemy: {enemy.name}")

    while enemy.hp > 0 and player.hp > 0:
        player.auto_attack(enemy)
        print(f"{enemy.name} HP: {enemy.hp}")

        if enemy.hp <= 0:
            print(f"{enemy.name} died!")
            break

    # enemy attacks back (optional for now)

