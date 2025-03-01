# Activate the virtual environment (PowerShell command)
.\venv\Scripts\Activate.ps1

# Opt out of telemetry tracking.
$env:DO_NOT_TRACK = "true"

# Run Langflow (using uvicorn, as specified)
uv run langflow run