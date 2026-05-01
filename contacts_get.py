import os
from dotenv import load_dotenv
from pyrx_synapse import Synapse
load_dotenv()
with Synapse(api_key=os.environ["SYNAPSE_API_KEY"], workspace_id=os.environ["SYNAPSE_WORKSPACE_ID"], base_url=os.environ.get("SYNAPSE_API_URL", "https://synapse-api.pyrx.tech")) as client:
    contacts = client.contacts.list(page=1, per_page=1)
    data = contacts.get("data") if isinstance(contacts, dict) else getattr(contacts, "data", [])
    if data:
        cid = data[0]["id"] if isinstance(data[0], dict) else data[0].id
        contact = client.contacts.get(cid)
        print("Contact:", contact)
    else:
        print("No contacts found")
