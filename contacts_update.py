import os
from dotenv import load_dotenv
from pyrx_synapse import Synapse
load_dotenv()
with Synapse(api_key=os.environ["SYNAPSE_API_KEY"], workspace_id=os.environ["SYNAPSE_WORKSPACE_ID"], base_url=os.environ.get("SYNAPSE_API_URL", "https://synapse-api.pyrx.tech")) as client:
    # First identify to ensure contact exists
    client.identify(external_id="sdk_update_test", email="update@example.com")
    updated = client.contacts.update("sdk_update_test", data={"properties": {"plan": "growth"}})
    print("Updated:", updated)
