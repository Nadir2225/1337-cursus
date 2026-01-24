def total_value_and_item_count(player: dict) -> tuple:
    total_value = 0
    item_count = 0
    for item in player:
        quantities = player[item]['quantities']
        value = player[item]['value']
        total_value += quantities * value
        item_count += quantities
    return (total_value, item_count)


def ft_inventory_system():
    print('=== Player Inventory System ===\n')
    players = {
        "Alice":
        {
            "sword":
            {
                "type": "weapon",
                "rarity": "rare",
                "quantities": 1,
                "value": 500
            },
            "potion":
            {
                "type": "consumable",
                "rarity": "common",
                "quantities": 5,
                "value": 50
            },
            "shield":
            {
                "type": "armor",
                "rarity": "uncommon",
                "quantities": 1,
                "value": 200
            }
        },
        "Bob":
        {
            "magic_ring":
            {
                "type": "weapon",
                "rarity": "rare",
                "quantities": 1,
                "value": 700
            }
        }
    }
    print("=== Alice's Inventory ===")
    for item in players["Alice"]:
        quantities = players['Alice'][item]['quantities']
        value = players['Alice'][item]['value']
        print(
            f"{item} ({players['Alice'][item]['type']}, "
            f"{players['Alice'][item]['rarity']}): "
            f"{players['Alice'][item]['quantities']}x @ "
            f"{players['Alice'][item]['value']} "
            f"gold each = {quantities * value} gold "
        )
    print()
    
    print(f"Inventory value: {total_value_and_item_count(players['Alice'])[0]} gold")
    print(f"Item count: {total_value_and_item_count(players['Alice'])[1]} items")
    print("Categories: ", end="")
    i = 0
    for item in players['Alice']:
        print(f' {players['Alice'][item]["type"]}({item})', end='')
        if i != len(players['Alice']) - 1:
            print(',', end='')
        i += 1
    print()
    potions_nbr = 2
    print("\n=== Transaction: Alice gives Bob {potions_nbr} potions ===")
    players['Alice']['potion']['quantities'] -= potions_nbr
    players["Bob"]['potion'] = {}
    players["Bob"]["potion"].update({
        "quantities": potions_nbr,
        "type": players['Alice']['potion']['type'],
        "rarity": players['Alice']['potion']['rarity'],
        "value": players['Alice']['potion']['value']
    })
    print("Transaction successful!")
    print()
    print("=== Updated Inventories ===")
    print(f"Alice potions: {players['Alice']['potion']['quantities']}")
    print(f"Bob potions: {players['Bob']['potion']['quantities']}")
    print()
    print('=== Inventory Analytics ===')
    mvp = ''
    mip = ''
    for player in players:
        mvp = player
        mip = player
        break
    ri = []
    for player in players:
        for item in players[player]:
            if (players[player][item]['rarity'] == 'rare'):
                ri += [item]
        if (total_value_and_item_count(players[player])[0] > total_value_and_item_count(players[mvp])[0]):
            mvp = player
        if (total_value_and_item_count(players[player])[1] > total_value_and_item_count(players[mip])[1]):
            mip = player
    print(f"Most valuable player: {mvp} ({total_value_and_item_count(players[mvp])[0]} gold)")
    print(f"Most items player: {mip} ({total_value_and_item_count(players[mip])[1]} items)")
    print(f"Rarest items: ", end='')
    i = 0
    for item in ri:
        print(f'{item}', end='')
        if (i == len(ri) - 1):
            print()
        else:
            print(', ', end='')
        i += 1


    
if __name__ == '__main__':
    ft_inventory_system()

