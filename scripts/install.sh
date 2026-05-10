#!/usr/bin/env bash
# install.sh — install gb-qutebrowser config to ~/.config/config.py
# Creates a timestamped backup of any existing config before installing.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"
SOURCE_CONFIG="$REPO_ROOT/config.py"
TARGET_DIR="$HOME/.config"
TARGET_CONFIG="$TARGET_DIR/config.py"

# Ensure source config exists
if [[ ! -f "$SOURCE_CONFIG" ]]; then
    echo "ERROR: source config not found at $SOURCE_CONFIG"
    exit 1
fi

# Ensure target directory exists
mkdir -p "$TARGET_DIR"

# Backup existing config if present
if [[ -f "$TARGET_CONFIG" ]]; then
    BACKUP_TIMESTAMP="$(date +%Y%m%d%H%M%S)"
    BACKUP_PATH="${TARGET_CONFIG}.bak.${BACKUP_TIMESTAMP}"
    cp "$TARGET_CONFIG" "$BACKUP_PATH"
    echo "Backed up existing config to: $BACKUP_PATH"
fi

# Install the config
cp "$SOURCE_CONFIG" "$TARGET_CONFIG"
echo "Installed config to: $TARGET_CONFIG"
