import os
from dotenv import load_dotenv
from pyrx_synapse import Synapse

load_dotenv()

with Synapse(
    api_key=os.environ["SYNAPSE_API_KEY"],
    workspace_id=os.environ["SYNAPSE_WORKSPACE_ID"],
) as client:
    client.send(
        template_slug="welcome-email",
        to={"user_id": "user_123", "email": "jane@example.com"},
        attributes={"first_name": "Jane", "plan": "starter"},
    )
    print("Email sent successfully")
