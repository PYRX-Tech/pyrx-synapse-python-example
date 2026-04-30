import os
from dotenv import load_dotenv
from pyrx_synapse import Synapse
load_dotenv()
with Synapse(api_key=os.environ["SYNAPSE_API_KEY"], workspace_id=os.environ["SYNAPSE_WORKSPACE_ID"], base_url=os.environ.get("SYNAPSE_API_URL", "https://synapse-api.pyrx.tech")) as client:
    # contacts.get() requires a UUID. List first to get one.
    contacts = client.contacts.list(page=1, limit=1)
    if contacts.get("data"):
        contact = client.contacts.get(contacts["data"][0]["id"])
        print("Contact:", contact)
    else:
        print("No contacts. Run identify_contact.py first.")
