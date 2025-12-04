@echo off
chcp 65001 >nul
cd /d "%~dp0"

if not exist venv\Scripts\activate.bat (
    echo Creating virtual environment with Python 3.12...
    py -3.12 -m venv venv
    call venv\Scripts\activate.bat
    echo Installing PyTorch with CUDA support...
    pip install torch --index-url https://download.pytorch.org/whl/cu121
    echo Installing openai-whisper...
    pip install -U openai-whisper
) else (
    call venv\Scripts\activate.bat
)

echo.
echo Transcribing videoplayback.mp3 with turbo model...
echo.

whisper videoplayback.mp3 --model turbo --language Russian --output_format txt

echo.
echo Done! Check videoplayback.txt for results.
pause
