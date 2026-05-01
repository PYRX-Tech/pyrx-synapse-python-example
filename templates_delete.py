import os
from dotenv import load_dotenv
from pyrx_synapse import Synapse
load_dotenv()
with Synapse(api_key=os.environ["SYNAPSE_API_KEY"], workspace_id=os.environ["SYNAPSE_WORKSPACE_ID"], base_url=os.environ.get("SYNAPSE_API_URL", "https://synapse-api.pyrx.tech")) as client:
    # Create then delete
    try:
        client.templates.create({"slug": "sdk-del-test", "name": "Del Test", "subject": "Test", "body_html": "<p>Hi</p>", "sender_name": "Test", "from_email": "test@example.com"})
    except Exception:
        pass
    client.templates.delete("sdk-del-test")
    print("Template deleted")
