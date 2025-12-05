@echo off
chcp 65001 >nul
cd /d "%~dp0"

call venv\Scripts\activate.bat

echo Uninstalling CPU version of PyTorch...
pip uninstall torch torchaudio torchvision -y

echo Installing PyTorch with CUDA 12.1 support...
pip install torch --index-url https://download.pytorch.org/whl/cu121

echo.
echo Checking GPU...
python check_gpu.py

pause
