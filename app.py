from flask import Flask, render_template, request
from flask_cors import CORS

app = Flask(__name__, template_folder="templates", static_folder="static")
CORS(app, resources={r"*": {"origins": "*"}})

dlist = ["gazipur", 'dhaka', 'bangladesh']

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        kwrd = request.form.get("keyword")
        results = []
        if kwrd is not None and kwrd != "":
            for lst in dlist:
                if lst.__contains__(kwrd):
                    results.append(lst)
        return {
            "results": results
        }

if __name__ == "__main__":
    app.run(debug=True)