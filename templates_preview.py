import os
from dotenv import load_dotenv
from pyrx_synapse import Synapse
load_dotenv()
with Synapse(api_key=os.environ["SYNAPSE_API_KEY"], workspace_id=os.environ["SYNAPSE_WORKSPACE_ID"], base_url=os.environ.get("SYNAPSE_API_URL", "https://synapse-api.pyrx.tech")) as client:
    # Create a template to preview
    try:
        client.templates.create({"slug": "sdk-preview-test", "name": "Preview Test", "subject": "Hi {the user's First Name}", "body_html": "<p>Hello {the user's First Name}</p>", "sender_name": "Test", "from_email": "test@example.com"})
    except Exception:
        pass
    preview = client.templates.preview("sdk-preview-test", params={"contact": {"email": "jane@example.com", "first_name": "Jane"}})
    print("Subject:", getattr(preview, 'subject', None) or preview.get('subject') if isinstance(preview, dict) else preview.subject)
    # Cleanup
    try:
        client.templates.delete("sdk-preview-test")
    except Exception:
        pass
