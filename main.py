import multiprocessing
import os
import subprocess
import time

def run_bot():
    print("🤖 Starting Telegram Bot...")
    subprocess.run(["python", "bot.py"])

def run_dashboard():
    print("🖥️ Starting Admin Dashboard...")
    # Use Gunicorn in production if possible, otherwise fallback to flask run
    # For Railway, we can use the environment variable PORT
    port = os.getenv("PORT", "5000")
    subprocess.run(["python", "dashboard.py"])

if __name__ == "__main__":
    # Start both processes
    p1 = multiprocessing.Process(target=run_bot)
    p2 = multiprocessing.Process(target=run_dashboard)

    p1.start()
    p2.start()

    print("🚀 Both services are starting...")

    try:
        p1.join()
        p2.join()
    except KeyboardInterrupt:
        print("🛑 Stopping services...")
        p1.terminate()
        p2.terminate()
