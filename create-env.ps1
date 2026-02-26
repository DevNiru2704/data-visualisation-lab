Write-Host "Creating virtual environment..."
python -m venv .venv

Write-Host "Activating virtual environment..."
. .\.venv\Scripts\Activate.ps1

Write-Host "Ensuring pip is installed..."
python -m ensurepip

Write-Host "Upgrading pip..."
python -m pip install --upgrade pip

Write-Host "Installing requirements..."
python -m pip install -r requirements.txt

Write-Host "Setup complete."