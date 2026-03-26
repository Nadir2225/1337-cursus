def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    artifacts.sort(key = lambda artifact : artifact['power'], reverse=True)
    return artifacts


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    filtered_mages = filter(lambda mage : mage['power'] >= min_power, mages)
    return list(filtered_mages)


def spell_transformer(spells: list[str]) -> list[str]:
    mapped_spells = map(lambda spell: f"* {spell} *", spells)
    return list(mapped_spells)


def mage_stats(mages: list[dict]) -> dict:
    powers = list(map(lambda mage: mage['power'], mages))
    return {
        'max_power': max(mages, key = lambda mage: mage['power'])['power'],
        'min_power': min(mages, key = lambda mage: mage['power'])['power'],
        'avg_power': round(sum(powers)/ len(powers))
    }


if __name__ == '__main__':
    artifacts = [{'name': 'Fire Staff', 'power': 77, 'type': 'armor'}, {'name': 'Crystal Orb', 'power': 106, 'type': 'weapon'}, {'name': 'Fire Staff', 'power': 74, 'type': 'relic'}, {'name': 'Earth Shield', 'power': 72, 'type': 'weapon'}]
    mages = [{'name': 'Sage', 'power': 76, 'element': 'water'}, {'name': 'Nova', 'power': 54, 'element': 'ice'}, {'name': 'Zara', 'power': 89, 'element': 'lightning'}, {'name': 'Nova', 'power': 57, 'element': 'wind'}, {'name': 'Storm', 'power': 68, 'element': 'wind'}]
    spells = ['tsunami', 'darkness', 'earthquake', 'lightning']
    first_artificat = artifact_sorter(artifacts)[0]
    second_artificat = artifact_sorter(artifacts)[1]
    print("\nTesting artifact sorter...")
    print(
        f"{first_artificat['name']} ({first_artificat['power']} "
        f"power) comes before {second_artificat['name']} "
        f"({second_artificat['power']} power)"
    )

    print("\nTesting spell transformer...")
    for spell in spell_transformer(spells):
        print(f"{spell} ", end = "")
