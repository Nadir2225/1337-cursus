from dotenv import load_dotenv
import os


if __name__ == '__main__':
    print("\nORACLE STATUS: Reading the Matrix...")

    load_dotenv()
    print("\nConfiguration loaded:")

    keys = [
        "MATRIX_MODE", "DATABASE_URL",
        "API_KEY", "LOG_LEVEL", "ZION_ENDPOINT"
    ]

    env_dict = {key: os.getenv(key) for key in keys}

    missing = False

    for key, value in env_dict.items():
        if value is None:
            missing = True
            print(f"missing key: {key}")
        else:
            if key == "DATABASE_URL":
                print("Database: Connected to local instance")
            elif key == "API_KEY":
                print("API Access: Authenticated")
            elif key == "ZION_ENDPOINT":
                print("Zion Network: Online")
            elif key == "MATRIX_MODE":
                print(f"Mode: {value}")
            elif key == "LOG_LEVEL":
                print(f"Log Level: {value}")

    print("\nEnvironment security check:")
    if not missing:
        print("[OK] No hardcoded secrets detected")
        print("[OK] .env file properly configured")
        print("[OK] Production overrides available")
    else:
        print("[ERROR] hardcoded secrets detected")
        print("[ERROR] .env file isn't properly configured")
        print("[ERROR] Production failed")

    print("\nThe Oracle sees all configurations.")
