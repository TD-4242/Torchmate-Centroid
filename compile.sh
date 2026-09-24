#!/usr/bin/env bash
#
# compile.sh — compile-check acorn_router_plc.src with Centroid's mpucomp.exe.
#   ./compile.sh            # compile; report errors and a warning count
#   ./compile.sh -v         # also print every compiler warning
#   ./compile.sh -o out.plc # keep the compiled program at out.plc
# Runs mpucomp.exe natively on Windows, or through Wine on Linux/macOS. It checks
# that the source compiles; it does not load anything onto the machine.
#
set -euo pipefail
cd "$(dirname "$0")"

SRC="acorn_router_plc.src"
COMPILER="mpucomp.exe"

OUT=""
VERBOSE=0
while getopts ":o:vh" opt; do
  case "$opt" in
    o) OUT="$OPTARG" ;;
    v) VERBOSE=1 ;;
    h) sed -n '2,8p' "$0"; exit 0 ;;
    *) echo "usage: $0 [-v] [-o output.plc]" >&2; exit 2 ;;
  esac
done

fail() { echo "ERROR: $*" >&2; exit 1; }

[[ -f "$SRC" ]]      || fail "source '$SRC' not found"
[[ -f "$COMPILER" ]] || fail "compiler '$COMPILER' not found in repo root"

# Git Bash does not search the current directory for binaries, hence ./
if [[ "${OS:-}" == "Windows_NT" ]]; then
  RUN=("./$COMPILER")
else
  command -v wine >/dev/null 2>&1 \
    || fail "wine not found; it is needed to run $COMPILER on this OS (e.g. 'sudo apt install wine')"
  RUN=(env WINEDEBUG=-all wine "./$COMPILER")
fi

# BSD/macOS mktemp needs -t; GNU mktemp does not.
PLC_OUT="$(mktemp 2>/dev/null || mktemp -t plc)"
LOG="$(mktemp 2>/dev/null || mktemp -t plclog)"
trap 'rm -f "$PLC_OUT" "$LOG"' EXIT

echo "Compiling $SRC ..."
set +e
"${RUN[@]}" -w "$SRC" "$PLC_OUT" > "$LOG" 2>&1
rc=$?
set -e

if grep -qiE "Compilation failed|^Error|Error Line" "$LOG" || [[ $rc -ne 0 ]]; then
  echo
  grep -iE "Error|Compilation failed" "$LOG" || cat "$LOG"
  fail "compilation failed"
fi

warn_count=$(grep -ciE "^Warning:" "$LOG" || true)
grep -iE "Compilation successful|Program size" "$LOG" || true
echo "Warnings: ${warn_count}"
if [[ "$VERBOSE" -eq 1 && "$warn_count" -gt 0 ]]; then
  echo "----"
  grep -iE "^Warning:" "$LOG"
  echo "----"
fi

if [[ -n "$OUT" ]]; then
  cp "$PLC_OUT" "$OUT"
  echo "Wrote compiled program to $OUT"
fi
