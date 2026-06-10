#!/usr/bin/env zsh
# Usa: ./learn.sh "lo que aprendiste" --type error/insight/optimization --tags "tag1,tag2"
# Como esta en local, escribe directo al corpus y al grafo local.
# El proximo push a GitHub lo sincroniza con los agentes CI.

SCRIPTPATH="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPTPATH" || exit 1

# Guarda el aprendizaje en corpus/learn/
python3 -m core.learn "$@"
python3 -m core.learn --stats 2>/dev/null || true

# NO reconstruir el grafo localmente: el rebuild local tarda ~40 min, y además
# pierde los nodos de docs ya archivados (sus .md no existen en local). El grafo
# autoritativo lo construye el CI; el sync horario lo trae con git pull.
# El aprendizaje llega al grafo así: sync horario lo commitea+push → CI lo ingiere.

echo "Listo. El sync horario lo subirá y el CI lo integrará al grafo."
