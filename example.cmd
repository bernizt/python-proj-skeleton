@echo off
IF NOT EXIST %~dp0.venv (
    echo.
    echo Preparing Python virtual environment [first run]
    echo.
    python -m venv %~dp0.venv
    %~dp0.venv\Scripts\pip.exe install -r %~dp0requirements.txt
)
%~dp0.venv\Scripts\python.exe %~dp0\src\example.py %*