import time
from datetime import datetime
import psycopg2
from twelvedata import TDClient

# Database connection parameters (replace with your Tiger Cloud credentials)
DB_HOST = "<YOUR_TIGER_HOST>"
DB_NAME = "tsdb"
DB_USER = "tsdb"
DB_PASSWORD = "<YOUR_DB_PASSWORD>"
DB_PORT = "5432"

def insert_tick(event):
    if event.get("event") == "price":
        symbol = event.get("symbol")
        price = event.get("price")
        day_volume = event.get("day_volume")
        timestamp = event.get("timestamp") # Unix timestamp
        dt = datetime.utcfromtimestamp(timestamp)

        try:
            conn = psycopg2.connect(
                host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASSWORD, port=DB_PORT
            )
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO crypto_ticks (time, symbol, price, day_volume) VALUES (%s, %s, %s, %s);",
                (dt, symbol, price, day_volume)
            )
            conn.commit()
            cur.close()
            conn.close()
            print(f"Inserted: {symbol} at ${price}")
        except Exception as e:
            print(f"Database error: {e}")

# Initialize Twelve Data Client (replace with your Twelve Data API key)
td = TDClient(apikey="<YOUR_TWELVE_DATA_API_KEY>")

# Connect to the websocket server and listen for cryptocurrency trades
ws = td.websocket(symbols=["BTC/USD", "ETH/USD"], on_event=insert_tick)
ws.connect()

while True:
    ws.heartbeat()
    time.sleep(10)