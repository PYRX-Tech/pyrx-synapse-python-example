import os
from dotenv import load_dotenv
from pyrx_synapse import Synapse
load_dotenv()
with Synapse(api_key=os.environ["SYNAPSE_API_KEY"], workspace_id=os.environ["SYNAPSE_WORKSPACE_ID"], base_url=os.environ.get("SYNAPSE_API_URL", "https://synapse-api.pyrx.tech")) as client:
    ext_id = f"del_test_{int(__import__('time').time())}"
    client.identify(external_id=ext_id, email=f"{ext_id}@test.com")
    client.contacts.delete(ext_id)
    print("Contact deleted")
