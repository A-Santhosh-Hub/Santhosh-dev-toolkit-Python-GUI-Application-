# TextTools Desktop App
### Convert your web project → native `.exe` in 3 steps

---

## 📁 Project Structure

```
TextTools/
├── src/
│   └── app.py              ← Python entry point (PyWebView)
├── assets/
│   └── index.html          ← Your full app (HTML + CSS + JS)
├── requirements.txt        ← Python dependencies
├── BUILD_WINDOWS.bat       ← One-click Windows build script
├── BUILD_MAC_LINUX.sh      ← One-click Mac/Linux build script
└── README.md               ← This file
```

---

## 🚀 How to Build TextTools.exe (Windows)

### Prerequisites
- **Python 3.9+** — Download from https://python.org  
  ✅ Check "Add Python to PATH" during install!

### Steps

1. **Open** the `TextTools` folder
2. **Double-click** `BUILD_WINDOWS.bat`
3. Wait ~2 minutes for the build to complete
4. Your `.exe` appears in the `dist/` folder!

```
dist/
└── TextTools.exe   ← Your desktop app!
```

---

## 🍎 How to Build on Mac / Linux

```bash
cd TextTools
chmod +x BUILD_MAC_LINUX.sh
./BUILD_MAC_LINUX.sh
```

---

## 🔧 Manual Build (Advanced)

If you prefer to run commands manually:

```bash
# Install dependencies
pip install pywebview pyinstaller

# Build (Windows)
pyinstaller --noconfirm --onefile --windowed --name "TextTools" --add-data "assets;assets" src/app.py

# Build (Mac/Linux)  
pyinstaller --noconfirm --onefile --windowed --name "TextTools" --add-data "assets:assets" src/app.py
```

---

## ✨ Features

| Feature | Status |
|---|---|
| Code Formatter (JSON, HTML, CSS, JS, C, Java, Python) | ✅ |
| Text Cleaning (Trim, Remove Spaces, Remove Empty Lines) | ✅ |
| Case Converter (UPPER, lower, Title, Sentence) | ✅ |
| YouTube Title Length Checker | ✅ |
| Hashtag Maker | ✅ |
| HTML Viewer (native window preview) | ✅ |
| Native File Open Dialog | ✅ |
| Native File Save Dialog | ✅ |
| Drag & Drop files | ✅ |
| History (auto-save last 10 actions) | ✅ |
| Dark / Light Mode | ✅ |
| Keyboard Shortcuts (Ctrl+Enter, Ctrl+S) | ✅ |

---

## ⌨️ Keyboard Shortcuts

| Shortcut | Action |
|---|---|
| `Ctrl + Enter` | Format & Clean |
| `Ctrl + S` | Save File (native dialog) |
| `Tab` | Insert indent in editor |

---

## 🛠️ How It Works

```
Your HTML/CSS/JS  →  PyWebView Window  →  Python API Bridge
      ↓                    ↓                     ↓
   Renders natively   No browser needed    Native OS dialogs
   (like Electron)    (no Chrome install)  (Open/Save files)
```

PyWebView embeds a native OS web renderer:
- **Windows** → WebView2 (Edge/Chromium)
- **Mac** → WKWebView (Safari engine)  
- **Linux** → GTK WebKit

All your HTML/CSS/JS runs exactly as in a browser — but inside a real desktop window.

---

## ❓ Troubleshooting

**`WebView2 not found` on Windows?**
→ Install Microsoft Edge WebView2 Runtime:  
https://developer.microsoft.com/en-us/microsoft-edge/webview2/

**Antivirus blocks the .exe?**  
→ This is a false positive common with PyInstaller. Add an exception or use `--onedir` instead of `--onefile` in the build script.

**Fonts/Icons not loading?**  
→ Requires internet on first launch (Google Fonts + FontAwesome CDN). To make fully offline, embed fonts locally in `index.html`.

---

## 📄 License
© 2025 SanStudio. All rights reserved.
