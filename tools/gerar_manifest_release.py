#!/usr/bin/env python3
"""Gera manifesto de atualizações para APK assinado publicado em uma Release pública."""
import argparse, hashlib, json, re
from pathlib import Path

REPO = "apoenalore/ApoenaBrowser-Updates"
TAG_PATTERN = r"v([0-9]+\.[0-9]+\.[0-9]+(?:-[a-z0-9.-]+)?)"

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--apk", required=True, type=Path)
    p.add_argument("--tag", required=True)
    p.add_argument("--out", default="updates/latest.json", type=Path)
    a = p.parse_args()
    match = re.fullmatch(TAG_PATTERN, a.tag)
    if not match:
        raise SystemExit("Tag invalida: ex. v0.3.1-alpha")
    if not a.apk.is_file() or not re.fullmatch(r"[a-zA-Z0-9._-]+\.apk", a.apk.name):
        raise SystemExit("Arquivo APK inexistente ou com nome invalido")
    h = hashlib.sha256()
    with a.apk.open("rb") as f:
        for block in iter(lambda: f.read(1024*1024), b""):
            h.update(block)
    release = f"https://github.com/{REPO}/releases"
    manifest = {
        "version": match.group(1),
        "notes": f"Apoena Browser {match.group(1)} — APK oficial assinado.",
        "release_url": f"{release}/tag/{a.tag}",
        "apk_url": f"{release}/download/{a.tag}/{a.apk.name}",
        "sha256": h.hexdigest(),
    }
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print("SHA-256:", manifest["sha256"])
    print("Manifesto criado:", a.out)
    print("ATENCAO: confirme que o APK foi assinado com a chave oficial antes de publicar.")
if __name__ == "__main__":
    main()
