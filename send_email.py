import os
from dotenv import load_dotenv
from pyrx_synapse import Synapse
load_dotenv()
with Synapse(api_key=os.environ["SYNAPSE_API_KEY"], workspace_id=os.environ["SYNAPSE_WORKSPACE_ID"], base_url=os.environ.get("SYNAPSE_API_URL", "https://synapse-api.pyrx.tech")) as client:
    try:
        result = client.send(template_slug="welcome-email", to={"user_id": "user_123", "email": "jane@example.com"}, attributes={"first_name": "Jane"})
        print("Email sent:", result)
    except Exception as e:
        print(f"Send failed (expected if template doesn't exist): {e}")
