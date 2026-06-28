@echo off
title AuraRecruit - AI Candidate Ranker
color 0A

echo.
echo  ============================================================
echo    AURA RECRUIT — AI Candidate Ranker
echo    Team Antigravity ^| India Runs Data ^& AI Challenge
echo  ============================================================
echo.

:: ─── Step 1: Check Python ───────────────────────────────────────────────────
echo  [1/4] Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo.
    echo  [ERROR] Python is not installed or not in PATH!
    echo.
    echo  Please install Python 3.10+ from: https://www.python.org/downloads/
    echo  Make sure to check "Add Python to PATH" during installation.
    echo.
    pause
    exit /b 1
)
for /f "tokens=*" %%i in ('python --version 2^>^&1') do echo  [OK] Found %%i
echo.

:: ─── Step 2: Install requirements ───────────────────────────────────────────
echo  [2/4] Installing required packages...
pip install -r "%~dp0requirements.txt" --quiet
if errorlevel 1 (
    echo  [ERROR] Failed to install requirements. Check your internet connection.
    pause
    exit /b 1
)
echo  [OK] All packages installed.
echo.

:: ─── Step 3: Find candidates.jsonl ──────────────────────────────────────────
echo  [3/4] Looking for candidates.jsonl...

set CANDIDATES=

:: Check next to this script first
if exist "%~dp0candidates.jsonl" (
    set CANDIDATES=%~dp0candidates.jsonl
    echo  [OK] Found candidates.jsonl in current folder.
    goto :run
)

:: Check one level up (common when cloned from GitHub)
if exist "%~dp0..\candidates.jsonl" (
    set CANDIDATES=%~dp0..\candidates.jsonl
    echo  [OK] Found candidates.jsonl in parent folder.
    goto :run
)

:: Check inside the challenge subfolder
if exist "%~dp0..\[PUB] India_runs_data_and_ai_challenge\India_runs_data_and_ai_challenge\candidates.jsonl" (
    set CANDIDATES=%~dp0..\[PUB] India_runs_data_and_ai_challenge\India_runs_data_and_ai_challenge\candidates.jsonl
    echo  [OK] Found candidates.jsonl in challenge folder.
    goto :run
)

:: Not found — ask the user
echo  [!] candidates.jsonl not found automatically.
echo.
echo  Please enter the full path to candidates.jsonl
echo  (You can drag and drop the file onto this window)
echo.
set /p CANDIDATES="  Path: "

:: Strip surrounding quotes if drag-dropped
set CANDIDATES=%CANDIDATES:"=%

if not exist "%CANDIDATES%" (
    echo.
    echo  [ERROR] File not found at: %CANDIDATES%
    echo  Please check the path and try again.
    pause
    exit /b 1
)
echo  [OK] Using: %CANDIDATES%

:run
echo.
:: ─── Step 4: Launch the app ─────────────────────────────────────────────────
echo  [4/4] Starting AuraRecruit server...
echo.
echo  ============================================================
echo   Server will start at: http://127.0.0.1:5000
echo   Your browser will open automatically in ~5 seconds.
echo   To stop: press Ctrl+C or close this window.
echo  ============================================================
echo.

python "%~dp0app.py" --candidates "%CANDIDATES%"

echo.
echo  Server stopped.
pause
