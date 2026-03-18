def validate_ingredients(ingredients: str) -> str:
    valid_elements = ["fire", "water", "earth", "air"]
    for ingredient in ingredients.split(" "):
        if ingredient not in valid_elements:
            return f"{ingredients} - INVALID"
    return f"{ingredients} - VALID"
