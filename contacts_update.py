import os
from dotenv import load_dotenv
from pyrx_synapse import Synapse
load_dotenv()
with Synapse(api_key=os.environ["SYNAPSE_API_KEY"], workspace_id=os.environ["SYNAPSE_WORKSPACE_ID"]) as client:
    updated = client.contacts.update("user_123", data={"email": "new@example.com", "properties": {"plan": "growth"}})
    print("Updated:", updated)
