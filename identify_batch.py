import os
from dotenv import load_dotenv
from pyrx_synapse import Synapse
load_dotenv()
with Synapse(api_key=os.environ["SYNAPSE_API_KEY"], workspace_id=os.environ["SYNAPSE_WORKSPACE_ID"]) as client:
    result = client.identify_batch(contacts=[
        {"external_id": "user_1", "email": "alice@example.com", "properties": {"plan": "starter"}},
        {"external_id": "user_2", "email": "bob@example.com", "properties": {"plan": "growth"}},
    ])
    print("Batch identified:", result)
