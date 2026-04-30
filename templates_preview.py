import os
from dotenv import load_dotenv
from pyrx_synapse import Synapse
load_dotenv()
with Synapse(api_key=os.environ["SYNAPSE_API_KEY"], workspace_id=os.environ["SYNAPSE_WORKSPACE_ID"], base_url=os.environ.get("SYNAPSE_API_URL", "https://synapse-api.pyrx.tech")) as client:
    preview = client.templates.preview("welcome-email", params={
        "contact": {"email": "jane@example.com", "first_name": "Jane", "properties": {"plan": "growth"}},
    })
    print("Subject:", preview.get("subject"))
    print("HTML:", str(preview.get("html", ""))[:200])
