import random
# import math
dodged = False
attack_dodged = False
# inputs
tarnished_lvl = int(input("tarnished level:  "))
sword_lvl = int(input("rivers of blood level:  "))
enemy_options = input("Enemy (soldier / knight / demigod / dragon):  ").lower()


# enemy types
enemies = {
    "soldier": {"hp": 300, "difficulty": 0.8, "runes": 500},
    "knight": {"hp": 600, "difficulty": 1.0, "runes": 3000},
    "demigod": {"hp": 1200, "difficulty": 1.4, "runes": 20000},
    "dragon": {"hp": 2000, "difficulty": 1.8, "runes": 50000},
}
if enemy_options not in enemies:
    print("thats not an enemy. get a glasses you fell off a cliff.")
enemy_hp = enemies[enemy_options]["hp"]
enemy_diff = enemies[enemy_options]["difficulty"]
enemy_runes = enemies[enemy_options]['runes']

# player stats
player_hp = 50
player_dmg = 20
base_hp = tarnished_lvl * player_hp
base_dmg = tarnished_lvl * player_dmg
print(f"you have {base_hp} HP")
rng = random.uniform(0.85, 1.15)
attack_dodged = 0.0
death_chance = 0.0


# weapon stats
sword_dmg = 20
max_damage = (sword_lvl * sword_dmg)+(player_dmg*tarnished_lvl)
print(f"you have {max_damage} DAMAGE")

# ===== action phase ======
while base_hp > 0 or enemy_hp > 0:
    action = input(
        "what's your move? attack / greed  / dodge / heal:  ").lower()

    if action == "attack":
        attack_dodged = 0.80
        damage = int(max_damage / enemy_diff)
        if random.random() < attack_dodged:
            print("Enemy dodged your attack!")
            damage = 0
        else:
            enemy_hp -= damage
            print(f"You dealt {damage}")

    elif action == "greed":
        damage = int(max_damage * 1.5)
        enemy_hp -= damage
        print(f"Greedy hit for {damage}")

    elif action == "dodge":
        print("You dodged!")
        dodged = True
    elif action == "heal":
        base_hp = (base_hp + 50) - enemy_damage

    print(f"Enemy HP now: {enemy_hp}")

    # enemy turn
    if dodged:
        enemy_damage = 0
        print("Enemy attack missed!")
    else:
        enemy_damage = round(random.randint(80, 100)*enemy_diff)
    base_hp -= enemy_damage
    print(f"Enemy hits you for {enemy_damage}")
    print(f"Your HP: {base_hp}")

    if action == "greed" and random.random() < death_chance:
        print("greedy bitch")
        print("You died")
        print("Get good")

    elif base_hp <= 0 or enemy_hp <= 0:
        print("Game over")
        break
