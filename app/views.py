from flask import Blueprint, render_template, request
from .analyzer import analyze_code

main = Blueprint('main', __name__)

@main.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        code = request.form.get("code")
        if not code:
            return render_template("index.html", error="Please provide a code snippet.")

        # Analyze the code
        result = analyze_code(code) # result is a dictionary with issues and suggestions
        return render_template("index.html", result=result, code=code)

    return render_template("index.html")
