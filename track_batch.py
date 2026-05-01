import os
from dotenv import load_dotenv
from pyrx_synapse import Synapse
load_dotenv()
with Synapse(api_key=os.environ["SYNAPSE_API_KEY"], workspace_id=os.environ["SYNAPSE_WORKSPACE_ID"], base_url=os.environ.get("SYNAPSE_API_URL", "https://synapse-api.pyrx.tech")) as client:
    result = client.track_batch(events=[
        {"external_id": "user_1", "event_name": "page_viewed", "attributes": {"page": "/pricing"}},
        {"external_id": "user_2", "event_name": "feature_used", "attributes": {"feature": "export"}},
    ])
    print("Batch tracked:", result)
