import re
import pandas as pd
from datetime import datetime, timedelta, timezone
from telethon import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import GetHistoryRequest
import json
import time
import asyncio

# Your Telegram API credentials
api_id = '22204672'
api_hash = 'c0113582134ed3cec1887c842ac9035e'

# Create a Telegram client session
client = TelegramClient('user_session', api_id, api_hash)

# Load channels from a JSON configuration file
# with open('channels.json', 'r') as file:
#     channels = json.load(file)["channels"]


async def fetch_messages_from_channel_today(client, channel_name, limit=50):
    """
    Fetch messages from a single channel within the current day.
    """
    # Get the channel entity
    channel = await client.get_entity(channel_name)

    # Fetch the messages up to the given limit
    history = await client(GetHistoryRequest(
        peer=channel,
        limit=limit,
        offset_date=None,
        offset_id=0,
        max_id=0,
        min_id=0,
        add_offset=0,
        hash=0
    ))

    # Get today's date range with timezone awareness
    now = datetime.now(timezone.utc)  # Make it timezone-aware
    today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)
    today_end = today_start + timedelta(days=1)

    # Filter messages within the current day
    daily_messages = [message for message in history.messages if today_start <= message.date < today_end]

    # Print messages for debugging
    # for message in daily_messages:
    #     print(f"Date: {message.date}, Content: {message.message}")

    return daily_messages


def process_and_extract_sell_values(text):
    # Split text into lines
    lines = text.split('\n')

    tp_values = []
    sl_values = []
    sell_values = []
    
    for line in lines:
        stripped_line = line.strip().upper()
        if stripped_line.startswith('TP'):
            # Process 'TP' lines
            processed_line = re.sub(r'[:@-\\/]', ' ', line)
            matches = re.findall(r'\d+\.?\d*', processed_line)
            for match in matches:
                if match:
                    tp = float(match)
                    if tp > 10:
                        tp_values.append(tp)
        elif stripped_line.startswith('SL'):
            # Process 'SL' lines
            processed_line = re.sub(r'[:@-\\/]', ' ', line)
            matches = re.findall(r'\d+\.?\d*(?!\s*\()', processed_line)
            for match in matches:
                if match:
                    sl = float(match)
                    if sl > 1000:
                        sl_values.append(sl)
        elif 'SELL' in stripped_line or 'ENTRY' in stripped_line:
            # Process 'SELL' or 'ENTRY' lines
            processed_line = re.sub(r'[:@-\\/]', ' ', line)
            matches = re.findall(r'\d+\.?\d*', processed_line)
            for match in matches:
                if match:
                    sell = float(match)
                    if sell > 10:  # Adjust this condition if needed
                        sell_values.append(sell)

                        # print(sell_values)
    # Calculate averages 
    # print(sell_values)
    tp_avg = sum(tp_values) / len(tp_values) if tp_values else 0 
    sl_avg = sum(sl_values) / len(sl_values) if sl_values else 0
    sell_avg = sum(sell_values) / len(sell_values) if sell_values else 0
    return tp_avg, sl_avg, sell_avg

def process_and_extract_buy_values(text):
    # Split text into lines
    lines = text.split('\n')

    tp_values = []
    sl_values = []
    buy_values = []
    
    for line in lines:
        stripped_line = line.strip().upper()
        if stripped_line.startswith('TP'):
            # Process 'TP' lines
            processed_line = re.sub(r'[:@-\\/]', ' ', line)
            matches = re.findall(r'\d+\.?\d*', processed_line)
            for match in matches:
                if match:
                    tp = float(match)
                    if tp > 10:
                        tp_values.append(tp)
        elif stripped_line.startswith('SL'):
            # Process 'SL' lines
            processed_line = re.sub(r'[:@-\\/]', ' ', line)
            matches = re.findall(r'\d+\.?\d*(?!\s*\()', processed_line)
            for match in matches:
                if match:
                    sl = float(match)
                    if sl > 1000:
                        sl_values.append(sl)
        elif 'BUY' in stripped_line:
            # Process 'SELL' lines
            processed_line = re.sub(r'[:@-\\/]', ' ', line)
            matches = re.findall(r'\d+\.?\d*', processed_line)
            for match in matches:
                if match:
                    buy = float(match)
                    if buy > 10:
                        buy_values.append(buy)
    # Calculate averages 
    tp_avg = sum(tp_values) / len(tp_values) if tp_values else 0 
    sl_avg = sum(sl_values) / len(sl_values) if sl_values else 0
    buy_avg = sum(buy_values) / len(buy_values) if buy_values else 0
    return tp_avg, sl_avg, buy_avg

async def fetch_messages_from_channel(client, channel_name, limit=50):
    """
    Fetch messages from a single channel.
    """
    # Get the channel entity
    channel = await client.get_entity(channel_name)

    # Fetch the last 10 messages
    history = await client(GetHistoryRequest(
        peer=channel,
        limit=limit,
        offset_date=None,
        offset_id=0,
        max_id=0,
        min_id=0,
        add_offset=0,
        hash=0
    ))
    return history
    
def process_channel_sell_messages(daily_messages):
    tp_data = []
    sl_data = []
    enter_data = []
    for message in daily_messages:
        # Ensure message.message is not None before processing
        if (message.message and 
            ('XAUUSD' in message.message.upper() or 'gold' in message.message.lower()) and 
            ('TP' in message.message.upper() and 'SL' in message.message.upper())):
            if 'SELL' in message.message.upper():
                # print(message.message)
                tp_values, sl_values, sell_values = process_and_extract_sell_values(message.message)
                if tp_values > 0:
                    tp_data.append(tp_values)
                if sl_values > 0:
                    sl_data.append(sl_values)
                if sell_values > 0:
                    enter_data.append(sell_values)
    stp_avg = round(sum(tp_data) / len(tp_data) if tp_data else 0, 2)
    ssl_avg = round(sum(sl_data) / len(sl_data) if sl_data else 0, 2)
    sen_avg = round(sum(enter_data) / len(enter_data) if enter_data else 0, 2)
    return sl_data, sen_avg, stp_avg, ssl_avg

def process_channel_buy_messages(daily_messages):
    tp_data = []
    sl_data = []
    enter_data = []
    for message in daily_messages:
        # Ensure message.message is not None before processing
        if (message.message and 
            ('XAUUSD' in message.message.upper() or 'gold' in message.message.lower()) and 
            ('TP' in message.message.upper() and 'SL' in message.message.upper())):
            if 'BUY' in message.message.upper():
                # print(message.message)
                tp_values, sl_values, buy_values = process_and_extract_buy_values(message.message)
                if tp_values > 0:
                    tp_data.append(tp_values)
                if sl_values > 0:
                    sl_data.append(sl_values)
                if buy_values > 0:
                    enter_data.append(buy_values)
    btp_avg = round(sum(tp_data) / len(tp_data) if tp_data else 0, 2)
    bsl_avg = round(sum(sl_data) / len(sl_data) if sl_data else 0, 2)
    ben_avg = round(sum(enter_data) / len(enter_data) if enter_data else 0, 2)
    return sl_data, ben_avg, btp_avg, bsl_avg
    
async def send_message_to_user(client, user_id, message_text):
    """
    Send a message to a specific Telegram user.
    """
    # Get the user entity
    user = await client.get_entity(user_id)
    
    # Send the message
    await client.send_message(user, message_text)


async def main():
    delay_between_batches = 900
    channel_ids = ["https://t.me/jamesgoldmaster",
        "https://t.me/natefxctrade",
        "https://t.me/bestforexsignal",
        "https://t.me/goldtradermo",
        "https://t.me/Gary_TheTrader",
        "https://t.me/forextrade",
        "https://t.me/goldsnipers11",
        "https://t.me/GOLDUS30FREESIGNALS",
        "https://t.me/GOLDUSDMASTER",
        "https://t.me/whh521gold",
        "https://t.me/goldtradingpk",
        "https://t.me/AliZafarSheikh50",
        "https://t.me/Goldmine_Investment",
        "https://t.me/golddailysignals001",
        "https://t.me/HuracanFx_Gold",
        "https://t.me/AltSignalsFX_TradingSignals1",
        "https://t.me/FxLondonSignalsA",
        "https://t.me/Apexbullfirexsignalfx",
        "https://t.me/Signal1000Pipsbuilder",
        "https://t.me/learn2trade",
        "https://t.me/kingofchartgold",
        "https://t.me/FoxGoldSignals",
        "https://t.me/goldhunteracademyfx_fx",
        "https://t.me/Signals_OlympTrade_Quotex",
        "https://t.me/RealGoldSnipers",
        "https://t.me/goldingtrade1",
        "https://t.me/usoil_crudeoiIsignal",
        "https://t.me/Gold_SignalsOfficials",
        "https://t.me/xauusd_gold_signalfx",
        "https://t.me/fx_goldxauusdsignal1",
        "https://t.me/signale",
        "https://t.me/GOLDXAUUSDPIPSHUNTERCLUB",
        "https://t.me/FOREX_XAUUSD_GOLD_SIGNAL",
        "https://t.me/XAUUSDA",
        "https://t.me/NASDAQ_XAUUSD_US30",
        "https://t.me/MrKingTeamGoldSignals",
        "https://t.me/signal_golds1",
        "https://t.me/usoilwtisignals",
        "https://t.me/wolf_forex_fxx",
        "https://t.me/vipgoldtradermo",
        "https://t.me/safe_pip",
        "https://t.me/glaad_elgold_1",
        "https://t.me/Forex_Signals_4x",
        "https://t.me/Forex_Signals_Ocean",
        "https://t.me/Forex_Signal_Freeeeee",
        "https://t.me/Forex_Signals_Bulls1",
        "https://t.me/Forex_Signals_Level_Up"
    ]
    
    sen_total = []
    ssl_total = []
    stp_total = []
    ben_total = []
    bsl_total = []
    btp_total = []
    for channel in channel_ids:
        history = await fetch_messages_from_channel_today(client, channel) 
        # Extracting Sell Data
        ssl_data, sen_avg, stp_avg, ssl_avg = process_channel_sell_messages(history)
        if sen_avg > 0:
            sen_total.append(sen_avg)
        if ssl_avg > 0:
            ssl_total.append(ssl_avg)
        if stp_avg > 0:
            stp_total.append(stp_avg)

        # Extracting Buy Data
        bsl_data, ben_avg, btp_avg, bsl_avg = process_channel_buy_messages(history)
        if ben_avg > 0:
            ben_total.append(ben_avg)
        if bsl_avg > 0:
            bsl_total.append(bsl_avg)
        if btp_avg > 0:
            btp_total.append(btp_avg)
        

    stp_avg_total = round(sum(stp_total) / len(stp_total) if stp_total else 0, 2)
    ssl_avg_total = round(sum(ssl_total) / len(ssl_total) if ssl_total else 0, 2)
    sen_avg_total = round(sum(sen_total) / len(sen_total) if sen_total else 0, 2)

    btp_avg_total = round(sum(btp_total) / len(btp_total) if btp_total else 0, 2)
    bsl_avg_total = round(sum(bsl_total) / len(bsl_total) if bsl_total else 0, 2)
    ben_avg_total = round(sum(ben_total) / len(ben_total) if ben_total else 0, 2)
    print(sen_total)
    print(ssl_total)
    print(btp_total)
    
    bmessage_text = f'BUY: {4*len(bsl_total)}  \nEntry: {ben_avg_total}\nTP: {btp_avg_total}\nSL: {bsl_avg_total}  \n\nSELL: {4*len(ssl_total)}\nEntry: {sen_avg_total}\nTP: {stp_avg_total}\nSL: {ssl_avg_total}'
    smessage_text = f'SELL: {len(ssl_total)}  BUY: {len(bsl_total)}\nEntry: {sen_avg_total}\nTP: {stp_avg_total}\nSL: {ssl_avg_total}'

    # if bsl_data > ssl_data:
    await send_message_to_user(client, 'yakhras', bmessage_text)
    #time.sleep(delay_between_batches)
    # else:
        # await send_message_to_user(client, 'yakhras', smessage_text)
    # print(sen_avg_total)
    

with client:
    client.loop.run_until_complete(main())