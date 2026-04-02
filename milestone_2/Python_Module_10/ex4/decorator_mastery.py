import time
from functools import wraps


def spell_timer(func: callable) -> callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")

        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        duration = end_time - start_time
        print(f"Spell completed in {duration:.3f} seconds")

        return result

    return wrapper


def power_validator(min_power: int) -> callable:
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not args:
                return "No power value provided"
            power = args[2]
            if power >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"

        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> callable:
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            f"Spell failed, retrying... (attempt {attempt}"
                            f"/{max_attempts})"
                        )
                    else:
                        return (
                            "Spell casting failed "
                            f"after {max_attempts} attempts"
                        )
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        return True

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with power {power}"


if __name__ == '__main__':
    mage_names = ['jo', 'Alex']

    @spell_timer
    def spell():
        return "Fireball cast!"

    print("\nTesting spell timer...")
    res = spell()
    print(f"Result: {res}")

    print("\nTesting MageGuild...")
    mages = []
    for name in mage_names:
        print(MageGuild.validate_mage_name(name))
        if MageGuild.validate_mage_name(name):
            mages.append(MageGuild())
    print(mages[0].cast_spell("Lightning", 15))
    print(mages[0].cast_spell("fire", 5))
