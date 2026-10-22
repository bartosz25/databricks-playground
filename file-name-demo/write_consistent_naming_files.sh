#!/usr/bin/env bash
set -euo pipefail

OUTPUT_DIR="$(cd "$(dirname "$0")" && pwd)/input_files"
DATE_SUFFIX="$(date +%Y%m%d)"

mkdir -p "$OUTPUT_DIR"
echo "[consistent_naming] Writing files to ${OUTPUT_DIR}"

printf 'from_currency,to_currency,rate\nUSD,EUR,0.92\n' > "${OUTPUT_DIR}/USD_EUR_${DATE_SUFFIX}.csv"
printf 'from_currency,to_currency,rate\nEUR,GBP,0.86\n' > "${OUTPUT_DIR}/EUR_GBP_${DATE_SUFFIX}.csv"

echo "[consistent_naming] Written 2 files"
