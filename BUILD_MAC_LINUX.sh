#!/bin/bash
set -e

echo "============================================================"
echo "  TextTools Desktop App — Build Script (Mac/Linux)"
echo "  Powered by PyWebView + PyInstaller"
echo "============================================================"
echo ""

# ── 1. Check Python ──────────────────────────────────────────
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] Python 3 not found! Install from python.org"
    exit 1
fi
echo "[OK] $(python3 --version) found."

# ── 2. Install dependencies ───────────────────────────────────
echo ""
echo "[STEP 1/3] Installing dependencies..."
pip3 install -r requirements.txt --quiet
echo "[OK] Dependencies installed."

# ── 3. Build ──────────────────────────────────────────────────
echo ""
echo "[STEP 2/3] Building TextTools binary..."
echo "(This may take 1-3 minutes)"

pyinstaller \
    --noconfirm \
    --onefile \
    --windowed \
    --name "TextTools" \
    --add-data "assets:assets" \
    src/app.py

# ── 4. Done ───────────────────────────────────────────────────
echo ""
echo "[STEP 3/3] Checking output..."
if [ -f "dist/TextTools" ] || [ -d "dist/TextTools.app" ]; then
    echo ""
    echo "============================================================"
    echo "  SUCCESS!"
    echo "  Your binary is in the dist/ folder."
    echo "  Run it with:  ./dist/TextTools"
    echo "============================================================"
else
    echo "[ERROR] Build failed. Check output above."
    exit 1
fi
