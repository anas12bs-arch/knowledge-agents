"""
PostToolUse(Bash) hook — captura comandos fallidos como aprendizajes.

Claude Code NO expone el exit code en tool_response (campos reales:
stdout, stderr, interrupted, isImage, noOutputExpected), así que el
fallo se detecta por patrones de error en stderr. Stdlib puro.
"""
from __future__ import annotations
import json
import re
import subprocess
import sys
from pathlib import Path

KA = Path(__file__).resolve().parent.parent

ERROR_PATTERNS = re.compile(
    r"(command not found|No such file or directory|"
    r"Traceback \(most recent call last\)|fatal:|npm ERR!|"
    r"SyntaxError|ModuleNotFoundError|ImportError|TypeError|"
    r"Permission denied|ENOENT|EADDRINUSE|error TS\d|"
    r"Segmentation fault|panic:|Compilation failed|FAILED)",
    re.IGNORECASE,
)


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except Exception:
        return

    resp = data.get("tool_response") or {}
    stderr = str(resp.get("stderr") or "")
    cmd = str((data.get("tool_input") or {}).get("command") or "")

    if not stderr or not ERROR_PATTERNS.search(stderr):
        return
    if "core.learn" in cmd:  # no capturar errores del propio capturador
        return

    subprocess.run(
        [sys.executable, "-m", "core.learn",
         f"Bash error: {cmd[:100]}",
         "--type", "error",
         "--cause", cmd[:300],
         "--effect", stderr[:400],
         "--tags", "bash,auto-capture",
         "--severity", "warning"],
        cwd=KA, capture_output=True, timeout=15,
    )


if __name__ == "__main__":
    main()
