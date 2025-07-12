from flask import Flask, render_template, request

app = Flask(__name__)

# Data buku
data_buku = {
    "AI for Beginners": {"AI", "ML", "Beginner"},
    "Deep Learning with Python": {"AI", "Deep Learning"},
    "Data Science Essentials": {"Data", "ML"},
    "AI and Ethics": {"AI", "Philosophy"},
}

@app.route("/", methods=["GET", "POST"])
def index():
    rekomendasi = []
    genre = ""

    if request.method == "POST":
        genre = request.form["genre"].strip().title()
        for judul, kategori in data_buku.items():
            if genre in kategori:
                rekomendasi.append(judul)

    return render_template("index.html", rekomendasi=rekomendasi, genre=genre)

if __name__ == "__main__":
    app.run(debug=True)
