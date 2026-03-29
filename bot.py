import time, json
from pocketoptionapi.stable_api import PocketOption
import pocketoptionapi.global_value as global_value

global_value.loglevel = 'INFO'

# ── Configure your session here ──────────────────────────────
ssid = """42["auth",{"session":"uemer33jbaqgnpfs5b72ha5nmn","isDemo":1,"uid":127983099,"platform":2}]"""
demo = True

# ── Pairs you want to watch ───────────────────────────────────
PAIRS = ["#EURUSD_otc", "#GBPUSD_otc", "#EURGBP_otc"]
PERIOD = 60  # candle period in seconds

api = PocketOption(ssid, demo)
api.connect()

def start():
    while not global_value.websocket_is_connected:
        time.sleep(0.1)
    time.sleep(2)

    balance = api.get_balance()
    print(f"Balance: {balance}")

    while True:
        for pair in PAIRS:
            df = api.get_candles(pair, PERIOD)
            if df is not None and len(df) > 0:
                last = df.iloc[-1]
                print(f"{pair} | time: {last['time']} | open: {last['open']} | high: {last['high']} | low: {last['low']} | close: {last['close']}")
            else:
                print(f"{pair} | no data yet")
        print("─" * 60)
        time.sleep(PERIOD)

if __name__ == "__main__":
    start()
