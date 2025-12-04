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

if not exist input mkdir input
if not exist output mkdir output

set "count=0"
for %%f in (input\*.mp3) do set /a count+=1

if %count%==0 (
    echo No MP3 files found in input folder.
    pause
    exit /b
)

echo Found %count% MP3 file(s) in input folder.
echo.

for %%f in (input\*.mp3) do (
    echo Processing: %%~nxf
    whisper "%%f" --model turbo --language Russian --output_format txt --output_dir output
    echo Done: %%~nf.txt
    echo.
)

echo.
echo All files processed! Check output folder for results.
pause
