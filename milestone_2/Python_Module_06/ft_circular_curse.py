from alchemy.grimoire import validate_ingredients, record_spell
import alchemy.grimoire as grimoire

if __name__ == "__main__":
    print('\n=== Circular Curse Breaking ===')

    print('\nTesting ingredient validation:')
    print(f'validate_ingredients("fire air"): {validate_ingredients("fire air")}')
    print(f'validate_ingredients("dragon scales"): {validate_ingredients("dragon scales")}')

    print('\nTesting spell recording with validation:')
    print(f'record_spell("Fireball", "fire air"): {record_spell("Fireball", "fire air")}')
    print(f'record_spell("Dark Magic", "shadow"): {record_spell("Dark Magic", "shadow")}')

    print('\nTesting late import technique:')
    """ for late import we use this: {from alchemy.grimoire.spellbook import record_spell} inside of the function bloc and not on top of the file,
    however for dependency injection we make the record spell func like the following:

    def record_spell(spell_name: str, ingredients: str, func: callable) -> str:
        if (func(ingredients).endswith("VALID")):
            return f'Spell recorded: {spell_name} ({func(ingredients)})'
        else:
            return f'Spell rejected: {spell_name} ({func(ingredients)})'
    
    and use it like : print(f'record_spell("Lightning", "air"): {record_spell("Lightning", "air", validate_ingredients)}')
    """
    print(f'record_spell("Lightning", "air"): {record_spell("Lightning", "air")}')

    print('\nCircular dependency curse avoided using late imports!')
    print('All spells processed safely!')
