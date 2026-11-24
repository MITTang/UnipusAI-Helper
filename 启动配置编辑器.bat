@echo off
cd /d "%~dp0"
title UnipusAI-Helper Config Editor
if not exist ".venv\Scripts\python.exe" (
    echo [ERROR] .venv not found. Please deploy first, see 部署说明.txt
    echo.
    pause
    exit /b 1
)
echo Starting config editor...
".venv\Scripts\python.exe" config_editor.py %*
if errorlevel 1 (
    echo.
    echo [WARN] Program exited abnormally. See messages above.
    pause
)
