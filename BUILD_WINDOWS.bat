@echo off
title TextTools — Build Script
color 0A

echo ============================================================
echo   TextTools Desktop App — Build Script
echo   Powered by PyQt5 + PyInstaller
echo   Compatible with Python 3.9 to 3.14
echo ============================================================
echo.

:: Check Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python not found! Install Python 3.9+ from python.org
    pause & exit /b 1
)
echo [OK] Python found.

:: Install dependencies
echo.
echo [STEP 1/3] Installing PyQt5 + PyInstaller...
pip install PyQt5 PyQtWebEngine pyinstaller --quiet
if %errorlevel% neq 0 (
    echo [ERROR] Failed to install. Check your internet connection.
    pause & exit /b 1
)
echo [OK] Dependencies installed.

:: Build EXE
echo.
echo [STEP 2/3] Building TextTools.exe ...
echo (This may take 2-4 minutes — please wait)
echo.

pyinstaller ^
    --noconfirm ^
    --onefile ^
    --windowed ^
    --name "TextTools" ^
    --add-data "assets;assets" ^
    src\app.py

:: Check result
echo.
echo [STEP 3/3] Checking output...
if exist "dist\TextTools.exe" (
    echo.
    echo ============================================================
    echo   SUCCESS! TextTools.exe is ready!
    echo   Location: dist\TextTools.exe
    echo   Double-click it to launch your desktop app!
    echo ============================================================
    explorer dist
) else (
    echo [ERROR] Build failed. See output above for details.
)
echo.
pause
