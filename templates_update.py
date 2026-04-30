import os
from dotenv import load_dotenv
from pyrx_synapse import Synapse
load_dotenv()
with Synapse(api_key=os.environ["SYNAPSE_API_KEY"], workspace_id=os.environ["SYNAPSE_WORKSPACE_ID"]) as client:
    updated = client.templates.update("order-confirm", params={"subject": "Your order is confirmed!"})
    print("Updated:", updated)
