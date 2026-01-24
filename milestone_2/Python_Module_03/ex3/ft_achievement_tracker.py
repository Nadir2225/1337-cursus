def ft_achievement_tracker():
    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie = {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon', 'perfectionist'}
    print('=== Achievement Tracker System ===')
    print()
    print(f'Player alice achievements: {alice}')
    print(f'Player bob achievements: {bob}')
    print(f'Player charlie achievements: {charlie}')
    print()
    unique = alice.union(bob).union(charlie)
    print('=== Achievement Analytics ===')
    print(f'All unique achievements: {unique}')
    print(f'Total unique achievements: {len(unique)}')
    print()
    common = alice.intersection(bob)
    common = common.intersection(bob.intersection(charlie))
    players_nbr = 0
    alice_unique = alice.difference(bob.union(charlie))
    bob_unique = bob.difference(alice.union(charlie))
    charlie_unique = charlie.difference(alice.union(bob))
    if (len(alice_unique)):
        players_nbr += 1
    if (len(bob_unique)):
        players_nbr += 1
    if (len(charlie_unique)):
        players_nbr += 1
    rare = alice_unique.union(bob_unique).union(charlie_unique)  
    print(f'Common to all players: {common}')
    print(f'Rare achievements (1 player): {rare}')
    # print(f'Rare achievements ({players_nbr} player): {rare}')
    print()
    print(f'Alice vs Bob common: {alice.intersection(bob)}')
    print(f'Alice unique: {alice.difference(bob)}')
    print(f'Bob unique: {bob.difference(alice)}')

if __name__ == '__main__':
    ft_achievement_tracker()