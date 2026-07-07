@echo off
echo ========================================
echo Claude Code API Switcher - Builder
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH
    echo Please install Python from https://python.org
    echo.
    pause
    exit /b 1
)

echo [1/3] Installing requirements...
pip install customtkinter pyinstaller -q
if errorlevel 1 (
    echo [ERROR] Failed to install requirements
    pause
    exit /b 1
)

echo [2/3] Building executable...
pyinstaller --onefile --windowed --icon "CLogo.ico" --name "Claude-API-Switcher" app.py

if errorlevel 1 (
    echo.
    echo [WARNING] Build completed with warnings
) else (
    echo [3/3] Build successful!
)

echo.
echo ========================================
echo Output: dist\Claude-API-Switcher.exe
echo ========================================
echo.
echo You can now run the .exe file directly!
echo.
pause
