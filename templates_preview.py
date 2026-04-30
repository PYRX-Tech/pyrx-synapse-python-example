import os
from dotenv import load_dotenv
from pyrx_synapse import Synapse
load_dotenv()
with Synapse(api_key=os.environ["SYNAPSE_API_KEY"], workspace_id=os.environ["SYNAPSE_WORKSPACE_ID"]) as client:
    preview = client.templates.preview("welcome-email", params={"attributes": {"first_name": "Jane", "plan": "growth"}})
    print("Subject:", preview.get("subject"))
    print("HTML:", preview.get("html", "")[:200])
