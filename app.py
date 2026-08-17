<<<<<<< HEAD
from flask import Flask, render_template, request
import fitz
import os
import re
from collections import Counter

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    if "pdf" not in request.files:
        return "No PDF uploaded"

    file = request.files["pdf"]

    if file.filename == "":
        return "Please select a PDF"

    if not file.filename.lower().endswith(".pdf"):
        return "Only PDF files are allowed"

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )

    file.save(filepath)

    # Open PDF
    document = fitz.open(filepath)

    total_pages = len(document)

    full_text = ""

    # Extract text from every page
    for page in document:
        text = page.get_text()
        full_text += text + "\n"

    document.close()

    # Basic analysis
    words = re.findall(r"\b[a-zA-Z]+\b", full_text)

    word_count = len(words)

    character_count = len(full_text)

    # Find common words
    word_frequency = Counter(
        word.lower() for word in words
    )

    common_words = word_frequency.most_common(10)

    return render_template(
        "index.html",
        filename=file.filename,
        pages=total_pages,
        words=word_count,
        characters=character_count,
        text=full_text,
        common_words=common_words
    )


if __name__ == "__main__":
=======
from flask import Flask, render_template, request
import fitz
import os
import re
from collections import Counter

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    if "pdf" not in request.files:
        return "No PDF uploaded"

    file = request.files["pdf"]

    if file.filename == "":
        return "Please select a PDF"

    if not file.filename.lower().endswith(".pdf"):
        return "Only PDF files are allowed"

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )

    file.save(filepath)

    # Open PDF
    document = fitz.open(filepath)

    total_pages = len(document)

    full_text = ""

    # Extract text from every page
    for page in document:
        text = page.get_text()
        full_text += text + "\n"

    document.close()

    # Basic analysis
    words = re.findall(r"\b[a-zA-Z]+\b", full_text)

    word_count = len(words)

    character_count = len(full_text)

    # Find common words
    word_frequency = Counter(
        word.lower() for word in words
    )

    common_words = word_frequency.most_common(10)

    return render_template(
        "index.html",
        filename=file.filename,
        pages=total_pages,
        words=word_count,
        characters=character_count,
        text=full_text,
        common_words=common_words
    )


if __name__ == "__main__":
>>>>>>> f437e02692caf68b941828b46d8ce1677cd8b116
    app.run(debug=True)