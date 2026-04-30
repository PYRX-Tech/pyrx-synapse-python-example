import os
from dotenv import load_dotenv
from pyrx_synapse import Synapse
load_dotenv()
with Synapse(api_key=os.environ["SYNAPSE_API_KEY"], workspace_id=os.environ["SYNAPSE_WORKSPACE_ID"], base_url=os.environ.get("SYNAPSE_API_URL", "https://synapse-api.pyrx.tech")) as client:
    updated = client.templates.update("order-confirm", params={"subject": "Your order is confirmed!", "body_html": "<h1>Updated!</h1>"})
    print("Updated:", updated)
