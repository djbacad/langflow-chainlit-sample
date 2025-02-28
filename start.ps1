# Get inside venv
venv_langflow_local/Scripts/activate

# Opt out of telemetry tracking.
$env:DO_NOT_TRACK = "true"

# Run Langflow (using uvicorn, as specified)
uv run langflow run