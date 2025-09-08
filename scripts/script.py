def draw1(character_X, character_Y, enemies_coords):
    if character_X > map_width or character_X <= 0:
        print('Указана неверная координата X у героя')
        return
    if character_Y > map_height or character_Y <= 0:
        print('Указана неверная координата Y у героя')
        return

    for enemy in enemies_coords:
        ex, ey = enemy
        if ex > map_width or ex <= 0 or ey > map_height or ey <= 0:
            print('Неверные координаты врага')
            return

    for i in range(1, map_height + 1):
        row = ''
        for j in range(1, map_width + 1):
            cell = map_symbol
            if j == character_X and i == character_Y:
                cell = 'C'
            else:
                for ex, ey in enemies_coords:
                    if j == ex and i == ey:
                        cell = 'e'
                        break
            row += cell
        print(row)

def calculate_damage(attack, target_defence):
    damage = attack * (1 - target_defence / 100)
    return max(1, int(damage))  # минимум 1 урон

calculate_damage(10, 10)

def fight(character_hp, character_atk, character_def, enemy_hp, enemy_atk, enemy_def, verbose=True):
    if verbose:
        print('Бой начался!')

    while True:
        # Игрок атакует врага
        damage_c_e = calculate_damage(character_atk, enemy_def)
        enemy_hp -= damage_c_e
        if verbose:
            print(f'Персонаж бьёт с атакой {character_atk} против защиты {enemy_def}, наносит {damage_c_e} урона')
            if enemy_hp > 0:
                print(f'У противника осталось {enemy_hp} хп')
            else:
                print('Вы победили!')

        if enemy_hp <= 0:
            return character_hp  # Возвращаем оставшееся здоровье

        # Враг атакует игрока
        damage_e_c = calculate_damage(enemy_atk, character_def)
        character_hp -= damage_e_c
        if verbose:
            print(f'Противник бьёт с атакой {enemy_atk} против защиты {character_def}, наносит {damage_e_c} урона')
            if character_hp > 0:
                print(f'У персонажа осталось {character_hp} хп')
            else:
                print('Вы проиграли!')

        if character_hp <= 0:
            return 0  # Игрок погиб