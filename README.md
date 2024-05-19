# YouTube RichPresence

YouTube RichPresence is a Chrome extension that tracks your YouTube activity (video playing, browsing, searching, and watching Shorts) and posts the activity to a localhost server. This activity is then displayed on Discord using pypresence. This is a beta version with a lot of imporovements to be done.

## Features

- Detects when a YouTube video is playing, paused, or when browsing/searching.
- Sends activity data (including video title, author, URL, etc.) to a localhost server.
- Updates your Discord status with the activity information.

## Prerequisites

- Python 3.x
- Google Chrome
- Flask
- pypresence
- flask-cors

## Installation

### Step 1: Set Up the Chrome Extension

1. Clone this repository:
   ```bash
   git clone https://github.com/JanLewDev/YouTube_RichPresence.git
   cd YouTube_RichPresence
2. Open `chrome://extensions/` in Chrome
3. Enable "Developer Mode"
4. Click on "Load unpacked" and select the extension directory from this repository.
5. Install the required Python packages with
    ```bash
    pip install flask pypresence flask-cors
6. Go to the [Discord Developer Portal](https://discord.com/developers/applications) and create an application
7. Update `richpresence.py` with the generated applicaiton id
8. Run the Flask server and the presence updater with
    ```bash
    python richpresence.py

## File structure
<pre>
. 
├── extension  
│   ├── manifest.json  
│   ├── background.js  
│   ├── content.js  
│   ├── popup.html  
│   └── icons  
│       └── yt.jpg  
└── richpresence.py


