from flask import Flask, jsonify, render_template, request
# ----------------------------------------------------------------------
# Import Section
# ----------------------------------------------------------------------

from flask import Flask, jsonify

from HackNC2019 import database

app = Flask(__name__)


# ----------------------------------------------------------------------
# Class and Methods
# ----------------------------------------------------------------------

@app.route("/")
def test():
    input_var = "WMT"
    create_entry = database.Database(input_var)
    create_stock_input = create_entry.export()
    return jsonify(create_stock_input)


@app.route("/watchtest")
def watch_test():
    watchlist = database.data_store()
    return jsonify(watchlist)


@app.route("/indextest")
def index_test():
    return "hello", render_template(
        'database.html')


@app.route("/hometest")
def home_test():
    return render_template('database.html')


@app.route("/hometest", methods=['POST'])
def home_form():
    action = request.form['action']
    search = request.form['search']
    if action == '1':
        create_entry = database.Database(search)
        create_stock_input = create_entry.export()
        return jsonify(create_stock_input)


if __name__ == "__main__":
    app.run()
