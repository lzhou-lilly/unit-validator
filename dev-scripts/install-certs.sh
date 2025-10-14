#!/usr/bin/env bash
if [ "$EUID" -ne 0 ]; then
    echo "This script must be run as root. Please run with sudo or as root user."
    exit 1
fi
set -euo pipefail

CERTS_DIR="$(dirname "$0")/../.certs"

if [ ! -d "$CERTS_DIR" ]; then
    echo "No .certs directory found at $CERTS_DIR. Exiting."
    exit 1
fi

echo "Installing all certificates from $CERTS_DIR..."


# Handle spaces in filenames using find and while-read loop
find "$CERTS_DIR" -type f \( -name '*.crt' -o -name '*.pem' \) -print0 |
while IFS= read -r -d '' cert; do
    echo "Installing $cert..."
    cp "$cert" /usr/local/share/ca-certificates/
done

echo "Updating CA certificates..."
sudo update-ca-certificates

echo "All certificates installed."
