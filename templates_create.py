import os
from dotenv import load_dotenv
from pyrx_synapse import Synapse
load_dotenv()
with Synapse(api_key=os.environ["SYNAPSE_API_KEY"], workspace_id=os.environ["SYNAPSE_WORKSPACE_ID"]) as client:
    template = client.templates.create({"slug": "order-confirm", "name": "Order Confirmation", "subject": "Order confirmed", "body": "Hi {the user's First Name}, your order is confirmed."})
    print("Created:", template)
