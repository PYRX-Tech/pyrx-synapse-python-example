import os
from dotenv import load_dotenv
from pyrx_synapse import Synapse
load_dotenv()
with Synapse(api_key=os.environ["SYNAPSE_API_KEY"], workspace_id=os.environ["SYNAPSE_WORKSPACE_ID"], base_url=os.environ.get("SYNAPSE_API_URL", "https://synapse-api.pyrx.tech")) as client:
    template = client.templates.create({
        "slug": "order-confirm",
        "name": "Order Confirmation",
        "subject": "Order confirmed",
        "body_html": "<h1>Hi {the user's First Name}</h1><p>Your order is confirmed.</p>",
        "sender_name": "Synapse",
        "from_email": "noreply@example.com",
    })
    print("Created:", template)
