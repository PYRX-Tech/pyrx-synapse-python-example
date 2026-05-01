import os
import time
from dotenv import load_dotenv
from pyrx_synapse import Synapse
load_dotenv()
with Synapse(api_key=os.environ["SYNAPSE_API_KEY"], workspace_id=os.environ["SYNAPSE_WORKSPACE_ID"], base_url=os.environ.get("SYNAPSE_API_URL", "https://synapse-api.pyrx.tech")) as client:
    slug = f"tpl-create-{int(time.time())}"
    template = client.templates.create({
        "slug": slug,
        "name": "Create Test",
        "subject": "Order confirmed",
        "body_html": "<h1>Hi</h1><p>Your order is confirmed.</p>",
        "sender_name": "Synapse",
        "from_email": "noreply@example.com",
    })
    print("Created:", template)
    # Cleanup
    try:
        client.templates.delete(slug)
    except Exception:
        pass
