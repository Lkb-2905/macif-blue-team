import argparse
import hashlib
import json
import os


def file_hash(path: str) -> str:
    sha = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(8192), b""):
            sha.update(chunk)
    return sha.hexdigest()


def scan_folder(folder: str, exclude: set[str]) -> dict:
    hashes = {}
    for root, _, files in os.walk(folder):
        for name in files:
            path = os.path.abspath(os.path.join(root, name))
            if path in exclude:
                continue
            hashes[path] = file_hash(path)
    return hashes


def main() -> None:
    parser = argparse.ArgumentParser(description="FIM basique")
    parser.add_argument("--folder", default=".")
    parser.add_argument("--baseline", default="baseline.json")
    args = parser.parse_args()

    exclude = {os.path.abspath(args.baseline)}
    current = scan_folder(args.folder, exclude)
    if not os.path.exists(args.baseline):
        with open(args.baseline, "w", encoding="utf-8") as handle:
            handle.write(json.dumps(current, ensure_ascii=True, indent=2))
        print("Baseline creee.")
        return

    with open(args.baseline, "r", encoding="utf-8") as handle:
        baseline = json.load(handle)

    changed = [path for path, h in current.items() if baseline.get(path) != h]
    removed = [path for path in baseline.keys() if path not in current]

    if not changed and not removed:
        print("Aucun changement detecte.")
        return
    print("Changements detectes:")
    for path in changed:
        print(f" - Modifie: {path}")
    for path in removed:
        print(f" - Supprime: {path}")


if __name__ == "__main__":
    main()
