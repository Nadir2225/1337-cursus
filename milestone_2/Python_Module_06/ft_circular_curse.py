from alchemy.grimoire import validate_ingredients
import alchemy.grimoire as grimoire

if __name__ == "__main__":
    print('\n=== Circular Curse Breaking ===')

    print('\nTesting ingredient validation:')
    print(f'validate_ingredients("fire air"): {validate_ingredients("fire air")}')
    print(f'validate_ingredients("dragon scales"): {validate_ingredients("dragon scales")}')

    print('\nTesting spell recording with validation:')
    print(f'record_spell("Fireball", "fire air"): {grimoire.record_spell("Fireball", "fire air")}')
    print(f'record_spell("Dark Magic", "shadow"): {grimoire.record_spell("Dark Magic", "shadow")}')

    print('\nTesting late import technique:')
    from alchemy.grimoire.spellbook import record_spell
    print(f'record_spell("Lightning", "air"): {record_spell("Lightning", "air")}')

    print('\nCircular dependency curse avoided using late imports!')
    print('All spells processed safely!')
