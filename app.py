# new input deletes clears old logs form terminal

import random
from utils.enemy_stats import enemies
from utils.validate_enemy import ValidateEnemy
import time
import os


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


clear_screen()


time.sleep(1)

dodged = False
attack_dodged = False
# inputs
tarnished_lvl = int(input("tarnished level:  "))
sword_lvl = int(input("Weapon upgrade (0-10):  "))
enemy_options = ''

enemy_options = ValidateEnemy()

enemy_hp = enemies[enemy_options]["hp"]
enemy_diff = enemies[enemy_options]["difficulty"]
enemy_runes = enemies[enemy_options]['runes']

# player stats

player_hp = 50
player_dmg = 20
player_mana = 10
base_hp = tarnished_lvl * player_hp
base_dmg = tarnished_lvl * player_dmg
base_mana = tarnished_lvl * player_mana
print(f"You have {base_hp} HP")
print(f"You have {base_mana} Mana")
print(f"Enemy has {enemy_hp} HP")
rng = random.uniform(0.85, 1.15)
attack_missed = 0.0
death_chance = 0.0
enemy_hit = 0.0

# weapon stats
sword_dmg = 20
max_damage = (sword_lvl * sword_dmg)+(player_dmg*tarnished_lvl)
print(f"You have {max_damage} DAMAGE")
magic_damage = round(enemy_hp * 0.4)
frostbite = round(magic_damage + 20 % enemy_hp)


# ===== action phase ======
while base_hp > 0 or enemy_hp > 0:
    time.sleep(1)
    action = input(
        "what's your move? attack/ magic / greed  / dodge / heal:  ").lower()

    clear_screen()

    if action == "attack":
        attack_missed = 0.2
        damage = int(max_damage / enemy_diff)
        if random.random() < attack_missed:
            print("Enemy dodged your attack!")
            damage = 0
        else:
            enemy_hp = enemy_hp - damage
            print(f"You dealt {damage} damage!")
        time.sleep(1)

    elif action == "magic":
        spell = input(
            "choose your spell: fireball / ice blizzard / lightning / wind slash ...  ").lower()
        if spell == "fireball":
            enemy_hp -= round(magic_damage)
            print(f"You did {magic_damage} damage!")
        elif spell == "ice blizzard":
            enemy_hp -= round(frostbite)
            print(f"You gave enemy Frostbite {frostbite} damage dealt!")

    elif action == "greed":
        damage = int(max_damage * 1.5)
        enemy_hp = enemy_hp - damage
        print(f"Greedy hit for {damage}")
        time.sleep(1)

    elif action == "dodge":
        print("You dodged!")
        dodged = True
        time.sleep(1)

    elif action == "heal":
        enemy_hit = 0.2
        print("HP BEFORE", base_hp)
        base_hp = (base_hp + 50)
        dodged = True
        print("hp gained", base_hp)
        print("HP AFTER", base_hp)
        if random.random() < enemy_hit:
            enemy_damage = round(random.randint(80, 100)*enemy_diff)
            print(f"Enemy hits you for {enemy_damage} while healing!")
            base_hp -= enemy_damage
        time.sleep(1)

    print(f"Enemy HP now: {enemy_hp}")

    # enemy turn
    if dodged:
        enemy_damage = 0
        print("Enemy attack missed!")

    else:
        enemy_damage = round(random.randint(80, 100)*enemy_diff)
    time.sleep(1)

    base_hp -= enemy_damage
    print(f"Enemy hits you for {enemy_damage}")
    time.sleep(1.2)
    print(f"Your HP: {base_hp}")

    if action == "greed" and random.random() < death_chance:
        print("greedy bitch")
        print("You died")
        print("Get good")

    elif base_hp <= 0 or enemy_hp <= 0:
        print("Game over")

        break
