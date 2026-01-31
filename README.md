# MACIF - Blue Team (demo portfolio)

![Tests](https://github.com/Lkb-2905/macif-blue-team/actions/workflows/tests.yml/badge.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)

Objectif: proposer des outils Blue Team simples a demontrer.

## Contenu
- `01-anonymisation-gdpr`: anonymisation CSV.
- `02-audit-ad-powershell`: audit comptes inactifs.
- `03-detecteur-phishing`: score par mots-cles.
- `04-file-integrity-monitor`: FIM basique.
- `05-generateur-mdp-anssi`: generation mdp fort.

## Demarrage rapide (demos)
```
cd 01-anonymisation-gdpr
python anonymize.py --input clients.sample.csv --output clients.anonymized.csv

cd ../02-audit-ad-powershell
powershell -ExecutionPolicy Bypass -File audit-ad.ps1 -InputPath users.sample.json -OutputPath inactive_users.csv -Days 90

cd ../03-detecteur-phishing
python phishing_score.py --text "Urgent: verification de mot de passe avant virement"

cd ../04-file-integrity-monitor
python fim.py --folder . --baseline baseline.json
python fim.py --folder . --baseline baseline.json

cd ../05-generateur-mdp-anssi
python password_gen.py --length 16
```

## Installation rapide
```
python -m venv .venv
source .venv/bin/activate  # ou .venv\\Scripts\\activate sous Windows
pip install -r requirements.txt
```

## Captures conseillees
- `01-anonymisation-gdpr/clients.anonymized.csv`
- `02-audit-ad-powershell/inactive_users.csv`
- Terminal: phishing score + FIM + password gen.

## Dependances
Voir `requirements.txt`.

## Roadmap et suggestions
- `ROADMAP.md`
- `CODE_SUGGESTIONS.md`
