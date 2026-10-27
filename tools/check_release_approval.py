#!/usr/bin/env python3
"""Controla se a publicação de uma nova versão foi explicitamente autorizada."""
import argparse, json, re, sys
from pathlib import Path
parser=argparse.ArgumentParser()
parser.add_argument("--tag", required=True)
args=parser.parse_args()
approval=json.loads(Path("updates/release_approval.json").read_text(encoding="utf-8"))
tag=args.tag
if not re.fullmatch(r"v\d+\.\d+\.\d+(?:-[a-z0-9.-]+)?",tag):
    raise SystemExit("Tag inválida")
if approval.get("approved") is not True or approval.get("tag")!=tag:
    raise SystemExit("RELEASE BLOQUEADA: versão não autorizada pelo proprietário.")
if int(approval.get("required_checks",0)) < 26 or not str(approval.get("evidence_reference","")).strip():
    raise SystemExit("RELEASE BLOQUEADA: auditoria/evidências incompletas.")
print("Autorização de publicação encontrada para",tag)
