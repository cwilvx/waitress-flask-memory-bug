## Waitress + Flask Send file Memory Bug
This repo provides code to reproduce a possible memory leak on Waitress `v3.0.2` which happens when you return files using `send_file` or `send_from_directory` on a Flask app running on Waitress.

The repo contains a simple Flask app that displays a list of files in the specified folder (on /) and allows you to play them by opening them in a new tab.

Issues on Waitress's Github Repo: https://github.com/Pylons/waitress/issues/461

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

Open the task manager and search for the "python" process for this server. You can search for "main.py" to find it.

1. Open http://localhost:1980 in your browser. You should see a list of music files diplayed. 
2. Ctrl + Click on different files to open them on a new tab
3. Observe the memory usage on the task manager after opening each file
4. Comment out the `waitress.serve` line (L39) in `main.py` and uncomment the `app.run` line (L37).
5. Run the server again, repeat steps 2 and 3.

> [!TIP]
> If you don't see the list of files displayed, please confirm that the `MUSIC_FOLDER` variable is correct.

## Notes

1. Serving the app with `werkzeug` or `bjoern` does not reproduce the bug.
2. Flask's `send_file` and `send_from_directory` both reproduce the bug.
3. I'm not sure if this affects other types of files, I've only tested with audio files.