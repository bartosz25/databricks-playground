#!/usr/bin/env bash
set -euo pipefail

OUTPUT_DIR="$(cd "$(dirname "$0")" && pwd)/input_files_autoloader"

mkdir -p "$OUTPUT_DIR"
echo "[autoloader] Writing test files to ${OUTPUT_DIR}"

printf 'id,amount\n1,100\n2,200\n' > "${OUTPUT_DIR}/file_001.csv"
printf 'id,amount\n3,300\n4,400\n' > "${OUTPUT_DIR}/file_002.csv"
printf 'id,amount\n5,500\n6,600\n' > "${OUTPUT_DIR}/file_003.csv"

echo "[autoloader] Written 3 files"
