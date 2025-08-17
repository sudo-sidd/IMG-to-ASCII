@echo off
REM ASCII Shader Converter Launch Script for Windows
echo 🎨 ASCII Shader Converter
echo ==========================
echo Opening in your default browser...
echo.

REM Try to start a local server first, then open browser
where python >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    echo Starting local server on http://localhost:8000
    echo Press Ctrl+C to stop the server
    start http://localhost:8000
    python -m http.server 8000
) else (
    REM Fallback to opening file directly
    echo Opening file directly...
    start index.html
)

pause
