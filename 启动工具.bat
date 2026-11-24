@echo off
cd /d "%~dp0"
title UnipusAI-Helper Launcher
if not exist ".venv\Scripts\python.exe" (
    echo [ERROR] .venv not found. Please deploy first, see 部署说明.txt
    echo.
    pause
    exit /b 1
)
echo ============================================
echo   Starting UnipusAI-Helper...
echo   A browser window will open, login once if asked.
echo ============================================
echo.
".venv\Scripts\python.exe" UnipusAI_Helper.py %*
if errorlevel 1 (
    echo.
    echo [WARN] Program exited abnormally. See messages above.
    pause
)
