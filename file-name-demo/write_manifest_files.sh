#!/usr/bin/env bash
set -euo pipefail

OUTPUT_DIR="$(cd "$(dirname "$0")" && pwd)/input_files_manifest"

mkdir -p "$OUTPUT_DIR"
echo "[manifest] Writing files to ${OUTPUT_DIR}"

printf 'id,amount\n1,100\n2,200\n' > "${OUTPUT_DIR}/transactions_001.csv"
printf 'id,amount\n3,300\n4,400\n' > "${OUTPUT_DIR}/transactions_002.csv"

echo "[manifest] Written 2 files"
