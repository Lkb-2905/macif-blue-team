import argparse
import csv
import random
import string


def fake_name() -> str:
    return "User" + "".join(random.choice(string.ascii_uppercase) for _ in range(4))


def fake_email() -> str:
    return "user" + "".join(random.choice(string.digits) for _ in range(4)) + "@example.com"


def main() -> None:
    parser = argparse.ArgumentParser(description="Anonymisation CSV (GDPR)")
    parser.add_argument("--input", default="clients.sample.csv")
    parser.add_argument("--output", default="clients.anonymized.csv")
    args = parser.parse_args()

    with open(args.input, "r", encoding="utf-8", newline="") as src:
        reader = csv.DictReader(src)
        rows = []
        for row in reader:
            row["Nom"] = fake_name()
            row["Email"] = fake_email()
            rows.append(row)

    with open(args.output, "w", encoding="utf-8", newline="") as dst:
        writer = csv.DictWriter(dst, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(f"Fichier anonymise: {args.output}")


if __name__ == "__main__":
    main()
