import waitress
from pathlib import Path
from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)

MUSIC_FOLDER = (
    "/home/cwilvx/download/Albums/Post Malone - F-1 Trillion Long Bed(Explicit)"
)


@app.route("/")
def index():
    files = Path(MUSIC_FOLDER).glob("**/*.flac")
    # Convert to relative paths and sort for better display
    relative_files = [str(file.relative_to(MUSIC_FOLDER)) for file in files]
    relative_files.sort()

    return render_template(
        "index.html", files=relative_files, music_folder=MUSIC_FOLDER
    )


@app.route("/file")
def stream_file():
    filepath = request.args.get("filepath")
    path = Path(filepath)
    print("Serving file:", path)

    if not path.exists():
        return "File not found", 404

    return send_from_directory(path.parent, path.name)


if __name__ == "__main__":
    # app.run(host="0.0.0.0", debug=False,port=1980)
    print("Starting server on: http://localhost:1980")
    waitress.serve(app=app, port=1980)
