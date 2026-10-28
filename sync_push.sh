#!/bin/bash
git add -A
if ! git diff --cached --quiet; then
    git commit -m "loop-sync: $(date '+%Y-%m-%d %H:%M:%S')"
    if git remote | grep -q "^origin$"; then
        git push -u origin main || true
        echo "[+] GitHub 원격 저장소 동기화 완료!"
    fi
fi
