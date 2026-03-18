def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients
    if (validate_ingredients(ingredients).endswith("VALID")):
        return f'Spell recorded: {spell_name} ({validate_ingredients(ingredients)})'
    else:
        return f'Spell rejected: {spell_name} ({validate_ingredients(ingredients)})'