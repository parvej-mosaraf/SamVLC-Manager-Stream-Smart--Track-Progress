@echo off
title SamVLC Manager

cd /d "%~dp0"

if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

call venv\Scripts\activate

pip install -r requirements.txt

start http://127.0.0.1:5000

python app.py

pause