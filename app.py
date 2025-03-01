import chainlit as cl
import sqlite3
import bcrypt
import requests
import json
import os
from dotenv import load_dotenv 
# Load environment variables from .env file
load_dotenv()

# Langflow API details
BASE_API_URL = "http://127.0.0.1:7860"
FLOW_ID = os.getenv("FLOW_ID")

def run_flow(message: str, endpoint: str = FLOW_ID, tweaks: dict = None, api_key: str = None) -> dict:
    """
    Call the Langflow API to run the flow with the provided query/prompt.
    """
    api_url = f"{BASE_API_URL}/api/v1/run/{endpoint}"
    payload = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat",
    }
    if tweaks:
        payload["tweaks"] = tweaks
    headers = {"x-api-key": api_key} if api_key else None
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()

def authenticate_user(username: str, password: str):
    """
    Verify user credentials from the SQLite database.
    """
    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    c.execute("SELECT password_hash, role FROM users WHERE username = ?", (username,))
    user = c.fetchone()
    conn.close()

    if user:
        stored_password_hash, role = user
        if bcrypt.checkpw(password.encode("utf-8"), stored_password_hash):
            return cl.User(identifier=username, metadata={"role": role, "provider": "credentials"})

    return None

@cl.password_auth_callback
def auth_callback(username: str, password: str):
    """
    Chainlit authentication callback.
    """
    return authenticate_user(username, password)

@cl.on_message
async def main(user_message):
    """
    Chainlit message handler.
    Sends the user's message (as text) to Langflow and then sends back the response.
    """
    if hasattr(user_message, "content"):
        text_input = user_message.content
    else:
        text_input = str(user_message)

    response = run_flow(text_input)

    try:
        text = response["outputs"][0]["outputs"][0]["results"]["message"]["data"]["text"]
    except Exception as e:
        text = f"Error extracting response: {e}\nFull response:\n{json.dumps(response, indent=2)}"

    await cl.Message(content=text).send()
