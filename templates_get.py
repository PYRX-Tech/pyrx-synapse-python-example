import os
from dotenv import load_dotenv
from pyrx_synapse import Synapse
load_dotenv()
with Synapse(api_key=os.environ["SYNAPSE_API_KEY"], workspace_id=os.environ["SYNAPSE_WORKSPACE_ID"], base_url=os.environ.get("SYNAPSE_API_URL", "https://synapse-api.pyrx.tech")) as client:
    # Create a template first to ensure it exists
    try:
        client.templates.create({"slug": "sdk-get-test", "name": "Get Test", "subject": "Test", "body_html": "<p>Hi</p>", "sender_name": "Test", "from_email": "test@example.com"})
    except Exception:
        pass  # may already exist
    template = client.templates.get("sdk-get-test")
    print("Template:", template)
    # Cleanup
    try:
        client.templates.delete("sdk-get-test")
    except Exception:
        pass
