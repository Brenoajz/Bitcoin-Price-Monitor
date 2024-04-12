import asyncio
from pycoingecko import CoinGeckoAPI
import json
from datetime import datetime
from telegram import Bot

cg = CoinGeckoAPI()

bot_token = 'SEU_TOKEN_DO_BOT_DO_TELEGRAM'
chat_id = 'SEU_CHAT_ID'

previous_price = None

async def send_message_async(chat_id, message):
    bot = Bot(token=bot_token)
    await bot.send_message(chat_id=chat_id, text=message)

def save_to_json(records):
    with open('price_records.json', 'w') as file:
        json.dump(records, file, indent=4)

async def main():
    global previous_price

    price_records = []

    while True:
        btc_price = cg.get_price(ids='bitcoin', vs_currencies='brl')
        current_price = btc_price['bitcoin']['brl']
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        if previous_price is None or current_price != previous_price:
            if previous_price is not None:
                if current_price > previous_price:
                    change = "up"
                elif current_price < previous_price:
                    change = "down"
                else:
                    change = "unchanged"
                    
                percentage_change = ((current_price - previous_price) / previous_price) * 100

                message = f"ℹ️ Bitcoin price update:\n\n⏰ Time: {current_time}\n\n💰 Price: R$ {current_price:.2f}\n\n📈 Change: {change} ({percentage_change:.2f}%)\n"

                await send_message_async(chat_id, message)

                record = {
                    "datetime": current_time,
                    "price": current_price,
                    "change": change,
                    "percentage_change": percentage_change
                }
                price_records.append(record)

                save_to_json(price_records)

            else:
                pass

            previous_price = current_price

        await asyncio.sleep(10)

asyncio.run(main())
