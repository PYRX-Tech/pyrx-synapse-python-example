import asyncio
import os
from dotenv import load_dotenv
from pyrx_synapse import AsyncSynapse
load_dotenv()

async def main():
    async with AsyncSynapse(
        api_key=os.environ["SYNAPSE_API_KEY"],
        workspace_id=os.environ["SYNAPSE_WORKSPACE_ID"],
        base_url=os.environ.get("SYNAPSE_API_URL", "https://synapse-api.pyrx.tech"),
    ) as client:
        await client.track(external_id="async_test", event_name="async_event", attributes={"src": "async"})
        await client.identify(external_id="async_test", email="async@test.com")
        print("Async operations completed")

asyncio.run(main())
