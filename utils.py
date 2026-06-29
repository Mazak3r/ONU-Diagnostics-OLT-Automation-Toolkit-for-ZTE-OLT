import json
import asyncio
import telnetlib3
import socket
import re

def load_config():
    with open('config.json', 'r') as f:
        return json.load(f)

def check_reachability(ip, port=23, timeout=3):
    try:
        with socket.create_connection((ip, port), timeout=timeout):
            return True
    except (socket.timeout, socket.error):
        return False

async def connect_to_olt(olt_ip, onu_type, olt_port, onu_id, creds):
    result_lines = []
    try:
        reader, writer = await telnetlib3.open_connection(olt_ip, 23, connect_minwait=0.05, connect_maxwait=1)
        writer.write(f"{creds['user']}\n")
        await asyncio.sleep(0.5)
        writer.write(f"{creds['pass']}\n")
        await asyncio.sleep(0.5)

        # Logic to extract data (simplified for brevity)
        state_command = f"show {onu_type.lower()} onu state {olt_port}\n"
        writer.write(state_command)
        
        # ... (Include your existing parsing logic here)
        result_lines.append("Connection successful. Analysis complete.")
        
    except Exception as e:
        result_lines.append(f"Error: {str(e)}")
    return result_lines
