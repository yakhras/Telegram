from telethon import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
from datetime import datetime, timedelta, timezone
from bidi.algorithm import get_display
from langdetect import detect
import asyncio
import json
import time

# Your Telegram API credentials
api_id = '22204672'
api_hash = 'c0113582134ed3cec1887c842ac9035e'

# Create a Telegram client session
client = TelegramClient('user_session', api_id, api_hash)

# Load channels from a JSON configuration file
with open('channels.json', 'r') as file:
    channels = json.load(file)["channels"]


async def fetch_messages_from_channel(channel_name):
    """
    Fetch messages from a single channel.
    """
    try:
        # Get the channel entity
        channel = await client.get_entity(channel_name)

        # Fetch the last 10 messages
        history = await client(GetHistoryRequest(
            peer=channel,
            limit=10,
            offset_date=None,
            offset_id=0,
            max_id=0,
            min_id=0,
            add_offset=0,
            hash=0
        ))

        now = datetime.now(timezone.utc)  # Make it timezone-aware
        today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)
        today_end = today_start + timedelta(days=1)

        # Process messages
        messages = [message for message in history.messages if today_start <= message.date < today_end]
        print(f"Fetched {len(messages)} messages from {channel_name}")

        return {channel_name: messages}
    
    except Exception as e:
        print(f"Error fetching messages from {channel_name}: {e}")
        return {channel_name: []}
 
async def fetch_messages_from_channels(channels):
    """
    Fetch messages from all channels in batches to handle rate limits.
    """
    results = {}
    batch_size = 5  # Process 5 channels at a time
    delay_between_batches = 2  # Delay in seconds between batches

    for i in range(0, len(channels), batch_size):
        batch = channels[i:i + batch_size]

        # Process the batch concurrently
        batch_results = await asyncio.gather(*[fetch_messages_from_channel(channel) for channel in batch])

        # Merge results
        for result in batch_results:
            results.update(result)

        print(f"Processed batch {i // batch_size + 1}/{(len(channels) + batch_size - 1) // batch_size}")
        time.sleep(delay_between_batches)  # Respect API limits

    return results

# Main function to execute the script
with client:
    messages = client.loop.run_until_complete(fetch_messages_from_channels(channels))
    for channel, msgs in messages.items():
        print(f"\nMessages from {channel}:")
        for msg in msgs:
            if msg:
                print(f"- {msg}")
