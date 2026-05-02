import os
import time
from dotenv import load_dotenv
from pyrx_synapse import Synapse
load_dotenv()
with Synapse(api_key=os.environ["SYNAPSE_API_KEY"], workspace_id=os.environ["SYNAPSE_WORKSPACE_ID"], base_url=os.environ.get("SYNAPSE_API_URL", "https://synapse-api.pyrx.tech")) as client:
    slug = f"tpl-update-{int(time.time())}"
    client.templates.create({
        "slug": slug,
        "name": "Update Test",
        "subject": "Original subject",
        "body_html": "<h1>Hi</h1>",
        "sender_name": "Synapse",
        "from_email": "noreply@example.com",
    })
    updated = client.templates.update(slug, params={"subject": "Your order is confirmed!", "body_html": "<h1>Updated!</h1>"})
    print("Updated:", updated)
    # Cleanup
    try:
        client.templates.delete(slug)
    except Exception:
        pass
