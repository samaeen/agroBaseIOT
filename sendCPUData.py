from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import psutil
import time
from datetime import datetime

# InfluxDB setup
url = "http://localhost:8086"  # Replace with your InfluxDB host if needed
token = "vonTBJH6Zpa9NkIU4WXO0umjjsV-SZ9vpxj0h0BuIGv2Rop4ZVrnJPfJPS4tLYUb0wxxGN25RqleBEd0suBgag=="
org = "shoummo"               # Replace with your actual organization name
bucket = "shoummo"         # Replace with your actual bucket name

# Create client
client = InfluxDBClient(url=url, token=token, org=org)
write_api = client.write_api(write_options=SYNCHRONOUS)

# Send CPU data every 5 seconds
while True:
    cpu = psutil.cpu_percent()
    point = Point("cpu_metrics").field("cpu_usage", cpu).time(datetime.utcnow())
    write_api.write(bucket=bucket, org=org, record=point)
    print(f"[{datetime.utcnow()}] Sent CPU usage: {cpu}%")
    time.sleep(5)



