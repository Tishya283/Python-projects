from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder="templates")

contacts = [
    {"name": "Tishya", "phone": "7016472708", "email": "283tishyapatel@gmail.com", "address": "Gujarat,India"}
]

@app.route("/")
def index():
    return render_template("index.html", contacts=contacts)

@app.route("/create", methods=["POST"])
def create():
    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']
    address = request.form['address']
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    return redirect(url_for("index"))

@app.route("/update/<int:index>", methods=["GET", "POST"])
def update(index):
    contact = contacts[index]
    if request.method == "POST":
        contact['name'] = request.form["name"]
        contact['phone'] = request.form["phone"]
        contact['email'] = request.form["email"]
        contact['address'] = request.form["address"]
        return redirect(url_for("index"))
    return render_template("update.html", contact=contact, index=index)

@app.route("/delete/<int:index>")
def delete(index):
    del contacts[index]
    return redirect(url_for("index"))

@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        search_term = request.form["search"]
        results = [contact for contact in contacts if search_term.lower() in contact["name"].lower()]
        return render_template("index.html", contacts=results)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
