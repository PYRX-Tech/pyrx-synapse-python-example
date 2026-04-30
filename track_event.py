import os
from dotenv import load_dotenv
from pyrx_synapse import Synapse

load_dotenv()

with Synapse(
    api_key=os.environ["SYNAPSE_API_KEY"],
    workspace_id=os.environ["SYNAPSE_WORKSPACE_ID"], base_url=os.environ.get("SYNAPSE_API_URL", "https://synapse-api.pyrx.tech"),
) as client:
    client.track(
        external_id="user_123",
        event_name="user_signed_up",
        attributes={"plan": "starter", "source": "landing_page"},
    )
    print("Event tracked successfully")
