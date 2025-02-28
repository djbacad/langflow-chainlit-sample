# Activate the virtual environment (PowerShell command)
.\venv_langflow_local\Scripts\Activate.ps1

# Opt out of telemetry tracking.
$env:DO_NOT_TRACK = "true"

# Run Langflow (using uvicorn, as specified)
uv run langflow run