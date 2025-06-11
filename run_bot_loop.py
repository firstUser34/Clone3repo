import os
import time
import subprocess

# === CONFIGURATION ===
TOTAL_RUNS = 200   # Number of times to run the bot (change as needed)
DELAY_BETWEEN_RUNS = 300  # Delay in seconds between runs (e.g., 300s = 5min)
BOT_COMMAND = [
    "python3", "-u", "ultimate_bot_tor.py", 
    "https://x.com/Hitansh54/status/1931754193489957133",           # CHANGE to your target URL
    "--target", "2000",              # CHANGE to your desired view count
    "--headless",                    # Add/remove flags as needed
    "--tor"
]
LOGFILE_NAME = "full_run_log.txt"

# === END CONFIGURATION ===

with open(LOGFILE_NAME, "a") as logfile:
    for i in range(TOTAL_RUNS):
        header = f"\n--- Run {i+1}/{TOTAL_RUNS} ---\n"
        print(header)
        logfile.write(header)
        logfile.flush()

        print("🔄 Restarting Tor service...")
        logfile.write("🔄 Restarting Tor service...\n")
        logfile.flush()
        os.system("sudo service tor restart")
        time.sleep(10)

        print("🌐 Fetching new Tor IP...")
        logfile.write("🌐 Fetching new Tor IP...\n")
        logfile.flush()
        ip = os.popen("curl --socks5 127.0.0.1:9050 https://api.ipify.org").read().strip()
        print(f"✅ New Tor IP: {ip}")
        logfile.write(f"✅ New Tor IP: {ip}\n")
        logfile.flush()

        print(f"🤖 Launching bot: {' '.join(BOT_COMMAND)}\n")
        logfile.write(f"🤖 Launching bot: {' '.join(BOT_COMMAND)}\n")
        logfile.flush()

        # Run the bot and stream output to both console and log file
        process = subprocess.Popen(
            BOT_COMMAND,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            universal_newlines=True,
            bufsize=1
        )

        for line in iter(process.stdout.readline, ''):
            print(line, end='')           # Terminal output
            logfile.write(line)           # Log file output
            logfile.flush()

        process.stdout.close()
        process.wait()

        print(f"⏳ Waiting {DELAY_BETWEEN_RUNS} seconds before next run...\n")
        logfile.write(f"⏳ Waiting {DELAY_BETWEEN_RUNS} seconds before next run...\n\n")
        logfile.flush()
        time.sleep(DELAY_BETWEEN_RUNS)

print("✅ All runs complete.")
