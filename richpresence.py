import time
from flask import Flask, request, jsonify
from flask_cors import CORS
from pypresence import Presence
from math import floor

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Initialize pypresence client
client_id = 'YOUR_APPLICATION_ID'  # Replace with your Discord application's client ID
RPC = Presence(client_id)
RPC.connect()

# Global variable to store the latest activity
latest_activity = {}

@app.route('/activity', methods=['POST'])
def receive_activity():
    global latest_activity
    latest_activity = request.json
    print(latest_activity)  # For debugging
    return jsonify({'status': 'success'}), 200

def update_discord_status():
    try:
        if latest_activity['type'] == 'video':
            state_message = "Paused" if latest_activity['isPaused'] else f"By {latest_activity['videoAuthor']}"
            RPC.update(
                state=state_message,
                details=f"{latest_activity.get('videoTitle', 'Unknown Title')}",
                large_image=f"https://img.youtube.com/vi/{latest_activity['videoId']}/sddefault.jpg",
                large_text=f"Duration: {latest_activity['videoDuration']}s",
                small_image="play" if not latest_activity['isPaused'] else "pause",
                start=floor(int(time.time() - latest_activity['currentTimeElapsed'])),
                end=floor(int(time.time() + latest_activity['videoDuration'] - latest_activity['currentTimeElapsed'])),
                buttons=[{"label": "Watch Video", "url": latest_activity.get('url', '')}]
            )
        elif latest_activity['type'] == 'search':
            RPC.update(
                state=f"Searching for {latest_activity['searchTerm']}",
                large_image="https://media1.tenor.com/m/QNpNzNspQmgAAAAC/cat-kitten.gif", # Replace with your own gif idea
                buttons=[{"label": "Search", "url": latest_activity['videoUrl']}]
            )
        elif latest_activity['type'] == 'shorts':
            RPC.update(
                state="Watching Brainrot (Shorts)",
                large_image="https://media1.tenor.com/m/1L6AmSdb5swAAAAC/squidward-meme.gif", # Replace with your own gif idea
                buttons=[{"label": "Lose braincells", "url": latest_activity.get('url', '')}]
            )
        else:
            RPC.update(
                state="Browsing YouTube",
                details=f"Page: {latest_activity['page']}",
                large_image="https://media.tenor.com/JprStizZPeEAAAAi/youtube-logo-youtube-play-button.gif",
                buttons=[{"label": "Watch Video", "url": latest_activity['videoUrl']}]
            )
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    # Start the Flask server in a separate thread
    from threading import Thread
    server_thread = Thread(target=lambda: app.run(debug=True, use_reloader=False))
    server_thread.start()

    # Periodically update Discord status
    while True:
        update_discord_status()
        time.sleep(1)  # Update every second
