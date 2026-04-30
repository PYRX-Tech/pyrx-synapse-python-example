import asyncio
import os
from dotenv import load_dotenv
from pyrx_synapse import AsyncSynapse

load_dotenv()

async def main():
    async with AsyncSynapse(
        api_key=os.environ["SYNAPSE_API_KEY"],
        workspace_id=os.environ["SYNAPSE_WORKSPACE_ID"],
    ) as client:
        await client.track(
            external_id="user_123",
            event_name="user_signed_up",
            attributes={"plan": "starter"},
        )
        await client.identify(
            external_id="user_123",
            email="jane@example.com",
        )
        print("Async operations completed")

asyncio.run(main())
