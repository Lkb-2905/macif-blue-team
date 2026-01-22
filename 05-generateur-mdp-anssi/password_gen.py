import argparse
import random
import string


def generate(length: int) -> str:
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + "!@#$%^&*"
    while True:
        pwd = "".join(random.choice(chars) for _ in range(length))
        if validate(pwd):
            return pwd


def validate(password: str) -> bool:
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*" for c in password)
    return has_lower and has_upper and has_digit and has_special and len(password) >= 12


def main() -> None:
    parser = argparse.ArgumentParser(description="Generateur de mots de passe")
    parser.add_argument("--length", type=int, default=16)
    args = parser.parse_args()

    pwd = generate(args.length)
    print(pwd)


if __name__ == "__main__":
    main()
