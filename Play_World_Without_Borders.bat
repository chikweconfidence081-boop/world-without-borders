@echo off
REM Play right now without building anything (needs Python installed).
cd /d "%~dp0"
where py >nul 2>nul && (start "" pyw WorldWithoutBorders3D.py & exit /b)
where pythonw >nul 2>nul && (start "" pythonw WorldWithoutBorders3D.py & exit /b)
echo Python not found - opening the game directly in your browser instead.
start "" "game\index.html"
