@echo off
REM ==== World Without Borders 3D - build WorldWithoutBorders3D.exe ====
REM Needs Python (3.10 - 3.13 recommended). Result: dist\WorldWithoutBorders3D.exe
setlocal
cd /d "%~dp0"
set "PY="
py -3.13 -c "import sys" >nul 2>nul && set "PY=py -3.13"
if not defined PY (py -3.12 -c "import sys" >nul 2>nul && set "PY=py -3.12")
if not defined PY (py -c "import sys" >nul 2>nul && set "PY=py")
if not defined PY (python -c "import sys" >nul 2>nul && set "PY=python")
if not defined PY goto :nopy

echo [1/2] Installing PyInstaller ...
%PY% -m pip install --upgrade pyinstaller
if errorlevel 1 (
  echo pip failed - retrying with pypi.org marked as trusted - usually an SSL certificate problem on this PC
  %PY% -m pip install --upgrade pyinstaller --trusted-host pypi.org --trusted-host files.pythonhosted.org
)
if errorlevel 1 goto :fail

echo [2/2] Building WorldWithoutBorders3D.exe ...
%PY% -m PyInstaller --noconfirm --clean --onefile --windowed --name WorldWithoutBorders3D ^
  --icon game\assets\icon.ico --add-data "game;game" WorldWithoutBorders3D.py
if errorlevel 1 goto :fail
echo.
echo Done!  Your game:  %cd%\dist\WorldWithoutBorders3D.exe
pause
exit /b 0

:nopy
echo Python was not found. Install Python 3.13 from https://www.python.org/downloads/ (tick "Add python.exe to PATH").
pause
exit /b 1
:fail
echo BUILD FAILED - copy the error above and send it to Claude.
pause
exit /b 1
