## Waitress + Flask Send file Memory Bug

## Pre-setup

If you don't have a folder containing music files, please download the following sample of 6 audio files from my Google Drive and extract it to a folder:

[Post Malone - F-1 Trillion Long Bed](https://drive.google.com/file/d/1B8wJNiniI8hl8PvcqM0r6DbgTxsusIom/view?usp=sharing)

> [!IMPORTANT]
> Replace the `MUSIC_FOLDER` variable with the path to the folder containing the music files.


### 1. Install dependencies and run the server
```bash
python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
python main.py
```

### 2. Testing

Open the task manager and search for the "python" process for this server.

1. Open http://localhost:1980 in your browser. You should see a list of music files diplayed. 
2. Ctrl + Click on different files to play them on a new tab
3. Observe the memory usage on the task manager after playing each file
4. Comment out the `waitress.serve` line (L39) in `main.py` and uncomment the `app.run` line (L37).
5. Run the server again, repeat steps 2 and 3.

