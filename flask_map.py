from flask import Flask, render_template
from flask import request, redirect, url_for
import getting_user_locations

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def map():
    global user_input

    if request.method == "POST":
        user_input = request.form.get('username')
        print(user_input)

        if user_input[0] != "@":
            user_input = "@" + user_input
        print(user_input)

        return redirect(url_for("waiting"))

    return render_template("index.html")


@app.route("/map")
def waiting():
    print("Getting locations...")
    context = {"html_map": getting_user_locations.find_locations(user_input)}
    print("Locations found")

    return render_template("html_map", **context)


if __name__ == '__main__':
    app.run(debug=True)
