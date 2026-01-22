import argparse


KEYWORDS = {
    "urgent": 3,
    "virement": 4,
    "mot de passe": 5,
    "confidentiel": 2,
    "verification": 2,
}


def score_text(text: str) -> int:
    score = 0
    lower = text.lower()
    for word, value in KEYWORDS.items():
        if word in lower:
            score += value
    return score


def level(score: int) -> str:
    if score >= 8:
        return "fort"
    if score >= 4:
        return "moyen"
    return "faible"


def main() -> None:
    parser = argparse.ArgumentParser(description="Detecteur phishing par mots-cles")
    parser.add_argument("--text", required=True)
    args = parser.parse_args()

    s = score_text(args.text)
    print(f"Score: {s} / Niveau: {level(s)}")


if __name__ == "__main__":
    main()
