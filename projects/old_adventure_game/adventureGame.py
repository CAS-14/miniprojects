# NEW ADVENTURE GAME
# id adventureGame

from time import sleep
import datetime
import random as r
import sys
import math as m

verbose_load = True

def find_weekday():
    weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday",
                "Sunday"]
    return weekdays[datetime.date(datetime.date.today().year,
                                  datetime.date.today().month,
                                  datetime.date.today().day).weekday()]

item_index = {
    0 : {
        'name' : "Fist",
        'damage' : 5,
        'value' : 0,
        'durability' : -1,
        'attributes' : ['weapon', 'built_in']
    },
    1 : {
        'name' : "Flashlight",
        'damage' : 5,
        'value' : 10,
        'durability' : -1,
        'attributes' : ['tool']
    },
    10 : {
        'name' : "Iron Sword",
        'damage' : 20,
        'value' : 75,
        'durability' : 50,
        'attributes' : ['weapon']
    },
    1000 : {
        'name' : "Excalibur",
        'damage' : 1000000000,
        'value' : 1000000000000,
        'durability' : -1,
        'attributes' : ['weapon', 'mythic']
    }
}

mob_index = {
    1 : {
        'name' : "Wild Boar",
        'health' : 100,
        'damage' : 10,
        'type' : 'hostile' # hostile, passive, neutral
    }
}

def continue_check():
    None
def update_save():
    None

game_saved = False

def parse_file(file_path):
    global code_version, game_data, with_errors, verbose_load
    with_errors = False

    try:
        with open(file_path, "r") as f:
            game_raw_data = f.read().splitlines()
    except:
        print("ERROR 204: File Read Error")
        return 204

    else:
        print("RAW DATA: "+str(game_raw_data)) if verbose_load else None
        if game_raw_data[0] == "!!CASGAMEFORMAT":
            # LOADS VIA EXACT LINE LOCATIONS
            print("CAS Game Format detected. Continuing...")
            game_raw_data.remove("!!CASGAMEFORMAT")
            game_data = {}

            for item in game_raw_data:
                split_item = item.split('=')
                first_half = split_item[0]
                second_half = split_item[1]
                game_data[first_half] = second_half

            if 'game' in game_data:
                if game_data["game"] == "adventureGame":
                    print("Game detected: adventureGame. Checking save data...")
                    return continue_check()

                else:
                    print("ERROR 202: Incorrect Game")
                    continue_broken = input("Continue anyway? (y/n): ").lower()
                    if continue_broken in ['yes','y']:
                        with_errors = True
                        return 10
                        print("Checking save data...")
                        return continue_check()

                    else:
                        return 206

            else:
                print("ERROR 206: Game Not Specified")
                continue_broken = input("Continue anyway? (y/n): ").lower()
                if continue_broken in ['yes','y']:
                    with_errors = True
                    return 10
                    print("Checking save data...")
                    return continue_check()

                else:
                    return 206

            print("Game data loaded. Data: ")
            print(game_data)

        else:
            print("ERROR 201 (FATAL): Invalid Save Format")
            return 201

def continue_check():
    global game_data, verbose_load, game_version, game_display_name, scene, game_used_dev_mode, char_name, inventory, game_save_format, with_errors

    incomplete_keys = False
    check_keys = ['game', 'version', 'displayName', 'scene', 'dev', 'characterName', 'inventory', 'saveFormat']
    for key in check_keys:
        if key not in game_data:
            print(f'Missing Data "{key}"')
            incomplete_keys = True

    if incomplete_keys:
        print("ERROR 203 (FATAL): Missing Data")
        return 203

    else:
        try:
            game_version = str(game_data['version'])
            game_display_name = str(game_data['displayName'])
            scene = int(game_data['scene'])
            game_used_dev_mode = bool(game_data['dev'])
            char_name = str(game_data['characterName'])
            inventory = eval(game_data['inventory'])
            game_save_format = int(game_data['saveFormat'])

        except:
            print("ERROR 209 (FATAL): Wrong Data Types")
            return 209

        else:
            if game_save_format < save_format:
                print(f"This save is version {game_save_format}, but the latest version is {save_format}. Game could be glitchy!")
                with_errors = True
                print("Save is ready.")
                return 10
            elif game_save_format > save_format:
                print(f"This save is version {game_save_format}, but the game version is only {save_format}. Game could be glitchy!")
                with_errors = True
                print("Save is ready.")
                return 10
            else:
                print("Save is ready.")
                return 10

#def update_save(file_path):
#    # update save
#    None

def save_game():
    global saved, file_path

    print(f'\nSave Game "{game_display_name} ({file_path})"\nInput file path or leave blank to overwrite current file')
    new_name = input("> ")
    file_path = new_name if new_name else None

    print(f"Saving game to {file_path}...")

    file_path_split = file_path.split('/')
    file_name = file_path_split[len(file_path_split) - 1]
    file_name_split = file_name.split('.')
    try:
        file_name_split[1] = "casgame"
    except:
        file_name_split.append("casgame")
    file_name = '.'.join(file_name_split)
    file_path_split[len(file_path_split) - 1] = file_name
    file_path = '/'.join(file_path_split)

    content_to_write = ['!!CASGAMEFORMAT',
                        'loadType=NORMAL',
                        'game=adventureGame',
                        'version='+game_version,
                        'displayName='+game_display_name,
                        'scene='+scene,
                        'dev='+game_used_dev_mode,
                        'characterName='+char_name,
                        'inventory='+inventory,
                        'saveFormat='+game_save_format]

    with open(file_path, 'w') as f:
        f.writelines(content_to_write)

    print(f"Game saved to {file_path} as {game_display_name}.\n")

def open_menu():
    print("""


    ==== GAME MENU ====

    [1] Return to game
    [2] Save game
    [3] Main menu
    [4] Quit
    """)
    prompt([1,2,3,4])
    if choice == 1:
        begin_scene(scene)
    elif choice == 2:
        save_game()
        open_menu()
    elif choice in [3,4]:
        if game_saved:
            if choice == 3:
                welcome()
            elif choice == 4:
                None
        else:
            choice2 = choice
            print("""
            Game is not saved. Are you sure you want to quit?

            [1] Quit anyway
            [2] Save and quit
            [3] Cancel
            """)
            prompt([1,2,3])
            if choice == 1:
                if choice2 == 3:
                    welcome()
                elif choice2 == 4:
                    None

            elif choice == 2:
                save_game()

            elif choice == 3:
                open_menu()

def dev_console():
    print("woo! dev console!")
    while True:
        cmd_full = input("> ")
        cmd = cmd_full.split(' ')

        if cmd[0] in ['inventory', 'inv']:
            if 1 < len(cmd) < 5:
                if cmd[1] == 'set':
                    try:
                        cmd[2] = int(cmd[2])
                    except:
                        print("ERROR 302: Invalid Arguments")
                    else:
                        if cmd[2] in item_index:
                            try: 
                                cmd[3] = int(cmd[3])
                            except IndexError:
                                inventory[cmd[2]] = 1
                                print(f"Set item ID {cmd[2]} to 1")
                            except ValueError:
                                print("ERROR 302: Invalid Arguments")
                            else:
                                inventory[cmd[2]] = cmd[3]
                                print(f"Set item ID {cmd[2]} to {cmd[3]}")
                        else:
                            print("ERROR 110: Unknown Item")
                elif cmd[1] == 'remove':
                    try:
                        cmd[2] = int(cmd[2])
                    except:
                        print("ERROR 302: Invalid Arguments")
                    else:
                        if cmd[2] in item_index:
                            try:
                                del inventory[cmd[2]]
                            except KeyError:
                                print(f"ERROR 303: Could not remove item ID {cmd[2]}, it doesn't exist in inventory")
                            else:
                                print(f"Removed item ID {cmd[2]} from inventory")
                        
                        else:
                            print("ERROR 110: Unknown Item")
                
                elif cmd[1] == 'show':
                    print("Inventory contents:")
                    print(inventory)
                
                else:
                    print("ERROR 302: Invalid Arguments")
            else:
                print("ERROR 302: Invalid Arguments")
        
        elif cmd[0] == 'fight':
            if len(cmd) == 2:
                try:
                    cmd[1] = int(cmd[1])
                except:
                    print("ERROR 302: Invalid Arguments")
                else:
                    if cmd[1] in mob_index:
                        if mob_index[cmd[1]]['type'] in ['hostile', 'neutral']:
                            fight_start(cmd[1])
                        else:
                            print(f"ERROR 303: Mob ID {cmd[1]} is not hostile!")
                    else:
                        print("ERROR 302: Invalid Arguments")
            else:
                print("ERROR 302: Invalid Arguments")
        
        else:
            print("ERROR 301: Unknown command.")

def prompt(valid_choices=None, allow_menu=True):
    global choice, dev_mode

    user_choice = input("> ")

    try:
        user_choice = int(user_choice)
    except:
        None

    if dev_mode and user_choice == 'dev':
        dev_console()

    elif user_choice in ['menu', 'm'] and allow_menu:
        open_menu()

    else:
        if valid_choices != None:
            if user_choice in valid_choices:
                choice = user_choice
                return choice

            else:
                print("Invalid choice! Please try again.")
                prompt()
        else:
            choice = user_choice
            return choice

def begin_scene(index):
    if index == 1:
        print("some wip text (sc1)")
    elif index == 2:
        print("some wip text (sc2)")
        choice = prompt()
    else:
        print("some wip text (sc_err)")

def end_game(death_index):
    if death_index == 1:
        print("some wip text")
    elif death_index == 2:
        print("some wip text")
    else:
        print("some wip text")

def new_game():
    print("NEW GAME!!")

def load_game():
    global file_path, game_version, game_display_name, scene, char_name, with_errors

    print("Please specify filepath of game.")
    file_path = input("> ")
    status_code = parse_file(file_path)

    if 199 < status_code < 300:
        print(f"ERROR {status_code}. Game cannot continue.")

    elif status_code == 10 or status_code == 11:
        print(f"Game loaded from {file_path}.")
        print(f"Game version: {game_version}")
        print(f"Game name: {game_display_name}")
        print(f"Scene #{scene}")
        print(f"Character name: {char_name}")
        if with_errors:
            print("Warning: Game is running with error(s). Play could be unstable!")

        input("Press enter to continue.")
        begin_scene(scene)

def welcome():
    print(f"""
    ADVENTURE GAME

    An experience by CAS

    Version {code_version}
    """)
    print("Developer Mode Active") if dev_mode else None
    print("""

    Choose an option
    [1] New Game
    [2] Load Game
    [3] How to Play
    (Type 1, 2, or 3 below)
    """)

    prompt([1, 2, 3])
    if choice == 1:
        print("Starting new game...")
        new_game()

    elif choice == 2:
        print("Load game:")
        load_game()

    elif choice == 3:
        # tutorial()
        print('ok')

def start():
    welcome()

def get_version_numbers(ver_string):
    split_ver = '.'.split(ver_string)

def player_attack():
    None

def enemy_attack():
    None #

def fight_start(enemy):
    print(f"\n{enemy} attacks!\nChoose your weapon.")

    available_items = [0]
    for id in inventory:
        if 'weapon' in item_index[id]['attributes']:
            available_items.append(id)

    index = 1
    for item in available_items:
        print(f"[{index}] {item_index[item]['name']} ({item_index[item]['damage']} base damage)")
        index += 1

    valid_options = []
    index2 = 1
    while index2 <= index:
        valid_options.append(index2)
        index2 += 1

    item_choice = available_items[prompt(valid_options, False) - 1]
    equipped_info = {
        'id' : item_choice,
        'name' : item_index[item_choice]['name'],
        'damage' : item_index[item_choice]['damage']
    }

    enemy_info = {
        'id' : enemy,
        'name' : mob_index[enemy]['name'],
        'damage' : mob_index[enemy]['damage'],
        'health' : mob_index[enemy]['health']
    }

    health_diff_p = m.floor(enemy_info['health'] * 0.2)
    health_diff_n = -1 * health_diff_p
    health_diff_c = r.randint(health_diff_n, health_diff_p)
    enemy_info['health'] = enemy_info['health'] + health_diff_c

    fighting = True

    while fighting:
        print(f"The {enemy_info['name']} is at {enemy_info['health']}")
        print("""

            Choose an option!
            [A] Attack
            [I] Items (UNAVAILABLE AT THIS TIME)
            [R] Run away (UNAVAILABLE AT THIS TIME)
        """)
        choice = prompt().lower()

        if choice == 'a':
            bonus_decider_g = r.randint(1, 10)
            bonus_decider_v = r.randint(1, 10) 

            damage_diff_p = m.floor(equipped_info['damage'] * 0.1)
            damage_diff_n = -1 * damage_diff_p
            damage_diff_c = r.randint(damage_diff_n, damage_diff_p)
            damage_now = equipped_info['damage'] + damage_diff_c
            
            if bonus_decider_v == bonus_decider_g:
                damage_now += damage_diff_p
                print(f"Bonus damage + {damage_diff_p}!")

            enemy_info['health'] -= damage_now
            print(f"You attack the {enemy_info['name']} with your {equipped_info['name']}! Caused {damage_now} damage.")

            if enemy_info['health'] <= 0:
                won_fight = True
            else:
                won_fight = False

            if won_fight:
                print("The enemy is at 0 health. You win!")
                break
            
            else:
                print(f"Enemy's health: {enemy_info['health']}")
            print(f"Your health: {enemy_info['health']}")

            if won_fight:
                health = 100 # HEALTH RESET (add max_health later)
        
        else:
            print("Invalid option! Try again.")

        print(f"The {enemy_info['name']} attacks!")
        enemy_damage_diff_p = m.floor(mob_index[enemy]['damage'] * 0.1)
        enemy_damage_diff_n = -1 * enemy_damage_diff_p
        enemy_damage_diff_c = r.randint(damage_diff_n, damage_diff_p)
        damage_now = mob_index[enemy]['damage'] + damage_diff_c

        # if enemy_info['health'] 

        print("This code doesn't exist yet!")


if __name__ == "__main__":
    dev_mode = False

    if '--dev' in sys.argv:
        dev_mode = True

    code_version = "0.1.0"
    save_format = 2

    choice = 0

    start()
