"""
SessionEnd hook — al cerrar una sesión de Claude Code, guarda un resumen
mecánico de lo que se hizo (archivos tocados, comandos fallidos) como
aprendizaje tipo `lesson`. Así el sistema también aprende de los ÉXITOS,
no solo de los errores. Stdlib puro.
"""
from __future__ import annotations
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path

KA = Path(__file__).resolve().parent.parent
MIN_FILES = 1


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except Exception:
        return
    transcript = data.get("transcript_path")
    session_id = str(data.get("session_id") or "")[:8]
    if not transcript or not Path(transcript).exists():
        return

    edited: set[str] = set()
    failed_cmds: list[str] = []
    user_msgs = 0
    for line in open(transcript, errors="ignore"):
        try:
            d = json.loads(line)
        except Exception:
            continue
        if d.get("type") == "user" and isinstance(
                d.get("message", {}).get("content"), str):
            user_msgs += 1
        msg = d.get("message") or {}
        for c in (msg.get("content") or []) if isinstance(msg.get("content"), list) else []:
            if not isinstance(c, dict) or c.get("type") != "tool_use":
                continue
            name, inp = c.get("name", ""), c.get("input") or {}
            if name in ("Write", "Edit", "NotebookEdit") and inp.get("file_path"):
                edited.add(str(inp["file_path"]))
        r = d.get("toolUseResult")
        if isinstance(r, dict) and r.get("stderr"):
            stderr = str(r["stderr"])
            if "Traceback" in stderr or "command not found" in stderr:
                failed_cmds.append(stderr[:80])

    if len(edited) < MIN_FILES:
        return

    files = sorted(edited)
    body = (
        f"Sesión {session_id} ({user_msgs} mensajes) modificó "
        f"{len(files)} archivo(s):\n"
        + "\n".join(f"- {f}" for f in files[:20])
        + (f"\n\nErrores vistos durante la sesión: {len(failed_cmds)}"
           if failed_cmds else "")
    )
    title = (f"Sesión {datetime.now():%Y-%m-%d} [{session_id}]: "
             f"{len(files)} archivos — {Path(files[0]).name}"
             + (f" +{len(files)-1}" if len(files) > 1 else ""))
    subprocess.run(
        [sys.executable, "-m", "core.learn", f"{title}\n{body}",
         "--type", "lesson", "--tags", "session,auto-capture"],
        cwd=KA, capture_output=True, timeout=15,
    )


if __name__ == "__main__":
    main()
