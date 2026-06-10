#!/usr/bin/env bash
# watchdog.sh — verifica que el pipeline de aprendizaje sigue VIVO.
# La causa raíz del incidente de mayo-junio 2026: el sistema murió en
# silencio 10 días. Esto detecta congelamientos en <24h.
# Salida: líneas "OK ..." o "⚠️ ..." — pensado para el scheduled task diario.

REPO="/Users/anasahmadouch/Desktop/PrimeBot/knowledge-agents"
PROBLEMS=0

# 1. ¿El grafo está fresco? (el sync horario hace pull; >26h = congelado)
GRAPH="$REPO/graphify-out/graph.json"
if [ -f "$GRAPH" ]; then
  AGE_H=$(( ( $(date +%s) - $(stat -f %m "$GRAPH") ) / 3600 ))
  if [ "$AGE_H" -gt 26 ]; then
    echo "⚠️ graph.json tiene ${AGE_H}h — el sync horario no está haciendo pull. Revisar scheduled task sync-knowledge-vectors."
    PROBLEMS=1
  else
    echo "OK grafo fresco (${AGE_H}h)"
  fi
else
  echo "⚠️ no existe graph.json — ejecutar: cd $REPO && python3 query.py --pull"
  PROBLEMS=1
fi

# 2. ¿Los aprendizajes fluyen? (si se acumulan, el sync no los está pusheando)
PENDING=$(ls "$REPO/corpus/learn/"*.md 2>/dev/null | wc -l | tr -d ' ')
if [ "$PENDING" -gt 10 ]; then
  echo "⚠️ $PENDING aprendizajes acumulados en corpus/learn/ sin subir — el paso de commit+push del sync está fallando."
  PROBLEMS=1
else
  echo "OK aprendizajes fluyendo ($PENDING pendientes)"
fi

# 3. ¿El CI sigue recolectando? (último run del pipeline en GitHub)
CI=$(gh run list --repo anas12bs-arch/knowledge-agents --limit 1 \
     --json conclusion,updatedAt --jq '.[0] | "\(.conclusion) \(.updatedAt)"' 2>/dev/null)
case "$CI" in
  success*) echo "OK CI verde (último run: ${CI#success })" ;;
  "")       echo "⚠️ no se pudo consultar el CI (gh no autenticado o sin red)"; PROBLEMS=1 ;;
  *)        echo "⚠️ último run del CI: $CI — revisar https://github.com/anas12bs-arch/knowledge-agents/actions"; PROBLEMS=1 ;;
esac

# 4. ¿Repo local sincronizado? (>50 commits detrás = pull roto hace días)
git -C "$REPO" fetch -q origin 2>/dev/null
BEHIND=$(git -C "$REPO" rev-list --count HEAD..origin/main 2>/dev/null || echo 0)
if [ "${BEHIND:-0}" -gt 50 ]; then
  echo "⚠️ repo local $BEHIND commits detrás de origin — el pull del sync está roto."
  PROBLEMS=1
else
  echo "OK repo local sincronizado ($BEHIND commits detrás)"
fi

[ "$PROBLEMS" -eq 0 ] && echo "RESULTADO: TODO VIVO ✅" || echo "RESULTADO: PIPELINE CON PROBLEMAS ⚠️"
